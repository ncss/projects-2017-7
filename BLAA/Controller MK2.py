from microbit import *
import radio
import music
import math

radio.on()
radio.config(channel=65, address=0x6e637373)
initial_acceleration = (accelerometer.get_y())

while True:
    Acceleration = ((accelerometer.get_y()) - initial_acceleration) / 100

    if button_a.is_pressed() and button_b.is_pressed():
        initial_acceleration = accelerometer.get_y()
        display.show(Image.HEART)
        sleep(500)
        display.clear()

    if Acceleration > 8:
        display.show(Image.ARROW_N, wait=False)
        radio.send("jump")
        music.play(music.BA_DING, wait=False, loop=False)
        sleep(1000)
        display.clear()
        
    if Acceleration < -6:
        display.show(Image.ARROW_S, wait=False)
        radio.send("crouch")
        music.play("C4:1", wait=False, loop=False)
        sleep(1000)
        display.clear()

# Displacement formula:
#   time_dis = pow(time, 2)
#   displacement = 0.5*(acceleration*time_dis)