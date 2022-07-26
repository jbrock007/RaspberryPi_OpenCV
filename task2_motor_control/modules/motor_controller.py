import random
from time import sleep


USE_FAKE_GPIO = True # Chage to FALSE if testing in the Raspberry Pi

if USE_FAKE_GPIO:
    from .fake_gpio import GPIO  # For running app
else:
    import RPi.GPIO as GPIO  # For testing in Raspberry Pi


# import ...

class MotorController(object):

    def __init__(self):
        self.working = False
        self.stopped = True
        self.direction = None  # Clockwise Rotation 0 # Counterclockwise Rotation 1
        self.spr = None
        self.msg = None

    def start_motor(self):
        self.stopped = False
        self.working = True
        self.PIN_STEP = 25  # do not change
        self.PIN_DIR = 8  # do not change
        self.direction = random.choice([0, 1]) # Clockwise Rotation 0 # Counterclockwise Rotation 1
        self.spr = random.choice([800, 1600])   # Steps per Revolution (180 / 0.225) = 800 # Steps per Revolution (360 / 0.225) = 1600 
        
        DIRECTION =self.direction
        SPR = self.spr
        DELAY =  0.001875 #0.0375# 0.0208 #0.001875
       
        # GPIO.setwarnings(False)
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PIN_DIR, GPIO.OUT)
        GPIO.setup(self.PIN_STEP, GPIO.OUT)
        
        if DIRECTION == 0 and SPR == 800:
            self.msg = "Rotating 180 degrees in clockwise direction"
            print(self.msg)
        elif DIRECTION == 0 and SPR == 1600:
            self.msg = "Rotating 360 degrees in clockwise direction"
            print(self.msg)
        elif DIRECTION == 1 and SPR == 800:
            self.msg = "Rotating 180 degrees in counterclockwise direction"
            print(self.msg)
        else:
            print("Rotating 360 degrees in counterclockwise direction")
        
        print('Motor started \n')

        GPIO.output(self.PIN_DIR, DIRECTION)
        for x in range(SPR):
            print('Steps left:', SPR-x, '\n')
            #print(self.stopped)
            GPIO.output(self.PIN_STEP, GPIO.HIGH)
            sleep(DELAY)
            GPIO.output(self.PIN_STEP, GPIO.LOW)
            sleep(DELAY)
            #print(self.stopped)
            if self.stopped == True:
                break 
          
        GPIO.cleanup()
        print('Motor stopped')
        self.working = False
        
    def stop_motor(self):
        self.stopped = True
        self.working = False
        return self.stopped

    def is_working(self):
        return self.working