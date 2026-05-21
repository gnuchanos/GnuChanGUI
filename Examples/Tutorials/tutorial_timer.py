"""Timer tutorial - demonstrates GTimer usage.
"""

try:
    import GnuChanGUI as gc
except Exception:
    raise

class TimerTutorial(gc.GnuChanGUI):
    def __init__(self):
        super().__init__(Title='Timer Tutorial', Size=(420,180), finalize=True)

        self.timer = gc.GTimer()

        self.Layout = [
            [self.GText(SetText='Timer demo', xStretch=True)],
            [self.GButton(Text='Start', SetValue='start'), self.GButton(Text='Stop', SetValue='stop')],
            [self.GText(SetText='Time: 0:0:0', SetValue='lbl')]
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(self.Update, exitBEFORE=self.BeforeExit)

    def Update(self):
        if self.GetEvent == 'start':
            self.timer.TimerStarts = True
        if self.GetEvent == 'stop':
            self.timer.TimerStarts = False
        # update label
        self.GetWindow['lbl'].update('Time: ' + self.timer.StringTime)

    def BeforeExit(self):
        self.timer.KillThreads = True

if __name__ == '__main__':
    TimerTutorial()
