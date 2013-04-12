import wx

__author__ = 'Donhilion'

class ConnectWindow(object):
    def __init__(self, parent):
        self.frame = wx.Frame(parent, -1, "Connect")

    def show(self):
        self.frame.Show()
