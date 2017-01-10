from microbit import *
import radio
radio.on()
radio.config(channel=58)
button_type = 'left'
under_time = True
initial = True
right_pressed = False


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
    if under_time:
        if pin8.read_digital() == 1:
            radio.send(button_type)
            display.show(Image.SQUARE_SMALL)
            if initial:
                start_time = running_time()
                initial = False
            else:
                if running_time() - start_time < 300:
                    continue
                else: under_time = False
            #radio.send("music")
            sleep(50)
        else:
            initial = True
    else:
        sleep(3000)
        under_time = True
        initial = True
    