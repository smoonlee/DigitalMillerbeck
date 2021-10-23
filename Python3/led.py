  GNU nano 3.2                                             led.py

# Raspberry Pi GPIO Sample Code
# https://learn.sparkfun.com/tutorials/raspberry-gpio/all
# Author: Simon Lee | @smoon_lee


# Import Python Modules
import RPi.GPIO as GPIO

# Define GPIO Board Configuration
GPIO.setmode(GPIO.BCM)

# Define GPIO Pin Config
GPIO.setup(21, GPIO.OUT) # White LED  (OFF)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Push Button (Off)

# Button Push Print
# https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/
while True: # Run forever
    if GPIO.input(20) == GPIO.HIGH:
        GPIO.output(21, 1)
        print("Button was pushed!")

    if GPIO.input(20) == GPIO.LOW:
        GPIO.output(21, 0)
