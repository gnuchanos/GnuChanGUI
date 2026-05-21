"""Image tutorial - demonstrates GImage usage.
"""

import os

try:
    import GnuChanGUI as gc
except Exception:
    raise

class ImageTutorial(gc.GnuChanGUI):
    def __init__(self):
        super().__init__(Title='Image Tutorial', Size=(420,360), finalize=True)
        logo_path = os.path.join(os.path.dirname(gc.__file__), 'logo.png')

        self.Layout = [
            [self.GText(SetText='Image demo', TFont='Sans,14', xStretch=True)],
            [self.GImage(SetValue='pic', filename=logo_path, xStretch=True)],
            [self.GButton(Text='Refresh', SetValue='refresh')]
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(self.Update)

    def Update(self):
        if not self.GetValues:
            return
        if self.GetEvent == 'refresh':
            logo_path = os.path.join(os.path.dirname(gc.__file__), 'logo.png')
            self.GetWindow['pic'].update(filename=logo_path)

if __name__ == '__main__':
    ImageTutorial()
