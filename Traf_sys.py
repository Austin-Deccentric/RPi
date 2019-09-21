import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT) #power to first green light
GPIO.setup(5,GPIO.OUT) #power to second green light
GPIO.setup(7,GPIO.OUT)#power to third green light
GPIO.setup(11,GPIO.OUT)#power to fourth green light
GPIO.setup(8,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #input from sensor I1
GPIO.setup(10,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #INPUT FROM SENSOR I3
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #INPUT FROM SENSOR I6
GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #INPUT FROM SENSOR I8
I1 = GPIO.input(8)
I3 = GPIO.input(10)
I6 = GPIO.input(12)
I8 = GPIO.input(16)

def my_callback2():
    GPIO.output(5,False)
    print("Seocnd Green ON")
    time.sleep(5)
    
def my_callback3():
    GPIO.output(7,False)
    print("Third Green ON")
    time.sleep(5)
    
def my_callback4():
    GPIO.output(11,False)
    print("Fourth GREEN ON")
    time.sleep(5)
    
def my_callback1():
    GPIO.output(3,False)
    print("Fisrt Green ON")
    time.sleep(5)
    
Lane1 = GPIO.add_event_detect(8,GPIO.FALLING)
Lane2 = GPIO.add_event_detect(10,GPIO.FALLING)
Lane3 = GPIO.add_event_detect(12,GPIO.FALLING)
Lane4 = GPIO.add_event_detect(16,GPIO.FALLING)
try:
    print("In the loop")
    while 1 :  #Because the optocoupolers use negative logic,1 means low density
        print("Program is here")
        if Lane1:   # Both sensors have no obstacle between them
            print("High density on Lane1") 
            GPIO.output(3,False)
            print("Greeen light goes on")
            GPIO.add_event_detect(10,GPIO.FALLING,callback=my_callback2)
            GPIO.add_event_detect(12,GPIO.FALLING,callback=my_callback3)
            GPIO.add_event_detect(16,GPIO.FALLING,callback=my_callback4)
        if Lane2:
            print("High density on Lane2") 
            GPIO.output(5,False)
            print("Greeen light goes on")
            GPIO.add_event_detect(12,GPIO.FALLING,callback=my_callback3)
            GPIO.add_event_detect(16,GPIO.FALLING,callback=my_callback4)
            GPIO.add_event_detect(8,GPIO.FALLING,callback=my_callback1)
        if Lane3:
            print("High density on Lane3") 
            GPIO.output(7,False)
            print("Greeen light goes on")
            GPIO.add_event_detect(16,GPIO.FALLING,callback=my_callback4)
            GPIO.add_event_detect(8,GPIO.FALLING,callback=my_callback1)
            GPIO.add_event_detect(10,GPIO.FALLING,callback=my_callback2)
        if Lane4:
            print("High density on Lane4") 
            GPIO.output(11,False)
            print("Greeen light goes on")
            GPIO.add_event_detect(8,GPIO.FALLING,callback=my_callback1)
            GPIO.add_event_detect(10,GPIO.FALLING,callback=my_callback2)
            GPIO.add_event_detect(12,GPIO.FALLING,callback=my_callback3)
            print("loop End")
finally:
    print("End of program")
    GPIO.cleanup()
    





