__author__ = 'Donhilion'

import json

CURRENT_MESSAGE_VERSION = '0.0.1'

class Message(object):

    def __init__(self, version=CURRENT_MESSAGE_VERSION, type='UNKNOWN'):
        self.version = version
        self.type = type

    def serialize(self, values=None):
        if values is None:
            values = {}
        values['version'] = self.version
        values['type'] = self.type
        return json.dumps(values)

    def parse(self, string):
        values = json.loads(string)
        self.version = values['version']
        self.type = values['type']
        return values