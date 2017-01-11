from microbit import *

#Import radio as r to increase typing speed
import radio as r
from radio import receive as recv

#Shows if the battery for the robot is working
display.show(Image.HAPPY)

#Enables Radio Interface
r.on()

#Configures channel for communication to 12
r.config(queue=5, channel=12, data_rate=r.RATE_250KBIT)

#Stops interferance from other teams with key
key = "l"

#Set pins to analog
pin0.set_analog_period(20)
pin16.set_analog_period(20)
pin12.set_analog_period(20)
pin8.set_analog_period(20)

#Extra variable declarations
direction = 0
#Functions for robot movement

def move(speed, direction):
	if direction < 0:
		reverse(speed)
	elif direction > 0:
		forward(speed)

def reverse(speed):
	pin0.write_analog(speed)
	pin16.write_analog(0)
	pin12.write_analog(0)
	pin8.write_analog(speed)

def forward(speed):
	pin0.write_analog(0)
	pin16.write_analog(speed)
	pin12.write_analog(speed)
	pin8.write_analog(0)

def stop():
	pin0.write_analog(0)
	pin16.write_analog(0)
	pin12.write_analog(0)
	pin8.write_analog(0)

def turn_left():
	pin0.write_analog(1)
	pin16.write_analog(0)
	pin12.write_analog(1)
	pin8.write_analog(0)

def turn_right():
	pin0.write_analog(0)
	pin16.write_analog(1)
	pin12.write_analog(0)
	pin8.write_analog(1)

def calculate(angle):
	speed = 0
	direction = 0
	#set the direction and speed based on size of angle
	if angle >= -10 and angle <= 10:
		pass
	elif angle < -10 and angle >= -30:
		direction = -1
		speed = 340
	elif angle > 10 and angle <= 30:
		direction = 1
		speed = 340
	elif angle < -30 and angle >= -50:
		speed = 680
 	elif angle > 30 and angle <= 50:
		speed = 680
	elif angle < -50 and angle >= -70:
		speed = 1023
	elif angle > 50 and angle <= 70:
		speed = 1023

	#return speed, direction
	return speed, direction


#Saves memory
#reverse_on = False
#forward_on = False
#stop_on    = False



#New state machine based loop

state = 1
current_speed = 0

while True:
	#print('ERROR: THIS CODE IS DEFINITlY BROKEN')
    try:
        mess = recv()
	#If it cannot convert to string, it dumps the value and moves on
    except ValueError:
        r.receive_bytes()

    if mess:
        try:
            current_speed, direction = calculate(float(mess[1:]))
        except TypeError:
            mess = "0"

	inter = pin2.read_analog()

	move(current_speed, direction)

	if state == 1:
		if inter < 500:
			state = 1
		elif inter > 500 and current_speed == 1:
			state += 1
	elif state == 2:
		state = 2
	elif state == 3 or state == 0:
		stop()








"""
#Main loop for recieveing data
while True:
	#Attempts to convert recieve to string and store in mess
	try:
		mess = recv()
	#If it cannot convert to string, it dumps the value and moves on
	except ValueError:
		r.receive_bytes()

	#If mess contains a variable deal with it
	if mess:

		#Handle different messages
		if mess == key + "f" and not forward_on:
			forward()
			forward_on = True
			stop_on = False
			reverse_on = False
		elif mess == key + "r" and not reverse_on:
			reverse()
			reverse_on = True
			forward_on = False
			stop_on = False
		elif mess == key + "s" and not stop_on:
			stop()
			stop_on = True
			reverse_on = False
			forward_on = False
"""

#### End Of Project ####
