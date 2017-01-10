#Project: right handed arm wrestle
from microbit import *
import music
import radio
from math import degrees, acos


radio.on()
radio.config(channel=12, data_rate=radio.RATE_250KBIT)
key = 'l'

#pre_values = []
while True:
    z = accelerometer.get_z()
    theta = acos((z-29.86)/1022.4)

    theta_deg = degrees(theta)
    print(theta, theta_deg, z)

'''
    if len(pre_values) > 50:
        pre_values.pop(0)
    pre_values.append(z)
    z = sum(pre_values) / len(pre_values)
'''

    if str(theta_deg).isnumeric():
        radio.send(key + theta_deg)
    else:
        radio.send(key + '180')

'''
    if z < -900:
        radio.send(key + 'f')
    elif z > 950:
        radio.send(key + 'r')
    else:
        radio.send(key + 's')
    sleep(20)
'''

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
