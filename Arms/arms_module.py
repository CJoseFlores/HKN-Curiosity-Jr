#! /usr/bin/env python
import RPi.GPIO as GPIO
import time
import mcp3008
import irdist

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Motor:
    __upin = None
    __dpin = None
    __speed = None
    __index = None

    def __init__(self, upin, dpin):
        self.__upin = upin
        self.__dpin = dpin
        GPIO.setup(upin, GPIO.OUT)
        GPIO.setup(dpin, GPIO.OUT)
        return

    def tmove(self, direction, t):
        if (direction == 1):
            GPIO.output(self.__upin, GPIO.HIGH)
            GPIO.output(self.__dpin, GPIO.LOW)
            time.sleep(t)
            self.stop()
        elif(direction == 0):
            GPIO.output(self.__dpin, GPIO.HIGH)
            GPIO.output(self.__upin, GPIO.LOW)
            time.sleep(t)
            self.stop()
        else:
            return

    def move(self,direction):
        if (direction == 1):
            GPIO.output(self.__upin, GPIO.HIGH)
            GPIO.output(self.__dpin, GPIO.LOW)
        elif (direction == 0):
            GPIO.output(self.__dpin, GPIO.HIGH)
            GPIO.output(self.__upin, GPIO.LOW)
        else:
            return
    def stop(self):
        GPIO.output(self.__upin, GPIO.LOW)
        GPIO.output(self.__dpin, GPIO.LOW)
        return

class Arm:
    __m1= None
    __m2 = None
    __m3 = None
    __m4 = None
    #Note that Arm() can only take in Motor Objects as parameters
    def __init__(self, m1, m2, m3, m4):
        self.__m1 = m1
        self.__m2 = m2
        self.__m3 = m3
        self.__m4 = m4
        return

    #This dconfig is based from the original plan.
    #This function will set the robot arm to the default state.
    #The first if statement refers to the sensor connected to channel 1 of the mcp3008
    #The second if statement refers to the sensor connected to channel 2 of the mcp 3008
    def defaultconfig1(self):
        self.stoparm()
        stopflag = [0,0]
        while(stopflag[0] == 0 or stopflag[1] == 0):
            if(irdist.get_distance(1)>123123): #12123 will be replaced with a certain distance reading, reading from channel 1. Ch1 sensor on top of m1
                self.__m1.move(1)#moves up
            else:
                self.__m1.stop()
                stopflag[0] = 1
            if(irdist.get_distance(2)>123123): #Sensor Connected to Channel 2, next to the baseplate
                self.__m2.move(0)#moves down
            else:
                self.__m2.stop()
                stopflag[1] = 1
        return
    #This is from the second plan, where we have 1 sensor on the bottom, 1 on top of m5, and then
    #1 one possibly on top of m1

    def defaultconfig2(self):
        self.stoparm()
        stopflag = 0
        while(stopflag == 0):
            if(irdist.get_distance(1)>5): #ch1 sensor is ontop of m1. If the sensor doesn't detect the arm part, the following if statements
                if(irdist.get_distance(2)<123123):
                    self.__m1.move(1) #m1 begins to move up if the sensor is too low to the ground.
                    self.__m2.stop()
                elif(irdist.get_distance(2)>123123):
                    self.__m2.move(0) #m2 begins to move down if the sensor is too high from the ground.
                    self.__m1.stop()
            else:
                self.__stoparm() #stops all arm movement/operation. The arm should now be in default position.
            stopflag = 1
        return

    def defaultconfig3(self):
        self.stoparm()
        snsr1 = irdist.get_distance2(1)
        snsr3 = irdist.get_distance2(3)
        glitchFinder = 0
        glitchFinder2 = 0
        if(snsr1 > 8):
            while(snsr1 > 8): #The arm is below default position
                self.__m1.move(1) #m1 moves up
                self.__m2.stop()
                snsr1 = irdist.get_distance2(1)
            self.stoparm()

        else: #The arm is above or at default position
            while(snsr1 < 8):
                self.__m1.move(0)#m1 moves down
                self.__m2.stop()
                snsr1 = irdist.get_distance2(1)
            self.stoparm()

        while(glitchFinder < 200 and glitchFinder2 < 200): #This condition moves motor3 down; uses and
            snsr3 = irdist.get_distance2(3)
            if(snsr3 > 11):
                glitchFinder = glitchFinder + 1
            else:
                glitchFinder2 = glitchFinder2 + 1

        if(glitchFinder == 200):
            while(snsr3 > 11):
                self.stoparm()
                self.__m3.move(0)
                snsr3 = irdist.get_distance2(3) #refresh

        self.stoparm()

        #else: #The arm is above or at default position
         #   while(snsr3 < 10):
          #      self.__m3.move(1)#m1 moves down
           #     snsr3 = irdist.get_distance2(3)
            #self.stoparm()


    #The code below is the original plan.
    #This function will lunge into position to grab or drop the payload
    def lunge1(self):
        self.stoparm()
        stopflag = 0
        while(stopflag == 0):
            if(irdist.get_distance(2)<123123):
                self.__m1.move(0)#moves down
                self.__m2.move(1)#moves up
            else:
                self.stoparm()
                stopflag = 1
        return

    def lunge2(self):
        self.stoparm()
        stopflag = 0
        while (stopflag == 0):
            if (irdist.get_distance(3) < 123123):#ch3 sensor is the sensor on top of the rover.
                if (irdist.get_distance(2) < 123123):
                        self.__m1.move(0)  # m2 begins to move down if the sensor is too high to the ground.
                        self.__m2.stop()
                elif (irdist.get_distance(2) > 123123):
                        self.__m2.move(1)  # m3 begins to move up if the sensor is too low from the ground.
                        self.__m1.stop()
            else:
                self.__stoparm()
                stopflag = 1
        return

    def lunge3(self):
        self.stoparm()
        snsr2 = irdist.get_distance2(2)
        self.__m3.tmove(1,1)
        glitchfilter = 0
        while(glitchfilter < 20):
            self.__m1.move(0)
            self.__m2.stop()
            snsr2 = irdist.get_distance2(2)
            if(snsr2 < 4):
                glitchfilter = glitchfilter + 1
        self.stoparm()

    #This function grabs or releases the payload. "action" means either grab or release
    def claw(self, action):
        self.stoparm()
        self.__m4.tmove(action,.75)#Moves for .75 seconds
        return

    def slowclaw(self, action):
        self.stoparm()
        self.__m4.tmove(action, .10)
        time.sleep(.10)
        self.__m4.tmove(action, .10)
        time.sleep(.10)
        self.__m4.tmove(action, .10)
        time.sleep(.10)
        self.__m4.tmove(action, .9)
        return

    def stoparm(self):
        self.__m1.stop()
        self.__m2.stop()
        self.__m3.stop()
        self.__m4.stop()
        return