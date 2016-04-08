#This uses modified code credited to Jeremy Blythe at:
#https://github.com/jerbly/Pi/blob/master/distance-screen.py
import mcp3008
import time
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# change these as desired - they're the pins connected from the
# SPI port on the ADC to the Cobbler
SPICLK = 11
SPIMISO = 9
SPIMOSI = 10
SPICS = 8
# set up the SPI interface pins
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPICS, GPIO.OUT)


#Reads from the mcp3008 chip, and outputs the calculated distance from the
#SHARP IR Sensor

def get_distance(mcp3008_ch):
    num_samples = 10
    r = []
    for i in range (0,num_samples):
        r.append(mcp3008.readadc(mcp3008_ch, SPICLK, SPIMOSI, SPIMISO, SPICS))
    a = sum(r)/float(num_samples)
    v = (a/1023.0)*3.3
    d = 16.2537 * v**4 - 129.893 * v**3 + 382.268 * v**2 - 512.611 * v + 306.439
    return int(round(d))

def get_distance2(mcp3008_ch):
    num_samples = 10
    r = []
    for i in range (0,num_samples):
        r.append(mcp3008.readadc(mcp3008_ch, SPICLK, SPIMOSI, SPIMISO, SPICS))
    a = sum(r)/float(num_samples)

    sensorRet = mcp3008.readadc(mcp3008_ch, SPICLK, SPIMOSI, SPIMISO, SPICS)

    sensorRet = sensorRet * 500 / 1023
    if(sensorRet == 0):
        sensorRet = 1

    sensorRet = 3200 / sensorRet-3

    return int(sensorRet)

#This method involves using mcp3008 with the SPI drivers.
#No GPIO are used, and all sensors are connected to
#mcp3008 channels 0-7

#