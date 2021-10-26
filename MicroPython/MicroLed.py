# Import Module
from machine import Pin

# Define LED
led = Pin(11, Pin.OUT)

# Define Button
button = Pin(10, Pin.IN, Pin.PULL_DOWN)

led.value(1) # 1 OFF 0 ON

# Button Code
while True:
    if button.value() == 1:
        led.value(0) # 1 OFF 0 ON
        print("LED ON")
    else:
        led.value(1)
