"""ButtonMenu tutorial - demonstrates GButtonMenu usage.
"""

try:
    import GnuChanGUI as gc
except Exception:
    raise

class ButtonMenuTutorial(gc.GnuChanGUI):
    def __init__(self):
        super().__init__(Title='ButtonMenu Tutorial', Size=(420,200), finalize=True)

        menu_def = ['Actions', ['Say Hello', 'Do Nothing', 'Exit']]
        self.Layout = [
            [self.GText(SetText='ButtonMenu demo', xStretch=True)],
            [self.GButtonMenu('Actions', menu_def, SetValue='bmenu')],
            [self.GText(SetText='Last:', SetValue='lbl')]
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(self.Update)

    def Update(self):
        if not self.GetValues:
            return
        if self.GetEvent == 'Say Hello':
            self.GetWindow['lbl'].update('Hello')
        if self.GetEvent == 'Exit':
            self.GetWindow.close()

if __name__ == '__main__':
    ButtonMenuTutorial()
