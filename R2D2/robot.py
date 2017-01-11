from microbit import *
import radio
#import music
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
    
def digital_left():
    pin0.write_digital(1)
    pin16.write_digital(0)
    pin12.write_digital(1)
    pin8.write_digital(0)
  
def digital_right():
    pin0.write_digital(0)
    pin16.write_digital(1)
    pin12.write_digital(0)
    pin8.write_digital(1) 

def pwm_left():
    pin0.write_digital(0)
    pin16.write_analog(350)
    pin12.write_digital(1)
    pin8.write_digital(0)
    
def pwm_right():
    pin0.write_digital(0)
    pin16.write_digital(1)
    pin12.write_analog(350)
    pin8.write_digital(0)

def reverse():
    pin0.write_digital(1)
    pin16.write_digital(0)
    pin12.write_digital(0)
    pin8.write_digital(1)
    
radio.on()
radio.config(channel=58)
start = 0
display.clear()
pressed = False

while True:
    if button_a.was_pressed():
        radio.send('starting')
        forward()
        pressed = True
        start = running_time()
    try:
        message = radio.receive()
    except ValueError:
        radio.receive_bytes()
    if pressed:
        #forward()
        if pin1.read_analog() < 20 or pin2.read_analog() < 20:
            radio.send("white")
            display.show(Image.SAD, delay=500, wait=False, clear=True)
            reverse()
            sleep(1000)
            stop()
        if button_b.was_pressed():
            end = running_time()
            stop()
            pressed = False
            time = float("{0:.2f}".format((end-start)/1000))
            display.scroll(str(time) + "s")
        elif message == "left":
            pwm_left()
            #print(message)
            #sleep(100)
        elif message == "right":
            pwm_right()
            #sleep(10)