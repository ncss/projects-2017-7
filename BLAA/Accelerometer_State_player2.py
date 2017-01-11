from microbit import *
import radio
import music

radio.on()
radio.config(channel=65,
address=0x6e637373)
initial_acceleration = accelerometer.get_y()

while True:
    y_axis = accelerometer.get_y() - initial_acceleration
    message = radio.receive()
    if message and type(message) == str:
        if str(message) == "start":
            initial_acceleration = accelerometer.get_y()
            display.show(Image.GIRAFFE)
            sleep(500)
            display.clear()
        elif str(message) == "impact2":
            music.stop()
            music.play("C2", wait=False, loop=False)
    
    if y_axis > 600:
        sleep(100)
        display.show(Image.ARROW_N, wait=False)
        radio.send("jump2")
        music.stop()
        music.play(music.BA_DING, wait=False, loop=False)
        sleep(500)
        display.clear()
    
    if y_axis < -600:
        sleep(200)
        display.show(Image.ARROW_S, wait=False)
        radio.send("crouch2")
        music.stop()
        music.play(music.BA_DING, wait=False, loop=False)
        sleep(500)
        display.clear()
