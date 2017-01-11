#Project: right handed arm wrestle
from microbit import *
import music
import radio
from math import degrees, acos


radio.on()
radio.config(channel=12, data_rate=radio.RATE_250KBIT)
key = 'l'
     
def yield_angle():

    pre_values = []
    current_angle = 0
    while True:
        
        # Get the acceleration from the accelerometer
        z = accelerometer.get_z()
        
        # Perform a moving average to smooth the measurements
        if len(pre_values) > 50:
            pre_values.pop(0)
        pre_values.append(z)
        z = sum(pre_values) / len(pre_values)
        
        # Convert the acceleration into an angle
        theta = acos((z-29.86)/1022.4)
        theta_deg = degrees(theta) - 90
        
        # Replace the angle if we got a measurement and it was in range
        if theta_deg != 'nan' and -1 < (z-29.86)/1022.4 < 1:
            current_angle = theta_deg
       
        # Return the last known correct angle
        yield current_angle


angle = yield_angle()
while True:
    current_angle = next(angle)
    print(current_angle)
    radio.send(key + str(current_angle))
        

