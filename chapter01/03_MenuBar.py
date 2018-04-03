
import wx

class iFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'App Tester', size=(300,200))
        panel = wx.Panel(self)

        status = self.CreateStatusBar()
        menubar = wx.MenuBar()
        first = wx.Menu()
        second = wx.Menu()
        first.Append(wx.NewId(), "New Window", "This is a new window")
        first.Append(wx.NewId(), "Open...", "This will open a new window")
        menubar.Append(first, "File")
        menubar.Append(second, "Edit")
        self.SetMenuBar(menubar)

if __name__ == '__main__':
    app = wx.App(False)
    frame = iFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()