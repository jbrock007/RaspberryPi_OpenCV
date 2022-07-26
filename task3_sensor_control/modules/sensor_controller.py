
import time
import statistics

USE_FAKE_GPIO = True # Chage to FALSE if testing in the Raspberry Pi

if USE_FAKE_GPIO:
    from .fake_gpio import GPIO  # For running app
else:
    import RPi.GPIO as GPIO  # For testing in Raspberry Pi


# import ...

class SensorController:

    def __init__(self):
        self.PIN_TRIGGER = 18  # do not change
        self.PIN_ECHO = 24  # do not change
        self.distance = None
        self.shape_from_distance = [False, False, False]
        print('Sensor controller initiated')

    def track_rod(self):
        # ...
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PIN_TRIGGER, GPIO.OUT)
        GPIO.setup(self.PIN_ECHO, GPIO.IN)

        GPIO.output(self.PIN_TRIGGER, GPIO.LOW)

        print('Monitoring')

        distance_list = []

        for _ in range(10):
            GPIO.output(self.PIN_TRIGGER, GPIO.HIGH)
            time.sleep(0.0001)
            GPIO.output(self.PIN_TRIGGER, GPIO.LOW)
            pulse_start_time = 0
            pulse_end_time = 0
            while GPIO.input(self.PIN_ECHO)==0:
                pulse_start_time = time.time()
            while GPIO.input(self.PIN_ECHO)==1:
                pulse_end_time = time.time()
            pulse_duration = None
            pulse_duration = pulse_end_time - pulse_start_time
            distance = pulse_duration * 17150
            d = round(distance, 2)
            distance_list.append(d)
        print(distance_list)
        self.distance = statistics.median(distance_list)
        print(self.distance)
        return self.distance

    def get_distance(self):
        return self.distance

    def get_shape_from_distance(self):
        self.distance = 16.579
        if int(self.distance) in range(14,20):
            self.shape_from_distance = [True, False, False]
            return self.shape_from_distance
        elif int(self.distance) in range(9,15):
            self.shape_from_distance = [False, True, False]
            return self.shape_from_distance
        elif int(self.distance) in range(4,10):
            self.shape_from_distance = [False, False, True]
            return self.shape_from_distance
        else:
            return self.shape_from_distance
