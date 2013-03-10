from communication.messages.get_pub_key_message import GetPubKeyMessage
from communication.messages.message import Message
from communication.state import State

__author__ = 'Donhilion'

class WaitingForMessageState(State):

    def __init__(self, get_pub_key=None):
        self.get_pub_key = get_pub_key

    def set_get_pub_key(self, get_pub_key):
        self.get_pub_key = get_pub_key

    def incoming_message(self, message_string):
        message = Message()
        message.parse(message_string)
        if message.type == 'getPubKey':
            if self.get_pub_key is None:
                print('Get pub key state not specified in waiting for message state.')
                return self
            get_pub_key_message = GetPubKeyMessage()
            get_pub_key_message.parse(message_string)
            self.get_pub_key.set_message(get_pub_key_message)
            return self.get_pub_key.do()
        return self
