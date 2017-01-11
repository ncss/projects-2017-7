from microbit import *
import radio
radio.on()
radio.config(channel=58)
button_type = 'left'
under_time = True
initial = True

left_arrow = Image(
"00000:"
"01000:"
"11111:"
"01000:"
"00000:"
)

right_arrow = Image(
"00000:"
"00010:"
"11111:"
"00010:"
"00000:"
)

button_time = 0
button_lookup = {}
button_lookup['left'] = left_arrow
button_lookup['right'] = right_arrow
button_type = 'left'

while True:
    # The big button is context free, and can be configured with the a and b buttons.
    if button_a.is_pressed():
        button_type = 'left'
    if button_b.is_pressed():
        button_type = 'right'
    if under_time:
        if pin1.read_digital() == 1:
            button_time = running_time()
            radio.send(button_type)
            display.show(button_lookup[button_type]*9)
            if initial:
                start_time = running_time()
                initial = False
            else:
                if running_time() - start_time < 400:
                    continue
                else: 
                    under_time = False
            #radio.send("music")
            sleep(50)
        else:
            initial = True
    else:
        display.show(button_lookup[button_type] * 4)
        sleep(800)
        under_time = True
        initial = True
        
    if button_time + 100 < running_time():
        display.show(button_lookup[button_type] * 4)
    