import wx

class iFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'App Tester', size=(300,200))
        panel = wx.Panel()

        mylist = ['beef', 'tuna', 'cocnuts', 'more beef']
        #cunt = wx.ListBox(panel, -1, pos=wx.Point(20,20), size=wx.Size(80,60), mylist, wx.LB_SINGLE)
        cunt = wx.ListBox(panel, -1, (20,20), (80,60),choices=mylist, style= wx.LB_SINGLE)
        cunt.SetSelection(3)

if __name__ == '__main__':
    app = wx.App(False)
    frame = iFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
