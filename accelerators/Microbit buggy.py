from microbit import *
import radio
win = False
radio.on()
radio.config(channel=95,
address = 0x75626974)

running = False

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
        if message.startswith('start '):
            start = int(message[len("start "):])
            running = True
            
    if not running:
        continue
            
    if win == False:
        if pin1.read_analog() < 10 or pin2.read_analog() < 10:
            end = running_time()
            timer = int((end - start)/1000)
            radio.send('finish ' + str(timer))
            display.scroll('You won! You took ' + str(timer) + ' seconds', wait = False)
            win = True
    if button_b.was_pressed():
        win = False

