#!/usr/bin/env python3

import json
import socket
import paho.mqtt.client
import paho.mqtt.publish

class MQTT:
    def __init__(self, config, on_connect=None, on_message=None):
        self.config = config

        self.server = config['server']
        self.port = config.get('port', 1883)

        self.client = paho.mqtt.client.Client(config.get('client_name', 'atlas-service'))
        if on_connect is not None:
            self.client.on_connect = on_connect
        if on_message is not None:
            self.client.on_message = on_message
        self.client.enable_logger()
        self.client.connect_async(self.server, port=self.port)
        self.client.loop_start()

    def publish(self, topic, data):
        if not isinstance(data, (str, bytes)):
            data = json.dumps(data)
        self.client.publish(topic, data, qos=1, retain=True)

    def subscribe(self, topic):
        ret = self.client.subscribe(topic, 1)
