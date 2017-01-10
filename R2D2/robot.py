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
error_count = 0

while True:
    if button_a.was_pressed():
        pressed = True
        start = running_time()
    message = radio.receive()
    if pressed:
        forward()
        if pin1.read_analog() < 20 or pin2.read_analog() < 20:
            radio.send("white")
            display.show(Image.SAD, delay=500, wait=False, clear=True)
            error_count += 1
        if button_b.was_pressed():
            end = running_time()
            stop()
            pressed = False
            time = float("{0:.2f}".format((end-start)/1000))
            score = time + float(error_count)
            display.scroll(str(score))
        elif message == "left":
            left()
            sleep(10)
        elif message == "right":
            right()
            sleep(10)