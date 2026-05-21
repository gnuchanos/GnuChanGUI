"""Button tutorial - demonstrates single Button interactions.
"""

try:
    import GnuChanGUI as gc
except Exception:
    raise

class ButtonTutorial(gc.GnuChanGUI):
    def __init__(self):
        super().__init__(Title='Button Tutorial', Size=(400,200), finalize=True)

        self.Layout = [
            [self.GText(SetText='Button demo', TFont='Sans,14', TPosition='center', xStretch=True)],
            [self.GButton(Text='Click me', SetValue='btn_click')],
            [self.GText(SetText='Last action:', SetValue='lbl_action')]
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(self.Update)

    def Update(self):
        if not self.GetValues:
            return
        if self.GetEvent == 'btn_click':
            self.GetWindow['lbl_action'].update('Last action: Button clicked')

if __name__ == '__main__':
    ButtonTutorial()
