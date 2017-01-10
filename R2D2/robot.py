from microbit import *
import radio

def forward():
    pin0.write_digital(0)
    pin16.write_digital(1)
    pin12.write_digital(1)
    pin8.write_digital(0)
    
def stop():
    pin0.write_digital(0)
    pin16.write_digital(0)
    pin12.write_digital(0)
    pin8.write_digital(0)
    
def left():
    pin0.write_digital(1)
    pin16.write_digital(0)
    pin12.write_digital(1)
    pin8.write_digital(0)
  
def right():
    pin0.write_digital(0)
    pin16.write_digital(1)
    pin12.write_digital(0)
    pin8.write_digital(1) 
    
radio.on()
radio.config(channel=58)

while True:
    if button_a.was_pressed():
        forward()
    message = radio.receive()
    if button_b.was_pressed():
        stop()
    elif message == "left":
        left()
        sleep(10)
        stop()
        forward()
    elif message == "right":
        right()
        sleep(10)
        stop()
        forward()