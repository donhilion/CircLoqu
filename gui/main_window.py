import wx
from common.constants import application_name
from gui.connect_window import ConnectWindow

__author__ = 'Donhilion'

class MainWindow(object):

    def __init__(self):
        self.app = wx.App()

        self.frame = wx.Frame(None, -1, application_name)

        self.menubar = wx.MenuBar()
        self.file_menu = wx.Menu()

        self.connect_entry = self.file_menu.Append(wx.ID_ANY, "Connect")
        self.frame.Bind(wx.EVT_MENU, self.on_connect, self.connect_entry)

        self.quit_entry = self.file_menu.Append(wx.ID_EXIT, "Exit")
        self.frame.Bind(wx.EVT_MENU, self.on_quit, self.quit_entry)

        self.menubar.Append(self.file_menu, "File")
        self.frame.SetMenuBar(self.menubar)

    def on_connect(self, e):
        connect = ConnectWindow(self.frame)
        connect.show()

    def on_quit(self, e):
        self.frame.Close()

    def run(self):
        self.frame.Show()
        self.app.MainLoop()

window = MainWindow()
window.run()