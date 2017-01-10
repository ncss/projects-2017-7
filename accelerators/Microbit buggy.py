from microbit import *
import radio

radio.on()
radio.config(channel=95,
address = 0x75626974)

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
    message = radio.receive()
    if message:
        forward()
        sleep(500)
        stop()

  
    
