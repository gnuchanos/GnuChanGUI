"""Colors tutorial - demonstrates GColors, RandColor, GnuChanOSColor, Themecolors usage.
"""

try:
    import GnuChanGUI as gc
except Exception:
    raise

class ColorsTutorial(gc.GnuChanGUI):
    def __init__(self):
        super().__init__(Title='Colors Tutorial', Size=(520,300), finalize=True)

        c = gc.GColors()
        rand = gc.RandColor()
        oscol = gc.GnuChanOSColor()

        swatches = [c.red1, c.green1, c.blue1, c.yellow1, c.purple1, c.pink1, oscol.BGColor, rand.take]

        rows = [[self.GText(SetText='Colors demo', TFont='Sans,14', xStretch=True)]]
        for idx, col in enumerate(swatches):
            rows.append([self.GButton(Text=f'Color {idx+1}', SetValue=f'c{idx}', bcolor=col)])

        rows.append([self.GButton(Text='Apply GnuChanOS Theme', SetValue='theme')])

        self.Layout = rows
        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(self.Update)

    def Update(self):
        if not self.GetValues:
            return
        if self.GetEvent == 'theme':
            gc.Themecolors().GnuChanOS
            gc.GMessage(WindowTitle='Theme', WindowText='Applied GnuChanOS theme')
        for i in range(8):
            if self.GetEvent == f'c{i}':
                gc.GMessage(WindowTitle='Color', WindowText=f'Selected color button {i+1}')

if __name__ == '__main__':
    ColorsTutorial()
