__author__ = 'Donhilion'

class State(object):

    def __init__(self):
        pass

    def incoming_message(self, message_string):
        return self

    def do(self):
        return self
