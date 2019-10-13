#!/usr/bin/env python3

import paho.mqtt.client

class MQTT:
    def __init__(self, config):
        self.config = config

        self.client = paho.mqtt.client.Client()
        self.client.enable_logger()

        self.client.connect(host=config['server'],
            port=config.get('port', 1883),
            keepalive=60)
