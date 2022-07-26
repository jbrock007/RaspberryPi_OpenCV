import random
import time


class GPIO(object):
    # Modes
    BCM = "BCM"
    BOARD = "BOARD"
    # Directions
    OUT = 0
    IN = 1
    # Values
    LOW = 0
    HIGH = 1
    # Channels ultrasonic sensor
    PIN_TRIGGER_ULTRASONIC = 18
    PIN_TRIGGER_ULTRASONIC_TEXT = "Ultrasonic sensor trigger"
    PIN_ECHO_ULTRASONIC = 24
    PIN_ECHO_ULTRASONIC_TEXT = "Ultrasonic sensor echo"
    # Channels motor
    PIN_STEP_MOTOR = 25
    PIN_STEP_MOTOR_TEXT = "Motor step"
    PIN_DIR_MOTOR = 8
    PIN_DIR_MOTOR_TEXT = "Motor dir"

    @staticmethod
    def setmode(mode):
        if (mode == GPIO.BCM):
            print("Mode was set: ", mode)
        else:
            print("You are trying to set up the WRONG mode for this project: ",
                  mode)

    @staticmethod
    def setup(channel, direction):
        if (channel == GPIO.PIN_TRIGGER_ULTRASONIC):
            print("Set up channel: ", GPIO.PIN_TRIGGER_ULTRASONIC_TEXT, " ",
                  channel, ", Direction: ", direction)
        elif (channel == GPIO.PIN_ECHO_ULTRASONIC):
            print("Set up channel: ", GPIO.PIN_ECHO_ULTRASONIC_TEXT, " ",
                  channel, ", Direction: ", direction)
        elif (channel == GPIO.PIN_STEP_MOTOR):
            print("Set up channel: ", GPIO.PIN_STEP_MOTOR_TEXT, " ", channel,
                  ", Direction: ", direction)
        elif (channel == GPIO.PIN_DIR_MOTOR):
            print("Set up channel: ", GPIO.PIN_DIR_MOTOR_TEXT, " ", channel,
                  ", Direction: ", direction)
        else:
            print("WRONG channel: ", channel)

        if (direction != GPIO.OUT and direction != GPIO.IN):
            print("ERROR: The passed direction for the setup is WRONG: ",
                  direction)

    @staticmethod
    def output(channel, value):
        if (channel == GPIO.PIN_TRIGGER_ULTRASONIC):
            print("Output channel: ", GPIO.PIN_TRIGGER_ULTRASONIC_TEXT, " ",
                  channel, ", Value: ", value)
        elif (channel == GPIO.PIN_STEP_MOTOR):
            print("Output channel: ", GPIO.PIN_STEP_MOTOR_TEXT, " ", channel,
                  ", Value: ", value)
        elif (channel == GPIO.PIN_DIR_MOTOR):
            print("Output channel: ", GPIO.PIN_DIR_MOTOR_TEXT, " ", channel,
                  ", Value: ", value)
        else:
            print("WRONG channel: ", channel)

        if (value != GPIO.LOW and value != GPIO.HIGH):
            print("ERROR: The passed value for the output is WRONG: ", value)

    @staticmethod
    def input(channel):
        if (channel == GPIO.PIN_ECHO_ULTRASONIC):
            print("Input in channel: ", GPIO.PIN_ECHO_ULTRASONIC_TEXT, " ",
                  channel)
        else:
            print("WRONG channel: ", channel)

        time.sleep(random.uniform(0, 1))
        return random.randint(0, 1)

    @staticmethod
    def cleanup():
        print("Cleaning up")
