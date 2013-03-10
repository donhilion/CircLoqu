from communication.state import State

__author__ = 'Donhilion'

class GetPubKeyState(State):

    def __init__(self, message=None, waiting_for_message=None):
        self.message = message
        self.waiting_for_message = waiting_for_message

    def set_message(self, message):
        self.message = message

    def set_waiting_for_message(self, waiting_for_message):
        self.waiting_for_message = waiting_for_message

    def do(self):
        if self.message is None:
            print('No message specified in get pub key state.')
            # TODO error handling
            return self.waiting_for_message
        owner = self.message.owner
