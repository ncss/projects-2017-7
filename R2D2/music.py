from microbit import *
import music
import radio
playing = False
radio.on()
radio.config(channel=58)
while True:
    if radio.receive() == 'starting':
        music.play(['F4:4', 'R:3', 'F4:4', 'R:3', 'F4:4', 'R:3', 'F5:8'], wait=True)
    #if radio.receive() == 'white':
        #music.play(music.WAWAWAWAA)


        