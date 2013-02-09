from tkinter import Tk, Frame, N, W, E, S, Text, Button
from common.constants import application_name

__author__ = 'Donhilion'

class Window(object):

    def __init__(self):
        self.tk = Tk()
        self.tk.title(application_name)

        self.frame = Frame(self.tk)
        self.frame.grid(column=0, row=0, sticky=(N, W, E, S))

        self.log = Text(self.frame)
        self.log.grid(column=0, row=0)

        self.test_button = Button(self.frame, text='Test')
        self.test_button.grid(column=0, row=1)

    def run(self):
        self.tk.mainloop()

window = Window()
window.run()