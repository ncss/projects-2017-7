from microbit import *
import music
import radio
playing = False
radio.on()
radio.config(channel=58)
while True:
    if button_a.was_pressed():
        if playing:
            playing = False
            music.stop()
        else:
            music.play(music.CHASE, wait= False, loop= True)
            sleep(5)
            playing = True
    #if radio.receive() == "music":
        #music.play(music.BA_DING)
        #music.stop()
    if radio.receive() == 'white':
        music.play(music.WAWAWAWAA)

        