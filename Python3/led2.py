# Import Python3 Modules
import RPi.GPIO as GPIO

# Configure Pin Read Out
GPIO.setmode(GPIO.BCM)

# Configure PIN Status
GPIO.setup(21, GPIO.OUT, initial=GPIO.HIGH) #LED White - Status - OFF
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Push Button (Off)

# Button Push Print
# https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/
while True: # Run forever
    if GPIO.input(20) == GPIO.LOW:
        GPIO.output(21, 1)

    if GPIO.input(20) == GPIO.HIGH:
        GPIO.output(21, 0)
        print("Button was pushed!")

# Clean up
GPIO.cleanup()
