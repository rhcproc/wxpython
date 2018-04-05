import wx

class iFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'App Tester', size=(300,200))
        panel = wx.Panel(self)

        box = wx.SingleChoiceDialog(None, "What's your favorite food?",
                            "Title", ['Apple', 'Banana', 'Kiwi'])
        if box.ShowModal() == wx.ID_OK:
            answer = box.GetStringSelection()

if __name__ == '__main__':
    app = wx.App(False)
    frame = iFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
