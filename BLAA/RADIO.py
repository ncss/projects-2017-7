from microbit import *
import radio              
radio.on()
while True:
  if crouch == 1:
    radio.send("crouch")
  if slide == 1:
    radio.send("slide")
  if jump == 1:
    radio.send("jump")
  if stand == 1:
    radio.send("stand")
    
from microbit import *
import radio

radio.on()
while True:
  score = 0
  message = radio.receive()
  if message == "crouch":
      sleep(10)
      score = score + 1
      sleep(10)

  if message == "slide":
      sleep(10)
      score = score + 1
      sleep(10)

  if message == "jump":
      sleep(10)
      score = score + 1
      sleep(10)

  if message == "stand":
      sleep(10)   