"""Titlebar tutorial - demonstrates GTitleBar usage (custom titlebar element).
"""

try:
    import GnuChanGUI as gc
except Exception:
    raise

class TitlebarTutorial(gc.GnuChanGUI):
    def __init__(self):
        super().__init__(Title='Titlebar Tutorial', Size=(480,160), finalize=True)

        tb = self.GTitleBar(title='Custom Title', icon=None, font='Sans,12')
        self.Layout = [
            [tb],
            [self.GText(SetText='Custom titlebar demo', xStretch=True)],
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(self.Update)

    def Update(self):
        if self.GetEvent == '__TIMEOUT__':
            return

if __name__ == '__main__':
    TitlebarTutorial()
