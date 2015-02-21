__author__ = 'KatarzynaAleksandra'
import wx

class Play(wx.Frame):

    def __init__(self, *args, **kw):
        super(Play, self).__init__(*args, **kw)
        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)

        menuBar = wx.MenuBar()
        menu = wx.Menu()
        m_exit = menu.Append(wx.ID_EXIT, "E&xit\tAlt-X", "Close window and exit program.")
        self.Bind(wx.EVT_MENU, self.OnClose, m_exit)
        menuBar.Append(menu, "&File")
        menu = wx.Menu()
        m_about = menu.Append(wx.ID_ABOUT, "&About", "Information about this program")
        self.Bind(wx.EVT_MENU, self.OnAbout, m_about)
        menuBar.Append(menu, "&Help")

        self.SetMenuBar(menuBar)

        first_player = ['','Stone', 'Peper', 'Scissors']
        second_player = ['','Stone', 'Peper', 'Scissors']

        self.cb1 = wx.ComboBox(panel, value=first_player[0],  choices=first_player)
        self.cb2 = wx.ComboBox(panel, value=second_player[0], choices=second_player)


        self.st1 = wx.StaticText(panel, label=' ', pos=wx.Point(210, 10))
        self.st2 = wx.StaticText(panel, label=' ', pos=wx.Point(210, 10))
        self.result = wx.StaticText(panel, label=' ', pos=wx.Point(210, 10))

        self.cb1.Bind(wx.EVT_COMBOBOX, self.OnSelect)
        self.cb2.Bind(wx.EVT_COMBOBOX, self.OnSelect)


        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.cb1, flag=wx.ALL, border=5)
        sizer.Add(self.cb2, flag=wx.ALL, border=5)

        sizer.Add(self.st1, flag=wx.ALL, border=5)
        sizer.Add(self.st2, flag=wx.ALL, border=5)
        sizer.Add(self.result, flag=wx.ALL, border=5)

        panel.SetSizer(sizer)

        self.SetSize((630, 330))
        self.SetTitle('Play: stone, peper, scissors')
        self.Centre()
        self.Show(True)

    def OnSelect(self, event):

        unit1 = self.cb1.GetValue()
        unit2 = self.cb2.GetValue()
        self.st1.SetLabel("The first player chosen " +unit1)
        self.st2.SetLabel("The second player chosen " +unit2)


        if unit1 == unit2:
            self.result.SetLabel("Result: \n  remis  " )
        elif unit1 == 'Stone' and unit2 == 'Peper' or unit2 == 'Stone' and unit1 == 'Peper' :
            self.result.SetLabel('Result: \n Won Peper')
        elif unit1 == 'Stone' and unit2 == 'Scissors' or unit2 == 'Stone' and unit1 == 'Scissors':
            self.result.SetLabel('Result: \n Won Stone')
        elif unit1 == 'Scissors' and unit2 == 'Papier' or unit2 == 'Scissors' and unit1 == 'Peper':
            self.result.SetLabel('Result: \n Won Scissors')

    def OnClose(self, event):
        dlg = wx.MessageDialog(self,
            "Do you really want to close this application?",
            "Confirm Exit", wx.OK|wx.CANCEL|wx.ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()
        if result == wx.ID_OK:
            self.Destroy()

    def OnAbout(self, event):
        dlg = wx.MessageDialog(self,
            "Rock-paper-scissors - game for two or more people. \n"
            "Scissors is stronger than paper   \n"
            "Stone is stronger than the scissors  \n"
            "Paper is stronger than stone " )
        result = dlg.ShowModal()
        dlg.Destroy()

def main():

    ex = wx.App()
    Play(None)
    ex.MainLoop()

if __name__ == '__main__':
    main()