from microbit import *
import music
import radio

radio.on()
radio.config(channel=58)
while True:
    if radio.receive() == "music":
        music.play(music.BA_DING)
        sleep(200)
        music.stop()
    if radio.receive() == 'stop':
        music.play(music.WAWAWAWAA)

        