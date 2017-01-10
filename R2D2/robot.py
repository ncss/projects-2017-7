from microbit import *

def forward():
    pin0.write_digital(1)
    pin16.write_digital(0)
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
    pin12.write_digital(0)
    pin8.write_digital(1)
  
def right():
    pin0.write_digital(0)
    pin16.write_digital(1)
    pin12.write_digital(1)
    pin8.write_digital(0) 
    
radio.on()
radio.config(channel=58)

while True:
    forward
    message = radio.receive()
    if message == "left":
        left
        sleep(500)
        forward
    if message == "right":
        right
        sleep(500)
        forward