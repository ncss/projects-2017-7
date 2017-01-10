from microbit import *
import radio

radio.on()
radio.config(channel=65,
address=0x6e637373)
initial_acceleration = accelerometer.get_y()

while True:
    y_axis = accelerometer.get_y() - initial_acceleration
    
    if button_a.is_pressed() and button_b.is_pressed():
        initial_acceleration = accelerometer.get_y()
        display.show(Image.HEART)
        sleep(500)
        display.clear()
    
    if y_axis > 600:
        sleep(200)
        display.show(Image.ARROW_N, wait=False)
        radio.send("jump")
        sleep(1000)
        display.clear()
    
    if y_axis < -600:
        sleep(400)
        display.show(Image.ARROW_S, wait=False)
        radio.send("crouch")
        sleep(1000)
        display.clear()
    else:
        radio.send("stand")