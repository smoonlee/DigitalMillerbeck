# Import Module
from machine import Pin
import time

# Define LED
led0 = Pin(11, Pin.OUT) # Led White
led1 = Pin(12, Pin.OUT) # Led Green
led2 = Pin(13, Pin.OUT) # Led Red

# Define Button
button = Pin(10, Pin.IN, Pin.PULL_DOWN)

# Debug Code
led0.value(1) # 1 OFF 0 ON
led1.value(1) # 1 OFF 0 ON
led2.value(1) # 1 OFF 0 ON

# Button Code
while True:
    if button.value() == 1:
        led0.value(0) # 1 OFF 0 ON
        print("LED ON")
    else:
        led0.value(1)
    time.sleep(0.1)
