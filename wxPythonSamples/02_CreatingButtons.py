
import wx

class iFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'App Tester', size=(300,200))
        panel = wx.Panel(self)
        
        button_start = wx.Button(panel, label="start", pos=(30,10), size=(60,60))
        self.Bind(wx.EVT_BUTTON, self.startbutton, button_start)
        button_exit = wx.Button(panel, label="exit", pos=(130,10), size=(60,60))
        self.Bind(wx.EVT_BUTTON, self.closebutton, button_exit)


        self.itext = wx.StaticText(panel, -1, "", (10,80), (260,-1), wx.ALIGN_CENTER)
        
        #self.Bind(wx.EVT_CLOSE, self.closewindow)

    def closebutton(self, event):
        self.Close(True)

    def startbutton(self, event):
        self.itext.SetLabel("Hello")

    def closewindow(self, event):
        self.Destroy()

if __name__ == '__main__':
    app = wx.App(False)
    frame = iFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
