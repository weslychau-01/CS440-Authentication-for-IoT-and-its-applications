import time

from counterfit_connection import CounterFitConnection
from counterfit_shims_grove.grove_light_sensor_v1_2 import GroveLightSensor
from counterfit_shims_grove.grove_led import GroveLed

# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes

try:
    CounterFitConnection.init('127.0.0.1', 5050)
    print("connection passed")
    
except: 
    print("Authentication failed, wrong plaintext")

file = open("credentials.txt", "r")
plaintext = str(file.read())
# print(plaintext)
#IoT light sensor assigned a token
# light_sensor = GroveLightSensor(1, plaintext)

#let's say we have another IoT device with wrong shared key, at pin 4
brute_force_token = "password"
fake_light_sensor = GroveLightSensor(4, brute_force_token)

#led indicator to simulate correct authentication
led = GroveLed(2) 

#authentication led on pin 3
authentication_led = GroveLed(3)

if fake_light_sensor.token != plaintext:
    authentication_led.on()
    print("authentication error!")