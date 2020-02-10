import wx

class iFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'App Tester', size=(300,200))
        panel = wx.Panel(self)

        test = wx.TextEntryDialog(None, "What's your name?", "Title", "Enter Name")
        if test.ShowModal() == wx.ID_OK:
            name = test.GetValue()
        
        wx.StaticText(panel, -1, "My name is {}".format(name), (10,10))

if __name__ == '__main__':
    app = wx.App(False)
    frame = iFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
