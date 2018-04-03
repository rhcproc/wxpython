
import wx

class iFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'App Tester', size=(300,200))
        panel = wx.Panel(self)

        box = wx.MessageDialog(None, 'Do I have some nuts?', 'Selector', wx.YES_NO)
        answer = box.ShowModal()
        print (answer)
        box.Destroy()

if __name__ == '__main__':
    app = wx.App(False)
    frame = iFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
