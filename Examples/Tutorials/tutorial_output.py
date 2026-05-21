"""Output tutorial - demonstrates GOutput usage (redirected print).
"""

try:
    import GnuChanGUI as gc
except Exception:
    raise

class OutputTutorial(gc.GnuChanGUI):
    def __init__(self):
        super().__init__(Title='Output Tutorial', Size=(520,320), finalize=True)

        self.Layout = [
            [self.GText(SetText='Output demo', TFont='Sans,14', xStretch=True)],
            [self.GOutput(SetValue='out', Size=(60,10), xStretch=True, yStretch=True)],
            [self.GButton(Text='Print', SetValue='print')]
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(self.Update)

    def Update(self):
        if not self.GetValues:
            return
        if self.GetEvent == 'print':
            print('This line goes to GOutput widget')

if __name__ == '__main__':
    OutputTutorial()
