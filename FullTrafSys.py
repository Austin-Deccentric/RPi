import RPi.GPIO as GPIO
import time
import signal

#Hardware setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT) #power to Q1
GPIO.setup(13,GPIO.OUT) #power to Q2
GPIO.setup(15,GPIO.OUT) #power to Q3
GPIO.setup(19,GPIO.OUT) #power to Q4
GPIO.output(11,True) #light red
GPIO.output(13,True) #light red
GPIO.output(15,True) #light red
GPIO.output(19,True) #light red
GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #input from sensor I1
GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #INPUT FROM SENSOR I2
GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #input from sensor I3
GPIO.setup(24,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #input from sensor I4
GPIO.setup(26,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #input from sensor I5
GPIO.setup(32,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #input from sensor I6
GPIO.setup(36,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #input from sensor I7
GPIO.setup(38,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #input from sensor I8

def allLightsOff(signal,frame):
    GPIO.output(11,True)
    GPIO.output(13,True)
    GPIO.cleanup()
    sys.exit(0)
signal.signal(signal.SIGINT,allLightsOff)


try:
    while True :
        print("In the Loop")
    
    #For first GREEN light
        if GPIO.input(16): #Because the optocoupolers use negative logic,1 means low density
            print("No Traffic")
            GPIO.output(11,True)
        else:
            print("High density on lane1") 
            GPIO.output(11,False)
            print("Greeen light goes ON")
            time.sleep(10)
            GPIO.output(11,True)
            time.sleep(2)
            #print("Greeen light goes on")
        if GPIO.input(18) == 0:
            print("Low density on lane1")
            GPIO.output(11,False)
            time.sleep(5)
            GPIO.output(11,True)
            time.sleep(1)
        else:
            GPIO.output(11,True)
                
        #For Second GREEN light
        if GPIO.input(22):
            print("No Traffic")
            GPIO.output(13,True)
        else:
            print("High density on lane2") 
            GPIO.output(13,False)
            print("Greeen2 light goes ON")
            time.sleep(10)
            GPIO.output(13,True)
            time.sleep(2)
        if GPIO.input(24) == 0:
            print("Low Density on Lane2")
            GPIO.output(13,False)
            time.sleep(5)
            GPIO.output(13,True)
            time.sleep(2)
        else:
            GPIO.output(13,True)
            
        #for third GREEN Light
        if GPIO.input(26):
            print("No Traffic")
            GPIO.output(15,True)
        else:
            print("High density on lane3") 
            GPIO.output(15,False)
            print("Greeen2 light goes ON")
            time.sleep(10)
            GPIO.output(15,True)
            time.sleep(2)
        if GPIO.input(32) == 0:
            print("Low Density on Lane3")
            GPIO.output(15,False)
            time.sleep(5)
            GPIO.output(15,True)
            time.sleep(2)
        else:
            GPIO.output(15,True)
            
        #for Fourth Green Light#
        if GPIO.input(36):
            print("No Traffic")
            GPIO.output(19,True)
        else:
            print("High density on lane4") 
            GPIO.output(19,False)
            print("Greeen2 light goes ON")
            time.sleep(10)
            GPIO.output(19,True)
            time.sleep(2)
        if GPIO.input(38) == 0:
            print("Low Density on Lane4")
            GPIO.output(19,False)
            time.sleep(5)
            GPIO.output(19,True)
            time.sleep(2)
        else:
            GPIO.output(19,True)
                
       
        
        GPIO.input(16)
        GPIO.input(18)
        GPIO.input(22)
        GPIO.input(24)
        GPIO.input(26)
        GPIO.input(32)
        GPIO.input(36)
        GPIO.input(38)

        
finally:
    print("End of program")
    GPIO.cleanup()
