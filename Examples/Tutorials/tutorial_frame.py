"""Frame tutorial - demonstrates nested frames.
"""

try:
    import GnuChanGUI as gc
except Exception:
    raise

class FrameTutorial(gc.GnuChanGUI):
    def __init__(self):
        super().__init__(Title='Frame Tutorial', Size=(520,320), finalize=True)

        inside = [[self.GText(SetText='Left frame', xStretch=True)], [self.GButton(Text='L-Button', SetValue='lbtn')]]
        inside2 = [[self.GText(SetText='Right frame', xStretch=True)], [self.GButton(Text='R-Button', SetValue='rbtn')]]

        self.Layout = [
            [self.GText(SetText='Frame demo', TFont='Sans,14', xStretch=True)],
            [self.GFrame(InsideWindowLayout=inside, SetValue='f1', xStretch=True), self.GFrame(InsideWindowLayout=inside2, SetValue='f2', xStretch=True)],
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(self.Update)

    def Update(self):
        if not self.GetValues:
            return
        if self.GetEvent == 'lbtn':
            gc.GMessage(WindowTitle='Frame', WindowText='Left button clicked')
        if self.GetEvent == 'rbtn':
            gc.GMessage(WindowTitle='Frame', WindowText='Right button clicked')

if __name__ == '__main__':
    FrameTutorial()
