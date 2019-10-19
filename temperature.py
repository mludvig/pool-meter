#!/usr/bin/env python3

import json
import ow

class Temperature:
    def __init__(self, config):
        # We only support 'owserver' temperature sensors at the moment
        # For example DS18B20 connected directly or over DS2482 I2C-to-1wire bridge
        assert(config['mode'] == 'owserver')
        
        # Load the probe aliases
        aliases = config.get('aliases', '{}')
        self.aliases = json.loads(aliases)

        # Connect to the server and list probes
        ow.init(config['server'])
        self.sensors = ow.Sensor('/').sensorList()
        for sensor in self.sensors:
            print('Address:   ' + sensor.address)
            if sensor.address in self.aliases:
                print('Alias:     ' + self.aliases[sensor.address])
            print('Family:    ' + sensor.family)
            print('ID:        ' + sensor.id)
            print('Type:      ' + sensor.type)
            print('Curr Temp: ' + sensor.temperature)
            print(' ')

    def read_all(self):
        ret = {}
        for sensor in self.sensors:
            if sensor.address in self.aliases:
                sensor_id = self.aliases[sensor.address]
            else:
                sensor_id = sensor.address
            ret[sensor_id] = float(sensor.temperature)
        return ret
