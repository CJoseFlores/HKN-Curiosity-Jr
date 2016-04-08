import RPi.GPIO as GPIO
import time
import random

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
servoPin1 = 14
servoPin2 = 18
GPIO.setup(servoPin1, GPIO.OUT)
GPIO.setup(servoPin2, GPIO.OUT)
pwm1 = GPIO.PWM(servoPin1, 50)
pwm2 = GPIO.PWM(servoPin2, 50)
pwm1.start(0)
pwm2.start(0)

while (1):
	tempForward = open('Forward', 'r')
	fileForward = int(tempForward.read())

	tempReverse = open('Reverse', 'r')
	fileReverse = int(tempReverse.read())

	tempLeft = open('Left', 'r')
	fileLeft = int(tempLeft.read())

	tempRight = open('Right', 'r')
	fileRight = int(tempRight.read())

	tempRoam = open('Roam', 'r')
	fileRoam = int(tempRoam.read())


	while(fileRight == 1):
		pwm1.ChangeDutyCycle(10)
		pwm2.ChangeDutyCycle(10)
		time.sleep(0.02)
		tempRight = open('Right', 'r')
	        fileRight = int(tempRight.read())

	while(fileLeft == 1):
		pwm1.ChangeDutyCycle(5)
		pwm2.ChangeDutyCycle(5)
		time.sleep(0.02)
		tempLeft = open('Left', 'r')
	        fileLeft = int(tempLeft.read())

	while(fileReverse == 1):
		pwm1.ChangeDutyCycle(5)
		pwm2.ChangeDutyCycle(10)
		time.sleep(0.02)
		tempReverse = open('Reverse', 'r')
        	fileReverse = int(tempReverse.read())

	while(fileForward == 1):
		pwm1.ChangeDutyCycle(12)
		pwm2.ChangeDutyCycle(6)
		time.sleep(0.02)
		tempForward = open('Forward', 'r')
        	fileForward = int(tempForward.read())
pwm1.stop()
pwm2.stop()
GPIO.cleanup()
