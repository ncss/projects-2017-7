from microbit import *
import radio
radio.on()
radio.config(channel=58)
button_type = 'left'
while True:
    # The big button is context free, and can be configured with the a and b buttons.
    if button_type == 'left':
        display.show(Image.ARROW_W)
    if button_type == 'right':
        display.show(Image.ARROW_E)
    if button_a.is_pressed():
        button_type = 'left'
    if button_b.is_pressed():
        button_type = 'right'
    if pin8.read_digital() == 1:
        radio.send(button_type)
        display.show(Image.SQUARE_SMALL)
        #radio.send("music")
        #sleep(500)
    