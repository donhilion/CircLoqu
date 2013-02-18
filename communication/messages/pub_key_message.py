from communication.messages.message import Message, CURRENT_MESSAGE_VERSION

__author__ = 'Donhilion'

class PubKeyMessage(Message):

    def __init__(self, owner='UKNOWN', key='NONE'):
        Message.__init__(self, version=CURRENT_MESSAGE_VERSION, type='pubKey')
        self.owner = owner
        self.key = key

    def serialize(self, values=None):
        if values is None:
            values = {}
        values['owner'] = self.owner
        values['key'] = self.key
        Message.serialize(self, values)

    def parse(self, string):
        values = Message.parse(self, string)
        self.owner = values['owner']
        self.key = values['key']
        return values
