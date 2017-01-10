from microbit import *

MAX_THRESHOLD = 950
MIN_THRESHOLD = 150

situp_count = 0
up = False

while True:
    z = accelerometer.get_z()
    
    if z > MAX_THRESHOLD:
        if up:
            situp_count += 0.5
            up = False
        else:
            #do nothing
           x = 1 
    elif z < MIN_THRESHOLD:
        if up:
            #dp mptjomg
            x = 1
        else:
            situp_count += 0.5
            up = True
    
    
    print(situp_count, accelerometer.get_z())
    sleep(100)