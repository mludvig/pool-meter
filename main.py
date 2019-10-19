#!/usr/bin/env python3

import time
import json
import logging
import configparser
from datetime import datetime

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
        temps['_timestamp'] = str(datetime.now())
        print(temps)
        mqtt.publish(config['temperature']['mqtt_topic'], json.dumps(temps))
        time.sleep(60)
