#!/usr/bin/env python3

import ow

class Temperature:
    def __init__(self, config):
        # We only support 'owserver' temperature sensors at the moment
        # For example DS18B20 connected directly or over DS2482 I2C-to-1wire bridge
        assert(config['mode'] == 'owserver')
        
        ow.init(config['server'])
        self.sensors = ow.Sensor('/').sensorList()
        for sensor in self.sensors:
            print('Address: ' + sensor.address)
            print('Family: ' + sensor.family)
            print('ID: ' + sensor.id)
            print('Type: ' + sensor.type)
            print(' ')

    def read(self):
        return self.sensors[0].temperature
