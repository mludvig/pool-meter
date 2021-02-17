#!/usr/bin/env python3

import socket
import paho.mqtt.client
import paho.mqtt.publish

class MQTT:
    def __init__(self, config):
        self.config = config

        self.server = config['server']
        self.port = config.get('port', 1883)

        self.client = paho.mqtt.client.Client(config.get('client_name', 'atlas-service'))
        self.client.enable_logger()
        self.client.connect(self.server, port=self.port)
        self.client.loop_start()

    def publish(self, topic, data):
        self.client.publish(topic, data, qos=1, retain=True)
