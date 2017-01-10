from microbit import *

while True:
    if button_a.was_pressed():
        break
    else:
        x = accelerometer.get_x()
        y = accelerometer.get_y()
        z = accelerometer.get_z()
        print(str(x) + ", " + str(y) + ", " + str(z))
        sleep(500)