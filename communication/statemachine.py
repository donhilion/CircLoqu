__author__ = 'Donhilion'

class StateMachine(object):

    def __init__(self):
        self.current_state = None

    def incoming_message(self, message):
        if self.current_state is not None:
            self.current_state = self.current_state.incomming_message(message)
