from microbit import *
radio.config(channel=58)

while True:
    # The button is context free, and can be configured with the a and b buttons.
    if button_a.is_pressed():
        button_type = 'left'
        display.show(ARROW_W)
    if button_b.is_pressed():
        button_type = 'right'
        display.show(ARROW_E)
    if pin8.read_digital() == 1:
        radio.send(button_type)
    sleep(5)