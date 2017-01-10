from microbit import *

display.show(Image.HAPPY)


def reverse():
	pin0.write_digital(1)
	pin16.write_digital(0)
	pin12.write_digital(0)
	pin8.write_digital(1)

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

def turn_left():
	pin0.write_digital(1)
	pin16.write_digital(0)
	pin12.write_digital(1)
	pin8.write_digital(0)

def turn_right():
	pin0.write_digital(0)
	pin16.write_digital(1)
	pin12.write_digital(0)
	pin8.write_digital(1)

forward()
sleep(2000)
stop()
