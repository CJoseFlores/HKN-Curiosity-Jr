import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class DualServos:
    __DataPin1 = None
    __DataPin2 = None
    __pwm1 = None
    __pwm2 = None

    def __init__(self, servopin1, servopin2):
        self.__DataPin1 = servopin1
        self.__DataPin2 = servopin2
        GPIO.setup(self.__DataPin1, GPIO.OUT)
        GPIO.setup(self.__DataPin2, GPIO.OUT)
        self.__pwm1 = GPIO.PWM(self.__DataPin1, 50)
        self.__pwm2 = GPIO.PWM(self.__DataPin2, 50)
        self.__pwm1.start(0)
        self.__pwm2.start(0)

    def TurnRight(self):
        self.__pwm1.ChangeDutyCycle(10)
        self.__pwm2.ChangeDutyCycle(10)
        time.sleep(0.02)

    def TurnLeft(self):
        self.__pwm1.ChangeDutyCycle(5)
        self.__pwm2.ChangeDutyCycle(5)
        time.sleep(0.02)

    def Reverse(self):
        self.__pwm1.ChangeDutyCycle(5)
        self.__pwm2.ChangeDutyCycle(10)
        time.sleep(0.02)

    def Forward(self):
        self.__pwm1.ChangeDutyCycle(12)
        self.__pwm2.ChangeDutyCycle(6)
        time.sleep(0.02)

    def Stop(self):
        self.__pwm1.stop()
        self.__pwm2.stop()
