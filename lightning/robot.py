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

#Functions for robot movement

def move(speed, direction):
	if direction < 0:
		reverse(speed)
	elif direction > 0:
		forward(speed)


def reverse(speed):
	pin0.write_digital(1)
	pin16.write_digital(0)
	pin12.write_digital(0)
	pin8.write_digital(1)

def forward(speed):
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

def calculate(angle):

	#Start 80-100 -- Speed shall be zero - direction = 0
	#Phase 1 speed 60-80 100-120 		 - direction = 1 or -1
	#Phase 2 speed 40-60 120-140 		 - less should be postivie - positive should be negetive
	#Phase 3 speed 20-40 140-160
	#Final speed   0 -20 160-180
	

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
	try:
		current_speed, direction = calculate(float(mess))
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
