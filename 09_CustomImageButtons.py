import wx

class iFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'App Tester', size=(300,200))
        panel = wx.Panel(self)

        pic = wx.Bitmap('test.png')
        self.button = wx.BitmapButton(panel, -1, pic, pos=(10,10))
        self.button.SetDefault()

    def doMe(self, event):
        self.Destory()

if __name__ == '__main__':
    app = wx.App(False)
    frame = iFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
