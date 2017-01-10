from microbit import *
import music
import radio
import math

#maximum and minimum z values to be detected as sitting up / falling down
MAX_THRESHOLD = -200
MIN_THRESHOLD = -900

#minimum time in ms for sit ups (to avoid cheating)
MIN_UP_TIME = 800
MIN_DOWN_TIME = 800

CHANNEL = 95

beat_frequency = 5
situp_count = 0

up = True
up_start = running_time()
down_start = running_time()
situp_start = running_time()

running = False

radio.on()
radio.config(channel = CHANNEL) 

def show_display(n):
    display.clear()
    n %= 25
    for i in range(n // 5):
        for j in range(5):
            display.set_pixel(i, j, 9)
    for i in range(n % 5):
        display.set_pixel(int(n // 5), i, 9)
    
   
    
while True:
    
    if button_a.was_pressed():
        
        display.show("3")
        sleep(1000)
        display.show("2")
        sleep(1000)
        display.show("1")
        sleep(1000)
        display.show(Image.HEART)
        running = True
        radio.send("start " + str(situp_start)) 
    
    if not running:
        continue
    
    
    
    msg = radio.receive()
    if msg:
        if msg.startswith("finish "):
            t = int(msg[len("finish "):])
            display.scroll("You won! You took " + str(t) + " seconds.")
            break
    
    z = accelerometer.get_z()
    
    
    
    #lying down
    if z > MAX_THRESHOLD:
        if up:
            time_taken = running_time() - up_start
            if time_taken >= MIN_UP_TIME:
                #play music
                music.stop()
                #music.play(music.JUMP_UP, wait = False)
                
                situp_count += 0.5
                show_display(situp_count)
                up = False
                
                radio.send("1")
                
    #sitting up
    elif z < MIN_THRESHOLD:
        if not up:
            time_taken = running_time() - down_start
            if time_taken >= MIN_DOWN_TIME:
                #play music
                music.stop()
                #music.play(music.JUMP_DOWN, wait = False)
                
                situp_count += 0.5
                show_display(situp_count)
                up = True
    

    print(situp_count, running_time() - situp_start)
    sleep(100)