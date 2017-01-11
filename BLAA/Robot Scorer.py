from  microbit import *
import radio

def forward():
    pin0.write_digital(1)
    pin16.write_digital(0)
    pin12.write_digital(0)
    pin8.write_digital(1)

def backward():
    pin0.write_digital(0)
    pin16.write_digital(1)
    pin12.write_digital(1)
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

def stop():
    pin0.write_digital(0)
    pin16.write_digital(0)
    pin12.write_digital(0)
    pin8.write_digital(0)

radio.on()
radio.config(channel = 65,
address=0x6e637373)
while True:
    message = radio.receive()
    if message == "Robot1":
        forward()
        sleep(1000)
        stop()
    if message == "Robot2":
        backward()
        sleep(1000)
        stop()
