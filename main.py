#!/usr/bin/env python3

import time
import json
import logging
import configparser
from datetime import datetime

from atlas import AtlasPH_I2C
from temperature import Temperature
from mqtt import MQTT

config_ini = "config.ini"

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read(config_ini)

    mqtt = MQTT(config['mqtt'])
    temp_sensors = Temperature(config['temperature'])
    ph_sensor = AtlasPH_I2C(
        address = int(config['ph']['addr'], 0),
        bus = int(config['ph']['bus'], 0)
    )

    while True:
        result = {
            '_timestamp': str(datetime.now())
        }
        result['temperature'] = temp_sensors.read_all()
        result['ph'] = ph_sensor.read_ph()
        print(result)
        mqtt.publish(config['mqtt']['topic'], json.dumps(result))
        time.sleep(60)
