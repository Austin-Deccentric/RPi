import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT) #first LED
GPIO.setup(13,GPIO.OUT) #second LED
GPIO.setup(15,GPIO.OUT) #third LED
#Common Ground Pin 9

#Function for blinking a pin for a specific on and off time
def blinking(pin, blinktime):
    GPIO.output(pin, True)
    print("on")
    sleep(blinktime)
    GPIO.output (pin, False)
    print("off")
    sleep(blinktime)

#main program   
starttime = datetime.now() #save the time when the process started
while (datetime.now() - starttime).seconds < 30:
    blinking(11, 3) #blink as long as the difference to the start time is smaller than 60 s

starttime = datetime.now()
while (datetime.now() - starttime).seconds < 30:
    blinking(13, 2)
    
starttime = datetime.now()
while (datetime.now() - starttime).seconds < 10:
    blinking(15, 1)

GPIO.cleanup() #turn off all gpios 

