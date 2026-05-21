"""Advanced GameCanvas tutorial - simple animation using GGameCanvas (requires Pillow).
"""

try:
    import GnuChanGUI as gc
except Exception:
    raise

class GameCanvasAdvanced(gc.GnuChanGUI):
    def __init__(self):
        super().__init__(Title='GameCanvas Advanced', Size=(640,480), finalize=True)

        try:
            self.Layout = [
                [self.GText(SetText='GameCanvas advanced demo', xStretch=True)],
                [self.GGameCanvas(SetValue='gcv', Size=(80,50), xStretch=True, yStretch=True)],
                [self.GButton(Text='Start', SetValue='start'), self.GButton(Text='Stop', SetValue='stop')]
            ]
            self.GWindow(SetMainWindowLayout_List=self.Layout)
        except Exception as e:
            self.Layout = [[self.GText(SetText='GGameCanvas unavailable: ' + str(e), xStretch=True)]]
            self.GWindow(SetMainWindowLayout_List=self.Layout)
            return

        self.pos_x = 50
        self.dir = 1
        self.running = False
        self.SetUpdate(self.Update)

    def Update(self):
        if not self.GetValues:
            return
        if self.GetEvent == 'start':
            self.running = True
        if self.GetEvent == 'stop':
            self.running = False

        cv = self.GetWindow.get('gcv')
        if not cv:
            return

        if self.running:
            # simple movement
            self.pos_x += 4 * self.dir
            if self.pos_x > cv.GetCanvasWidth() - 50 or self.pos_x < 50:
                self.dir *= -1

        try:
            cv.BeginDrawing()
            cv.EndDrawing()
            # draw entity manual
            cv.DrawRectangle(gc.GVector2(self.pos_x, 120), gc.GVector2(80, 40), 0, gc.GColor_HEX('#ffcc00'), 0, fill=True, fillColor=gc.GColor_HEX('#ffcc00'))
        except Exception as e:
            gc.GMessage(WindowTitle='Canvas error', WindowText=str(e))

if __name__ == '__main__':
    GameCanvasAdvanced()
