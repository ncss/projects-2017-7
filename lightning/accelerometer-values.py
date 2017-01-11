#Project: right handed arm wrestle
from microbit import *
import music
import radio
from math import degrees, acos


radio.on()
radio.config(channel=12, data_rate=radio.RATE_250KBIT)
key = 'l'

pre_values = []
while True:
    z = accelerometer.get_z()
    if len(pre_values) > 50:
        pre_values.pop(0)
    pre_values.append(z)
    z = sum(pre_values) / len(pre_values)

    if -1 < (z-29.86) / 1022.4 < 1:
        theta = acos((z-29.86)/1022.4)
        theta_deg = degrees(theta) - 90
        print(theta, theta_deg, z)
        radio.send(key + str(theta_deg))
