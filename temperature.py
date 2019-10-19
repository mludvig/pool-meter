#!/usr/bin/env python3

import ow

class Temperature:
    def __init__(self, config):
        # We only support 'owserver' temperature sensors at the moment
        # For example DS18B20 connected directly or over DS2482 I2C-to-1wire bridge
        assert(config['mode'] == 'owserver')
        
        ow.init(config['server'])
        self.sensors = ow.Sensor('/').sensorList()
        self.addrs = {}
        for sensor in self.sensors:
            print('Address: ' + sensor.address)
            print('Family:  ' + sensor.family)
            print('ID:      ' + sensor.id)
            print('Type:    ' + sensor.type)
            print('Temper:  ' + sensor.temperature)
            print(' ')
            self.addrs[sensor.address] = sensor

    def read(self, addr):
        return self.addrs[addr].temperature

    def read_all(self):
        ret = {}
        for sensor in self.sensors:
            ret[sensor.address] = float(sensor.temperature)
        return ret
