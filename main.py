#!/usr/bin/env python3

import time
import logging
import configparser

from atlas import AtlasPH
from temperature import Temperature
from mqtt import MQTT

config_ini = "config.ini"

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read(config_ini)

    mqtt = MQTT(config['mqtt'])
    temp_sensors = Temperature(config['temperature'])

    while True:
        temps = temp_sensors.read_all()
        print(temps)
        time.sleep(5)
