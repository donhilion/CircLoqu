__author__ = 'Donhilion'

class CommunicationStack(object):
    """
    A communication stack for processing messages.
    """

    def __init__(self):
        """
        Generates a new instance of this class.
        """
        self.layers = []

    def add(self, layer):
        """
        Adds the given layer to the communication stack.

        :param layer: The layer to add.
        """
        self.layers.append(layer)

    def remove(self):
        """
        Removes the last layer of this communication stack.
        """
        self.layers.pop()

    def process_msg(self, msg):
        """
        Processes the given message through all layers.
        :param msg: The message to process.
        """
        for layer in self.layers:
            msg = layer.process(msg)
