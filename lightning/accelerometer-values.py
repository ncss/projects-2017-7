from microbit import *

#Import Music library
import music


#Project: right handed arm wrestle


"""
def calibrate():
    xcen=accelerometer.get_x()
    ycen=accelerometer.get_y()
    zcen=accelerometer.get_z()
    return [xcen, ycen, zcen]
"""

while True:
    """
    if button_a.was_pressed():
        print(calibrate())
        sleep(1000)
    """
    z = accelerometer.get_z()
    print(z)
    if z < -900:
        #music.play(music.BA_DING, wait = True)
        display.show(Image.HAPPY, wait = True)
    elif z > 950:
        #music.play(music.POWER_DOWN, wait = True)
        display.show(Image.SAD, wait = True)
    else:
        display.clear()
    
    
"""    
while True:
    
    a = accelerometer.get_values()
    print(a)
    sleep(10)
"""
