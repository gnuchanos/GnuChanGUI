"""Multiline (text area) tutorial - demonstrates multiline element.
"""

try:
    import GnuChanGUI as gc
except Exception:
    raise

class MultilineTutorial(gc.GnuChanGUI):
    def __init__(self):
        super().__init__(Title='Multiline Tutorial', Size=(520,300), finalize=True)

        self.Layout = [
            [self.GText(SetText='Multiline demo', TFont='Sans,14', xStretch=True)],
            [self.GMultiline(InText='Hello\nThis is a GMultiline example.', SetValue='multi', xStretch=True, yStretch=True, Size=(None,8))],
            [self.GButton(Text='Count Lines', SetValue='count')],
            [self.GText(SetText='Lines: 0', SetValue='lbl')]
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(self.Update)

    def Update(self):
        if not self.GetValues:
            return
        if self.GetEvent == 'count':
            txt = self.GetValues.get('multi', '')
            lines = str(txt).count('\n') + 1 if txt else 0
            self.GetWindow['lbl'].update('Lines: ' + str(lines))

if __name__ == '__main__':
    MultilineTutorial()
