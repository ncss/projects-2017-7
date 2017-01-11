from microbit import *
import music
import radio

PLAYER_NAME = "Player 2"

# maximum and minimum z values to be detected as sitting up / falling down
MAX_THRESHOLD = -200
MIN_THRESHOLD = -900

# minimum time in ms for sit ups (to avoid cheating)
MIN_UP_TIME = 800
MIN_DOWN_TIME = 800

CHANNEL = 95

beat_frequency = 5
situp_count = 0

up = True
up_start = running_time()
down_start = running_time()
situp_start = 0

running = False

radio.on()
radio.config(channel=CHANNEL)


def show_display(n):
    display.clear()
    n %= 25
    for i in range(n // 5):
        for j in range(5):
            display.set_pixel(i, j, 9)
    for i in range(n % 5):
        display.set_pixel(int(n // 5), i, 9)
    
while True:
    
    if not running:
        if button_a.was_pressed():
            display.scroll("waiting", wait=False, loop = True)
            radio.send("ready " + PLAYER_NAME)
        
        msg = radio.receive()
        if msg:
            if msg == "ready both":
                display.clear()
                display.show("3")
                sleep(1000)
                display.show("2")
                sleep(1000)
                display.show("1")
                sleep(1000)
                display.show(Image.HEART)
                situp_start = running_time()
                running = True
        
    else:
        z = accelerometer.get_z()

        # lying down
        if z > MAX_THRESHOLD:
            if up:
                time_taken = running_time() - up_start
                if time_taken >= MIN_UP_TIME:
                    #play music
                    music.stop()
                    music.play(music.JUMP_UP, wait = False)
                    
                    situp_count += 0.5
                    show_display(situp_count)
                    up = False
                    
                    radio.send("forward " + PLAYER_NAME)

        #sitting up
        elif z < MIN_THRESHOLD:
            if not up:
                time_taken = running_time() - down_start
                if time_taken >= MIN_DOWN_TIME:
                    #play music
                    music.stop()
                    music.play(music.JUMP_DOWN, wait = False)
                    
                    situp_count += 0.5
                    show_display(situp_count)
                    up = True
        
        msg = radio.receive()
        if msg:
            if msg.startswith("finish "):
                s = msg[len("finish "):]
                arr = s.split(" ")
                if arr[0] == PLAYER_NAME:
                    display.scroll("You won! You took " + str(arr[1]) + " seconds.", wait = True)
                else:
                    display.scroll("You lost! You took " + str(arr[1]) + " seconds. " + arr[0] + " won in " + str(arr[1]) + " seconds.", wait = True)
                running = False
        
        print(situp_count, running_time() - situp_start)
    
    sleep(100)