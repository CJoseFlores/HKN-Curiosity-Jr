import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.OUT)
#use PWM for duty cycles.
#Slow/Speed motors increase or decrease the duty cycle

#p = GPIO.PWM(channel, freq) where channel is the pin # frequency is in Hz
# p is just a random variable
#p.start(dc)
#^ The above starts the PWM, and the duty cycle is the parameter
#p.ChangeDutyCycle(dc)      #will do exactly that if we want to continually change
#the value/speed/brightness of a motor/led
#p.ChangeFrequency(freq)    #straight forward

#p.stop() stops the PWM

#if you use a for() to change the duty cycle, make sure to have the delay of:
#time.sleep(0.02) so they don't change state too quickly

#For non-continuous servos, the pulse legnth can determine what direction it will fly.

#So for some, doing 0.5 ms pulse will make it go to 0 degrees position (which is directly left)
#and 1.5ms is neutral (straight up), and 2.5ms is 180 degrees 2.5ms

#no matter where the servo is currently at, the time will tell it to go to that direction.

#With a simple program that sends pulses that are 1.5ms each 2 seconds will send the servo
#towars neutral, no matter what direction it is currently in.
#Notice that it's still waay to slow.
#We need to have pulses much more frequently
#Use PWM
#50Hz means 50 pulses in 1 second.
#Eacb pulse will only take 20ms because of the 50hz!!!
#The pulses are too long at 50% Duty cycle.
#This means they are high for 10ms, which is bad we need the 0.5, 1.5 and 2.5ms values
#so to get the duty cycles you need do:
#time you need / pulse length = duty cycle
# so 0.5ms/20ms = 2.5% duty cycle. Do this for all the ones you need.



#so for the arm stuff you'll want something like:

#m1.ChangeDutyCycle(7.5)   Goes to neutral
#time.sleep(1)
#m2.ChangeDutyCycle(12.5)   Goes to 180 degrees
#etc...

#It's good practice to stop PWM when the program ends.

#Keep in mind since we are using Software PWM, it's not super accurate. Use hardware implementation
#for more accuracy you scrub.



#Neutral at otpimal operation is .0015s, so at 50hz,
p = GPIO.PWM(21,50)
p.start(7.5)

while(1):
    p.ChangeDutyCycle(7.5) #Possible Neutral?
    time.sleep(1)