from microbit import *
import radio              
radio.on()
while True:
  if crouch == 1:
    radio.send("crouch")
  if crouch == 1:
    radio.send("slide")
  if crouch == 1:
    radio.send("jump")
  if crouch == 1:
    radio.send("stand")