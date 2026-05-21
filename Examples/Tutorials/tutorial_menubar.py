"""Menu bar tutorial - demonstrates GMenu and GMenuForTheme usage.
"""

try:
    import GnuChanGUI as gc
except Exception:
    raise

class MenuTutorial(gc.GnuChanGUI):
    def __init__(self):
        super().__init__(Title='Menu Tutorial', Size=(520,260), finalize=True)

        defaultFont = 'Sans, 16'
        c = gc.GColors()

        gMenu = [["File", ["New","Open","Exit"]], ["Help", ["About"]]]
        themedMenu = [["Theme", ["Black","Blue","Green","Red"]]]

        self.Layout = [
            [self.GMenu(WinMENU_List=gMenu)],
            [self.GMenuForTheme(WinMENU_List=themedMenu, TFont=defaultFont, TColor=c.white, BColor=c.blue1)],
            [self.GText(SetText='Menu demo - use menu items', xStretch=True)],
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(self.Update)

    def Update(self):
        if not self.GetValues:
            return
        if self.GetEvent == 'Exit':
            self.GetWindow.close()
        if self.GetEvent == 'About':
            gc.GMessage(WindowTitle='About', WindowText='GnuChanGUI Menu example')
        if self.GetEvent in ('Black', 'Blue', 'Green', 'Red'):
            gc.Themecolors().__getattribute__(self.GetEvent)
            gc.GMessage(WindowTitle='Theme', WindowText=f'Set theme: {self.GetEvent}')

if __name__ == '__main__':
    MenuTutorial()
