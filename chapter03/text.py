#https://wiki.wxpython.org/StdouttoTextCtrl

import wx
import sys, time

class LogWindow(wx.TextCtrl):
    def __init__ (self):
        frame = wx.Frame(None,-1, "Standard out", size=(200,200))
        frame.Show(True)

        self.parent = frame

        wx.TextCtrl.__init__(self,self.parent,size=self.parent.GetClientSize(), style=wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)

        sys.stdout = self

        print ("this is in Stdout!!!!")
        for i in range(10):
            print (i)
            wx.Yield()
            time.sleep(0.21)

        print ("All done!")

class MainApp(wx.App):
    def OnInit(self):
        log = LogWindow()
        log.parent.Show(True)
        self.SetTopWindow(log.parent)

        Alog = LogWindow()
        Alog.parent.Show(True)
        self.SetTopWindow(Alog.parent)
        return True

if __name__ == '__main__':
    app = MainApp(0)
    app.MainLoop()
    sys.stdout = sys.__stdout__
