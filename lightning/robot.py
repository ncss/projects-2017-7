from microbit import *

#Import radio as r to increase typing speed
import radio as r
from radio import receive as recv

#Shows if the battery for the robot is working
display.show(Image.HAPPY)

#Enables Radio Interface
r.on()

#Configures channel for communication to 12
r.config(channel=12)

#Stops interferance from other teams with key
key = "lightning"

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


#Main loop for recieveing data
while True:
	#Stores radio messages into variable mess
	mess = recv()
	
	#If mess contains a variable deal with it
	if mess:
		
		#Handle different messages
		if str(mess) == key + "f":
			forward()
		elif str(mess) == key + "r":
			reverse()
		elif str(mess) == key + "s":
			stop()



#### End Of Project ####
