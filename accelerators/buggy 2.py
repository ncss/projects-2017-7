from microbit import *
import radio

CHANNEL = 95

radio.on()
radio.config(channel = CHANNEL)

PLAYER_NAME_1 = "Player 1"
PLAYER_NAME_2 = "Player 2"

PLAYER_NAME = PLAYER_NAME_2

player1_ready = False
player2_ready = False

start = 0
running = False

def forward():
    pin0.write_digital(1)
    pin16.write_digital(0)
    pin12.write_digital(0)
    pin8.write_digital(1)
        
def stop():
    pin0.write_digital(0)
    pin16.write_digital(0)
    pin12.write_digital(0)
    pin8.write_digital(0)

while True:
    
    message = radio.receive()
    if message:
        
        if message.startswith("ready "):
            s = message[len("ready "):]
            if s == PLAYER_NAME_1:
                player1_ready = True
            elif s == PLAYER_NAME_2:
                player2_ready = True
            
        elif message.startswith("forward "):
            #detecting when a player does a situp
            
            s = message[len("forward "):]
            if s == PLAYER_NAME:
                
                forward()
                sleep(500)
                stop()
        
        elif message.startswith("finish "):
            #somebody has won
            
            t = int(msg[len("finish "):])
            arr = t.split(" ")
            if arr[0] == PLAYER_NAME:
                #the current buggy has won
                display.scroll("You won! You took " + str(arr[1]) + " seconds.")
            else:
                #the other buggy won
                display.scroll("You lost! You took " + str(arr[1]) + " seconds. " + arr[0] + " won in " + str(arr[1]) + " seconds.")
                
            #either way, stop the buggies
            running = False
    
    #only when both players are ready, then the competition starts
    if player1_ready and player2_ready:
        sleep(100)
        radio.send("ready both")
        sleep(3000)
        start = running_time()
        running = True
        
    print(str(player1_ready), str(player2_ready))
    
    #if the game has not yet started, or has finished, do not detect crossing the finish line
    if not running:
        continue
        
        
    #crossing finishing line
    if pin1.read_analog() < 10 or pin2.read_analog() < 10:        
        time = running_time() - start
        radio.send("finish " + PLAYER_NAME + " " + str(time))
        display.scroll("You won! You took " + str(time) + " seconds", wait = True)
        running = False
            
    #if button_b.was_pressed():
    #    win = False

