"""Input (single-line) tutorial - demonstrates text input element.
"""

try:
    import GnuChanGUI as gc
except Exception:
    raise

class InputTutorial(gc.GnuChanGUI):
    def __init__(self):
        super().__init__(Title='Input Tutorial', Size=(420,180), finalize=True)

        self.Layout = [
            [self.GText(SetText='Input demo', TFont='Sans,14', xStretch=True)],
            [self.GInput(InText='Type here...', SetValue='inp', xStretch=True)],
            [self.GButton(Text='Show', SetValue='show')],
            [self.GText(SetText='You typed:', SetValue='lbl')]
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(self.Update)

    def Update(self):
        if not self.GetValues:
            return
        if self.GetEvent == 'show':
            v = self.GetValues.get('inp')
            self.GetWindow['lbl'].update('You typed: ' + str(v))

if __name__ == '__main__':
    InputTutorial()
