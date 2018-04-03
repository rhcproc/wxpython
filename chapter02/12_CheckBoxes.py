import wx

class iFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'App Tester', size=(300,200))
        panel = wx.Panel(self)

        wx.CheckBox(panel, -1, "Apples", (20,20), (160, -1))
        wx.CheckBox(panel, -1, "Tuna", (20,40), (160, -1))
        wx.CheckBox(panel, -1, "Roast Beef", (20,60), (160, -1))

if __name__ == "__main__":
    app = wx.App()
    frame = iFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
