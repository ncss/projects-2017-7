from microbit import *
import music
import radio

radio.on()
radio.config(channel=58)
while True:
    if radio.receive() == "music":
        music.play(music.BA_DING)
        music.stop()
    if radio.receive() == 'white':
        music.play(music.WAWAWAWAA)

        