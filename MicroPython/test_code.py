# Millerbeck Tunnel Code
# Version 1.0
# Release Date 27.10.2021

# Import Required Modules
from machine import Pin
import time

# Define LED GPIO Pins
S18Red = Pin(16, Pin.OUT)  # Tunnel Entrance
S18Green = Pin(17, Pin.OUT)
S19Red = Pin(18, Pin.OUT)  # Tunnel Middle
S19Green = Pin(19, Pin.OUT)
S20Red = Pin(20, Pin.OUT)  # Tunnel Bank End
S20Green = Pin(21, Pin.OUT)

# Define Track Circuit GPIO
track0 = Pin(14, Pin.IN, Pin.PULL_DOWN)  # enter BROWN
track1 = Pin(15, Pin.IN, Pin.PULL_DOWN)  # mid  RED

### Code ###
# System Boot Check LED Status
S18Green.value(1)
S18Red.value(1)
S19Green.value(1)
S19Red.value(1)
S20Green.value(1)
S20Red.value(1)
time.sleep(2)
print("System Booted! - LED Check")

# Initial Track Check and Value Config
while True:
    if track0.value() == 0 and track1.value() == 0:
        S18Green.value(1)
        S18Red.value(0)
        S19Green.value(1)
        S19Red.value(0)
        S20Green.value(1)
        S20Red.value(0)
        print("All Clear")
        time.sleep(0.1)
    else:
        S18Green.value(0)
        S18Red.value(1)
        S19Green.value(0)
        S19Red.value(1)
        S20Green.value(0)
        S20Red.value(1)
        print("Object Detected")
        time.sleep(0.1)
        
    # Define Circuit Values
    if track0.value() == 1 and track1.value() == 0:
        Circuit0 = 1
        Circuit1 = 0
        State = 1
        print("Section1")
        print("State", State)

    if track0.value() == 0 and track1.value() == 1:
        Circuit0 = 0
        Circuit1 = 1
        State = 2
        print("Section2")
        print("State", State)

    if track0.value() == 1 and track1.value() == 1:
        Circuit0 = 1
        Circuit1 = 1
        State = 3
        print("SectionBoth")
        print("State", State) 


