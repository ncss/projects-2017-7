from microbit import *
import radio
win = False
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

start = running_time()
while True:
    message = radio.receive()
    if message:
        forward()
        sleep(500)
        stop()
    if win == False:
        if pin1.read_analog() < 10 or pin2.read_analog() < 10:
            end = running_time()
            timer = int((end - start)/1000)
            radio.send('I won!')
            display.scroll('You won! You took ' + str(timer) + 's', wait = False)
            win = True
    if button_b.was_pressed():
        win = False
