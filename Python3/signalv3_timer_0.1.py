# Import Python Modules
import RPi.GPIO as GPIO
import time

# Disable Verbose Message
GPIO.setwarnings(False)

# Configure GPIO Board Read
GPIO.setmode(GPIO.BCM)

# Configure LED GPIO Pins
GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW) # Start Signal RED - System Boot [ON]
GPIO.setup(26, GPIO.OUT, initial=GPIO.HIGH) # Start Signal Green - System Boot [OFF]
GPIO.setup(16, GPIO.OUT, initial=GPIO.HIGH) # Start Signal White - System Boot [OFF]

# Configure Button GPIO Pins
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Push Button (Off)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Signal Green
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Singal White

# Configure Relay GPIO Pins (Air Solenoid)
GPIO.setup(12, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(6, GPIO.OUT, initial=GPIO.HIGH)

# Define Software Lock Starting Point (ON)
SoftLock=1

# Code
while True:
 # Set Signal Red
 if GPIO.input(20) == GPIO.HIGH:
    SoftLock = 0
    print(SoftLock)
    GPIO.output(26,1) # Clear Green
    GPIO.output(16,1) # Clear White
    GPIO.output(12,1) # Clear Air Solenoid
    GPIO.output(6,1) # Clear Air Solenoid
    print("Signal Red")
 else:
    time.sleep(0.1)

 # Set Signal Green - Clear Red
 if GPIO.input(19) == GPIO.HIGH and SoftLock == 0:
    SoftLock = 1
    print(SoftLock)
    GPIO.output(21,1) # Clear Red
    GPIO.output(26,0) # Green Set
    GPIO.output(12,0) # Trigger Relay
    print("Signal Green")
 else:
    time.sleep(0.1)
 # Set Signal White - Clear Red
 if GPIO.input(13) == GPIO.HIGH and SoftLock == 0:
    SoftLock = 1
    print(SoftLock)
    GPIO.output(21,1) # Clear Red
    GPIO.output(16,0) # White set
    GPIO.output(6,0) # Trigger Relay
    print("Signal White")
 else:
    time.sleep(0.1)

# Python3 Cleanup
GPIO.cleanup()

