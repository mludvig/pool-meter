#!/usr/bin/env python3

import socket
import paho.mqtt.client
import paho.mqtt.publish

class MQTT:
    def __init__(self, config):
        self.config = config

        self.client = paho.mqtt.client.Client()
        self.client.enable_logger()

        self.server = config['server']
        self.port = config.get('port', 1883)

    def publish(self, topic, data):
        try:
            paho.mqtt.publish.multiple(
                [
                    (topic, data, 1, True),
                ],
                hostname=self.server,
                port=self.port)
        except socket.error as e:
            print(f"ERROR publishing to {topic}: {e}")
