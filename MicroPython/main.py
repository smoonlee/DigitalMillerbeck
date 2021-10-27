# Import Modules
from machine import Pin
import time

# Define Led
S18Red = Pin(16, Pin.OUT) # Entrance
S18Green   = Pin(17, Pin.OUT)

S19Red = Pin(18, Pin.OUT) # Tunnel
S19Green   = Pin(19, Pin.OUT)

S20Red = Pin(20, Pin.OUT) # Bank Reverse
S20Green   = Pin(21, Pin.OUT)

# Define Detection
track0 = Pin(14, Pin.IN, Pin.PULL_DOWN) #enter BROWN
track1 = Pin(15, Pin.IN, Pin.PULL_DOWN) #mid  RED

State = 0

# Order of Play
#1)tunnel occupied-S18 and s20 to red
#2)Tunnel occupied and then 2nd section occupied- s19 to red
#3)Both occupied and tunnel clears- s18 to green
#4)both clear- all to green, this is the main 'reset Circuit'
#5)2nd section occupied while tunnel is clear- s18, s19, s20 all red
#6)tunnel become occupied while 2nd occupied- s18, s19, s20 all red
#7)2nd section clears while tunnel occupied- s19 to green

# System Book Defaults
S18Green.value(1)
S18Red.value(1)

S19Green.value(1)
S19Red.value(1)

S20Green.value(1)
S20Red.value(1)
time.sleep(1)
print('LED SAFE - System Booted!')

# 0 Check Status
while True:
    if track0.value() == 0 and track1.value() == 0:
        S18Green.value(1)
        S18Red.value(0)
        S19Green.value(1)
        S19Red.value(0)
        S20Green.value(1)
        S20Red.value(0)
        Circuit0 = 0
        Circuit1 = 0
        State = 0
        print('All Clear')
        print('State',State)
    else:
        S18Green.value(0)
        S18Red.value(1)
        S19Green.value(0)
        S19Red.value(1)
        S20Green.value(0)
        S20Red.value(1)
        Circuit0 = 1
        Circuit1 = 1
        print('Something Found')
        
    # Define Circuit Values
    if track0.value() == 1 and track1.value() == 0:
        Circuit0 = 1
        Circuit1 = 0
        State = 1
        print('Section1')
        print('State',State)
        
    if track0.value() == 0 and track1.value() == 1:
        Circuit0 = 0
        Circuit1 = 1
        State = 2
        print('Section2')
        print('State',State)
        
    if track0.value() == 1 and track1.value() == 1:
        Circuit0 = 1
        Circuit1 = 1
        State = 3
        print('SectionBoth')
        print('State',State)
        
    # Check GOTO for Startup Loop

    # State Value -
    while State == 0:
        print('Starting State 0')
        time.sleep(1)
        print('End State 0')
        break
  
    # State value 1
    while State == 1:
            Print('Starting State 1')
            # 1)tunnel occupied-S18 and s20 to red
            if track0.value() == 1 and track1.value() == 0:
                print('Train Detected in Tunnel - Section 1')
                S18Green.value(0)
                S18Red.value(1)
                S19Green.value(1)
                S19Red.value(0)
                S20Green.value(0)
                S20Red.value(1)
                time.sleep(0.1)
                
            #2)Tunnel occupied and then 2nd section occupied- s19 to red
            if track0.value() == 1 and track1.value() == 1:
                print('Train Detected Section Two')
                S18Green.value(0)
                S18Red.value(1)
                S19Green.value(0)
                S19Red.value(1)
                time.sleep(0.1)

            #3)Both occupied and tunnel clears- s18 to green
            if track0.value() == 0 and track1.value() == 1:
                print('Tunnel Clear')
                S18Red.value(0) 
                S18Green.value(1) 
                time.sleep(0.1)
                
            #4)both clear- all to green, this is the main 'reset state'
            if track0.value() == 0 and track1.value() == 0:
                print('All Track Clear')
                S18Green.value(1)
                S18Red.value(0)
                S19Green.value(1)
                S19Red.value(0)
                S20Green.value(1)
                S20Red.value(0)
                time.sleep(0.1)  
    print('End State 1')                            
    break
    
        # State value 2
    while State == 2:
            Print('Starting State 2')
            #5)2nd section occupied while tunnel is clear- s18, s19, s20 all red            
            if track0.value() == 0 and track1.value() == 1:
                print('[S2] Train Coming from Bank')
                S18Green.value(0)
                S18Red.value(1)
                S19Green.value(0)
                S19Red.value(1)
                S20Green.value(0)
                S20Red.value(1)
                time.sleep(0.1)
                
            #6)tunnel become occupied while 2nd occupied- s18, s19, s20 all red
            if track0.value() == 1 and track1.value() == 1:
                print('[S2] Train Detected Section Two')
                S18Green.value(0)
                S18Red.value(1)
                S19Green.value(0)
                S19Red.value(1)
                S20Green.value(0)
                S20Red.value(1)
                time.sleep(0.1)

            #7)2nd section clears while tunnel occupied- s19 to green
            if track0.value() == 1 and track1.value() == 0:
                print('[S2] Tunnel Clear')
                S19Red.value(0) 
                S19Green.value(1) 
                time.sleep(0.1)
                
            #4)both clear- all to green, this is the main 'reset state'
            if track0.value() == 0 and track1.value() == 0:
                print('[S2] All Track Clear')
                S18Green.value(1)
                S18Red.value(0)
                S19Green.value(1)
                S19Red.value(0)
                S20Green.value(1)
                S20Red.value(0)
                time.sleep(0.1)

                
    print('End State 2')
    break


