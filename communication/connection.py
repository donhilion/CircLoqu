from communication.communication_stack import CommunicationStack
from communication.statemachine import StateMachine

__author__ = 'Donhilion'

class Connection(object):

    def __init__(self):
        self.communication_stack = CommunicationStack()
        self.state_machine = StateMachine()
