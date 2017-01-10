from microbit import *
import music
import radio

#maximum and minimum z values to be detected as sitting up / falling down
MAX_THRESHOLD = -200
MIN_THRESHOLD = -900

#minimum time in ms for sit ups (to avoid cheating)
MIN_UP_TIME = 800
MIN_DOWN_TIME = 800

CHANNEL = 95

situp_count = 0

up = True
up_start = running_time()
down_start = running_time()

radio.on()
radio.config(channel = CHANNEL)

def reset_timers():
    up_start = running_time()
    down_start = running_time()

while True:
    z = accelerometer.get_z()
    
    if z > MAX_THRESHOLD:
        if up:
            if running_time() - up_start >= MIN_UP_TIME:
                reset_timers()
                
                #play music
                music.stop()
                music.play(music.JUMP_UP, wait = False)
                
                situp_count += 0.5
                up = False
                
                radio.send("1")
    elif z < MIN_THRESHOLD:
        if not up:
            if running_time() - down_start >= MIN_DOWN_TIME:
                reset_timers()
                
                #play music
                music.stop()
                music.play(music.JUMP_DOWN, wait = False)
                
                situp_count += 0.5
                up = True
    
    #radio.send(str(situp_count))
    print(situp_count, accelerometer.get_z())
    sleep(100)