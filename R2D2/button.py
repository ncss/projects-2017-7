from microbit import *
pin8.read_digital()
pin8.PULL_DOWN

while True:
    if pin8.read_digital() == 1:
        display.show(Image.ANGRY)
    else:
        display.clear()