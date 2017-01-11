from microbit import *
import radio

def player_1_score():
    pin0.write_analog(throttle_1)
    pin16.write_digital(0)
    pin12.write_digital(0)
    pin8.write_analog(throttle_1)
        
def player_2_score():
    pin0.write_digital(0)
    pin16.write_analog(throttle_2)
    pin12.write_analog(throttle_2)
    pin8.write_digital(0)

def stop():
    pin0.write_digital(0)
    pin16.write_digital(0)
    pin12.write_digital(0)
    pin8.write_digital(0)

radio.on()
radio.config(channel=65, address=0x6e637373)
throttle_1 = 1
throttle_2 = 1
while True:
    message = radio.receive()
    if message == "Robot1":
        print(message)
        if throttle_1 > 0:
            throttle_1 += 102
            player_1_score()
            if throttle_1 > 1020:
                throttle_1 = 1020
        if throttle_1 == 0:
            throttle_2 -= 102
            player_2_score()
            if throttle_2 < 0:
                throttle_2 = 0

    if message == "Robot2":
        print(message)
        if throttle_2 > 0:
            throttle_2 += 102
            player_2_score()
            if throttle_2 > 1020:
                throttle_2 = 1020
        if throttle_2 == 0:
            throttle_1 -= 102
            player_1_score()
            if throttle_1 < 0:
                throttle_1 = 0