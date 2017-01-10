from microbit import *
import music

#Project: right handed arm wrestle


pre_values = []

while True:
    z = accelerometer.get_z()
    if len(pre_values) > 50:
        pre_values.pop(0)
    pre_values.append(z)
    z = sum(pre_values) / len(pre_values)

    if z < -900:
        display.show(Image.HAPPY, wait=True)
    elif z > 950:
        display.show(Image.SAD, wait=True)
    else:
        display.clear()


'''
Alternative Codes without Averages

    if z < -900:
        z_time = 0
        while z < -900:
            z = accelerometer.get_z()
            print(z)
            z_time += 20
            sleep(200)
            if z_time > 500:
                #music.play(music.BA_DING, wait = True)
                display.show(Image.HAPPY)
    elif z > 950:
        #music.play(music.POWER_DOWN, wait = True)
        display.show(Image.SAD, wait = True)
    else:
        display.clear()


while True:

    a = accelerometer.get_values()
    print(a)
    sleep(20)
'''
