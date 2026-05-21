"""Message tutorial - demonstrates GMessage popup usage.
"""

try:
    import GnuChanGUI as gc
except Exception:
    raise

class MessageTutorial(gc.GnuChanGUI):
    def __init__(self):
        super().__init__(Title='Message Tutorial', Size=(420,160), finalize=True)

        self.Layout = [
            [self.GText(SetText='Message demo', xStretch=True)],
            [self.GButton(Text='Show Message', SetValue='show')]
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(self.Update)

    def Update(self):
        if self.GetEvent == 'show':
            gc.GMessage(WindowTitle='Hello', WindowText='This is a GMessage example')

if __name__ == '__main__':
    MessageTutorial()
