# Import Python Modules
import RPi.GPIO as GPIO

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

SoftLock=1

# Code
while True:
 # Set Signal Red
 if GPIO.input(20) == GPIO.HIGH:
    SoftLock = 0
    print(SoftLock)
    GPIO.output(26,1) # Clear Green
    GPIO.output(16,1) # Clear White
    print("Signal Red")

 # Set Signal Green - Clear Red
 if GPIO.input(19) == GPIO.HIGH and SoftLock == 0:
    SoftLock = 1
    print(SoftLock)
    GPIO.output(21,1) # Clear Red
    GPIO.output(26,0) # Green Set
    print("Signal Green")

 # Set Signal White - Clear Red
 if GPIO.input(13) == GPIO.HIGH and SoftLock == 0:
    SoftLock = 1
    print(SoftLock)
    GPIO.output(21,1) # Clear Red
    GPIO.output(16,0) # White set
    print("Signal White")
