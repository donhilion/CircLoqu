from communication.messages.message import Message, CURRENT_MESSAGE_VERSION

__author__ = 'Donhilion'

class GetPubKeyMessage(Message):

    def __init__(self, owner='server'):
        Message.__init__(self, version=CURRENT_MESSAGE_VERSION, type='getPubKey')
        self.owner = owner

    def serialize(self, values=None):
        if values is None:
            values = {}
        values['owner'] = self.owner
        Message.serialize(self, values)

    def parse(self, string):
        values = Message.parse(self, string)
        self.owner = values['owner']
        return values
