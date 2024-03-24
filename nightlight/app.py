import time


from counterfit_connection import CounterFitConnection
from counterfit_shims_grove.grove_light_sensor_v1_2 import GroveLightSensor
from counterfit_shims_grove.grove_led import GroveLed

CounterFitConnection.init('127.0.0.1', 5001)
sharedkey = b'Sf11SX7KTZg7UFSB'
iv_in_bytes = b'Q1nulqHWhajpiKDe'
# Try changing 1231 to 1232, pops error for invalid sharedkey


light_sensor = GroveLightSensor(1, sharedkey, iv_in_bytes)
led = GroveLed(2)

while True:
    sensor_value = light_sensor.light
    print(f'Light sensor reading: {sensor_value}')

    if sensor_value > 200:
        print('Turning LED off')
        led.off()
    else:
        print('Turning LED on')
        led.on()

    time.sleep(2)