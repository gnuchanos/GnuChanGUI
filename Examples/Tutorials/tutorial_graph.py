"""Graph tutorial - demonstrates GGraph usage.
"""

try:
    import GnuChanGUI as gc
except Exception:
    raise

class GraphTutorial(gc.GnuChanGUI):
    def __init__(self):
        super().__init__(Title='Graph Tutorial', Size=(520,320), finalize=True)

        self.Layout = [
            [self.GText(SetText='Graph demo', TFont='Sans,14', xStretch=True)],
            [self.GGraph(SetValue='graf', canvas_size=(400,200), graph_bottom_left=(0,0), graph_top_right=(100,100), xStretch=True, yStretch=True)],
            [self.GButton(Text='Draw Line', SetValue='draw')]
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(self.Update)

    def Update(self):
        if not self.GetValues:
            return
        if self.GetEvent == 'draw':
            g = self.GetWindow['graf']
            g.erase()
            g.draw_line((10,10), (90,90), color='red', width=2)

if __name__ == '__main__':
    GraphTutorial()
