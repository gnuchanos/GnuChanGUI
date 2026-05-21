"""Canvas tutorial - demonstrates drawing on GCanvas.
"""

try:
    import GnuChanGUI as gc
except Exception:
    raise

class CanvasTutorial(gc.GnuChanGUI):
    def __init__(self):
        super().__init__(Title='Canvas Tutorial', Size=(600,400), finalize=True)

        self.Layout = [
            [self.GText(SetText='Canvas demo', TFont='Sans,14', xStretch=True)],
            [self.GCanvas(SetValue='cv', Size=(60,20), xStretch=True, yStretch=True)],
            [self.GButton(Text='Draw', SetValue='draw')]
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(self.Update)

    def Update(self):
        if not self.GetValues:
            return
        if self.GetEvent == 'draw':
            cv = self.GetWindow['cv']
            with cv.BeginScene2D():
                cv.ClearScene2D()
                cv.DrawRectangle('bg', 0, 0, 400, 300, fill='#112233')
                cv.DrawCircle('c', 100, 80, 30, fill='orange')

if __name__ == '__main__':
    CanvasTutorial()
