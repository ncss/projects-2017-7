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
    if button_a.is_pressed() and button_b.is_pressed():
        radio.send("start")
        initial_acceleration = accelerometer.get_y()
        display.show(Image.HEART)
        sleep(500)
        display.clear()
    
    if message and type(message) == str:
        if str(message) == "impact1":
            music.stop()
            #music.play("C2", wait=False, loop=False)
    
    if y_axis > 600:
        sleep(100)
        display.show(Image.ARROW_N, wait=False)
        radio.send("jump1")
        music.stop()
        #music.play(music.BA_DING, wait=False, loop=False)
        sleep(500)
        display.clear()
    
    if y_axis < -600:
        sleep(200)
        display.show(Image.ARROW_S, wait=False)
        radio.send("crouch1")
        music.stop()
        # music.play(music.BA_DING, wait=False, loop=False)
        sleep(500)
        display.clear()
