import wx

if __name__ == '__main__':
    app = wx.App()
    names = ['A','B','C','D','E']
    modal = wx.SingleChoiceDialog(None, 'Whats your number', 'App Tester', names)
    if modal.ShowModal() == wx.ID_OK:
        print ("Your name is {}".format(modal.GetStringSelection()))
    modal.Destory()
