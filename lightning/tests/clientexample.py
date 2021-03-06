from microbit import *

#import radio module
import radio

#enable radio interface
radio.on()


#Set up radio channel
radio.config(channel=12, data_rate=radio.RATE_250KBIT)

#Key for messages
key = "l"


#Permanent loop
while True:
	#Both buttons = Stop, A = forward, B = reverse
	if button_a.is_pressed() and button_b.is_pressed():
		radio.send(key + "s")
	elif button_a.was_pressed():
		radio.send(key + "f")
	elif button_b.was_pressed():
		radio.send(key + "r")
