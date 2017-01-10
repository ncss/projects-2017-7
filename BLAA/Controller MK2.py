from microbit import *

initial_acceleration = (accelerometer.get_y())

while True:
    Acceleration = ((accelerometer.get_y()) - initial_acceleration) / 100
    Velocity = Acceleration
    print(Velocity)
    sleep(100)

    if button_a.is_pressed() and button_b.is_pressed():
        initial_acceleration = accelerometer.get_y()
        display.show(Image.HEART)
        sleep(500)
        display.clear()

    if Acceleration > 8:
        display.show(Image.ARROW_N, wait=False)
        sleep(1000)
        display.clear()
        
    if Acceleration < -8:
        display.show(Image.ARROW_S, wait=False)
        sleep(1000)
        display.clear()
