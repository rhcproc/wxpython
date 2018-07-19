
import wx
from six import print_

class iFrame(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)
        self.Bind(wx.EVT_SIZE, self.onSize)
        wx.CallAfter(self.after, 1, 2, 3)
        
    def after(self, a, b, c):
        print_('Called via wx.CallAfter : ', a, b, c)

    def onSize(self, evt):
        print_(repr(evt.Size))
        evt.Skip()

class iApp(wx.App):
    def OnInit(self):
        frm = iFrame(None, title="Hello, WxPython", size=(480,360))
        frm.Show()
        return True
    
    def OnExit(self):
        print_('OnExit')
        return 0

if __name__ == '__main__':
    app = iApp()
    app.MainLoop()
