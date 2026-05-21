"""GameCanvas tutorial - demonstrates GGameCanvas basics (requires Pillow).
"""

try:
    import GnuChanGUI as gc
except Exception:
    raise

class GameCanvasTutorial(gc.GnuChanGUI):
    def __init__(self):
        super().__init__(Title='GameCanvas Tutorial', Size=(600,420), finalize=True)

        try:
            # If Pillow missing, GGameCanvas will raise on import
            self.Layout = [
                [self.GText(SetText='GameCanvas demo', xStretch=True)],
                [self.GGameCanvas(SetValue='gcv', Size=(60,20), xStretch=True, yStretch=True)],
                [self.GButton(Text='Test Draw', SetValue='draw')]
            ]
        except Exception as e:
            self.Layout = [[self.GText(SetText='GameCanvas unavailable: ' + str(e), xStretch=True)]]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(self.Update)

    def Update(self):
        if not self.GetValues:
            return
        if self.GetEvent == 'draw':
            try:
                cv = self.GetWindow['gcv']
                cv.BeginDrawing()
                cv.DrawText('Hello', 'Sans, 20', 100, 100, gc.GColor_HEX('#FFFFFF'))
                cv.DrawLine(gc.GVector2(50,50), gc.GVector2(150,150), gc.GColor_HEX('#FF0000'), 2)
                cv.EndDrawing()
            except Exception as e:
                gc.GMessage(WindowTitle='Error', WindowText=str(e))

if __name__ == '__main__':
    GameCanvasTutorial()
