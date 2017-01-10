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
start = 0
display.clear()
pressed = False


while True:
    if button_a.was_pressed():
        pressed = True
        start = running_time()
    message = radio.receive()
    if pressed:
        forward()
        sleep(400)
        if pin1.read_analog() < 20 or pin2.read_analog() < 20:
            stop()
            pressed = False
            end = running_time()
            radio.send("stop")
            display.show(Image.SAD)
            sleep(2000)
            display.clear()
            display.scroll(str(end-start))
        if button_b.was_pressed():
            stop()
            pressed = False
        elif message == "left":
            left()
            sleep(100)
            stop()
            forward()
        elif message == "right":
            right()
            sleep(100)
            stop()
            forward()