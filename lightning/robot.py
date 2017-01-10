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

#Saves memory
reverse_on = False
forward_on = False
stop_on    = False



#New state machine based loop

while True:
	print('ERROR: THIS CODE IS DEFINITlY BROKEN')










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
