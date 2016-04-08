#Code credited to Jeremy Blythe at:
#https://github.com/jerbly/Pi/blob/master/mcp3008.py
import spidev
import time
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def readadc(adcnum, clockpin, mosipin, misopin, cspin):
    if ((adcnum > 7) or (adcnum < 0)):
        return -1
    GPIO.output(cspin, True)

    GPIO.output(clockpin, False) # start clock low
    GPIO.output(cspin, False) # bring CS low
    commandout = adcnum
    commandout |= 0x18 # start bit + single-ended bit
    commandout <<= 3 # we only need to send 5 bits here

    for i in range(5):
        if (commandout & 0x80):
            GPIO.output(mosipin, True)
        else:
            GPIO.output(mosipin, False)
        commandout <<= 1
        GPIO.output(clockpin, True)
        GPIO.output(clockpin, False)

    adcout = 0
# read in one empty bit, one null bit and 10 ADC bits
    for i in range(12):
        GPIO.output(clockpin, True)
        GPIO.output(clockpin, False)
        adcout <<= 1
        if (GPIO.input(misopin)):
            adcout |= 0x1

    GPIO.output(cspin, True)

    adcout >>= 1 # first bit is 'null' so drop it
    return adcout

#spi = spidev.SpiDev()
#spi.open(0,0)

# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
#def readadc(adcnum):
#    if ((adcnum > 7) or (adcnum < 0)):
#        return -1
#    r = spi.xfer2([1,(8+adcnum)<<4,0])
#    adcout = ((r[1]&3) << 8) + r[2]
#    return adcout

