"""StatusBar tutorial - demonstrates GStatusBar usage.
"""

import time

try:
    import GnuChanGUI as gc
except Exception:
    raise

class StatusBarTutorial(gc.GnuChanGUI):
    def __init__(self):
        super().__init__(Title='StatusBar Tutorial', Size=(520,200), finalize=True)

        self.Layout = [
            [self.GText(SetText='StatusBar demo', xStretch=True)],
            [self.GStatusBar(SetText='Ready', SetValue='sb', xStretch=True)],
            [self.GButton(Text='Update', SetValue='upd')]
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(self.Update)

    def Update(self):
        if not self.GetValues:
            return
        if self.GetEvent == 'upd':
            self.GetWindow['sb'].update('Updated: ' + str(int(time.time()) % 1000))

if __name__ == '__main__':
    StatusBarTutorial()
