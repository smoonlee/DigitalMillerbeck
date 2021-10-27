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
CheckTime = 0
while CheckTime < 5:
    if track0.value() == 0 and track1.value() == 0:
        S18Green.value(1)
        S18Red.value(0)
        S19Green.value(1)
        S19Red.value(0)
        S20Green.value(1)
        S20Red.value(0)
        State = 0
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
    CheckTime = CheckTime + 1
    time.sleep(1.0)

while True:
    # Define Circuit Values
    if track0.value() == 1 and track1.value() == 0:
        # State 1 = Tunnel Occupied
        State = 1
        time.sleep(0.1)
        print("Section1")
        print("State", State)

    if track0.value() == 0 and track1.value() == 1:
        # State 2 = bank Occupied
        State = 2
        time.sleep(0.1)
        print("Section2")
        print("State", State)

    if track0.value() == 1 and track1.value() == 1:
        # State 3 = Both Occupied
        State = 3
        time.sleep(0.1)
        print("SectionBoth")
        print("State", State)

    # State 0 = Blank - Boot Order
    # State 1 = Tunnel Occupied - Done
    # State 2 = bank Occupied
    # State 3 = Both Occupied
    while State == 1:
        print("Starting State 1")
        # 1)tunnel occupied-S18 and s20 to red
        if track0.value() == 1 and track1.value() == 0:
            print("[S1] Train Detected in Tunnel - Section 1")
            S18Green.value(0)
            S18Red.value(1)
            S19Green.value(1)
            S19Red.value(0)
            S20Green.value(0)
            S20Red.value(1)
            time.sleep(0.1)

        # 2)Tunnel occupied and then 2nd section occupied- s19 to red
        if track0.value() == 1 and track1.value() == 1:
            print("[S1] Train Detected in Tunnel - Section 2")
            S18Green.value(0)
            S18Red.value(1)
            S19Green.value(0)
            S19Red.value(1)
            time.sleep(0.1)

        # 3)Both occupied and tunnel clears- s18 to green
        if track0.value() == 0 and track1.value() == 1:
            print("[S1] Tunnel Clear")
            S18Red.value(0)
            S18Green.value(1)
            time.sleep(0.1)

        # 4)both clear- all to green, this is the main 'reset state'
        if track0.value() == 0 and track1.value() == 0:
            print("[S1] All Track Clear")
            S18Green.value(1)
            S18Red.value(0)
            S19Green.value(1)
            S19Red.value(0)
            S20Green.value(1)
            S20Red.value(0)
            time.sleep(0.1)
            State = 0
            print(State)

    while State == 2:
        print("Starting State 2")
        # 5)2nd section occupied while tunnel is clear- s18, s19, s20 all red
        if track0.value() == 0 and track1.value() == 1:
            print("[S2] Train Detected in Tunnel - Section 2")
            S18Green.value(0)
            S18Red.value(1)
            S19Green.value(1)
            S19Red.value(0)
            S20Green.value(0)
            S20Red.value(1)
            time.sleep(0.1)

        # 6)tunnel become occupied while 2nd occupied- s18, s19, s20 all red
        if track0.value() == 1 and track1.value() == 1:
            print("[S2] Train Detected in Tunnel - Section 1")
            S18Green.value(0)
            S18Red.value(1)
            S19Green.value(0)
            S19Red.value(1)
            S20Green.value(0)
            S20Red.value(1)
            time.sleep(0.1)

        # 7)2nd section clears while tunnel occupied- s19 to green
        if track0.value() == 1 and track1.value() == 0:
            print("[S2] Tunnel Clear")
            S20Red.value(0)
            S20Green.value(1)
            time.sleep(0.1)

        # 4)both clear- all to green, this is the main 'reset state'
        if track0.value() == 0 and track1.value() == 0:
            print("[S2] All Track Clear")
            S18Green.value(1)
            S18Red.value(0)
            S19Green.value(1)
            S19Red.value(0)
            S20Green.value(1)
            S20Red.value(0)
            State = 0
            time.sleep(0.1)

    while State == 3:
        print("Starting State 3")
        # 6)tunnel become occupied while 2nd occupied- s18, s19, s20 all red
        if track0.value() == 1 and track1.value() == 1:
            print("[S3] BAD JUJU BADDDD!")
            S18Green.value(0)
            S18Red.value(1)
            S19Green.value(0)
            S19Red.value(1)
            S20Green.value(0)
            S20Red.value(1)
            time.sleep(0.1)
        else:
            State = 0
