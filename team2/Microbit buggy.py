from microbit import *
def forward():
    pin0.write_digital(1)
    pin16.write_digital(0)
    pin12.write_digital(0)
    pin8.write_digital(1)
        
def stop():
    pin0.write_digital(0)
    pin16.write_digital(0)
    pin12.write_digital(0)
    pin8.write_digital(0)

while True: 
    if button_a.was_pressed():
        forward()
        sleep(2000)
        stop()
        
    