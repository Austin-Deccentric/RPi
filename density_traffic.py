import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
##GPIO.setup(3,GPIO.OUT) #first red light
GPIO.setup(5,GPIO.OUT) #first green light
##GPIO.setup(7,GPIO.OUT) #second RED light
GPIO.setup(8,GPIO.IN) #Second Green light
##GPIO.setup(10,GPIO.IN) #SENSOR
I1 = GPIO.input(8)
##I2 = GPIO.input(10)

try:
    while 1 :
        if I1:
            GPIO.output(5,True)
            print("Green light goes off")
            time.sleep(10)
            GPIO.output(5,False)
            print("Green On")
            time.sleep(5)
            continue
           
            
        else:
            print("High density") 
            GPIO.output(5,False)
            print("Greeen light goes on")
            time.sleep(10)
            GPIO.output(5,True)
            print("Green light is OFF")
            time.sleep(5)
            break
            
##        if 11 or I2:
##            GPIO.output(5,False)
##            print("Green light is on")
##            time.sleep(5)
##            GPIO.output(5,True)
##            print("Green light is off")
##        else:
##            GPIO.output(5,True)
##            print("NO TRAFFIC")
finally:
    GPIO.cleanup()
    




