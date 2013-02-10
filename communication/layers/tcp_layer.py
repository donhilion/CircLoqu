__author__ = 'Donhilion'

class TcpLayer(object):

    def __init__(self, socket):
        self.socket = socket

    def process(self, msg):
        self.socket.send(msg)
