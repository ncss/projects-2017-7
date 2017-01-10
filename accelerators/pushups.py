from microbit import *

startz = 0
pushupsCount = 0
onFloor = False

while True:
    if button_a.was_pressed():
        display.show("3")
        sleep(1000)
        display.show("2")
        sleep(1000)
        display.show("1")
        sleep(1000)
        display.clear()
        
        #calibrating - planking
        startz = accelerometer.get_z()
        
    z = accelerometer.get_z() - startz
    print(z)
    
    #lowered onto floor
    if not onFloor and z < -150:
        #play music
        onFloor = True
    
    #pushed up
    if onFloor and z > 0:
        onFloor = False
        pushupsCount += 1
    
    print(pushupsCount)