"""Image GIF tutorial - demonstrates GImageGif usage (animated GIF).
"""

import os

try:
    import GnuChanGUI as gc
except Exception:
    raise

class ImageGifTutorial(gc.GnuChanGUI):
    def __init__(self):
        super().__init__(Title='Image GIF Tutorial', Size=(420,360), finalize=True)
        package_dir = os.path.dirname(gc.__file__)
        gif_path = None
        for item in os.listdir(package_dir):
            if item.lower().endswith('.gif'):
                gif_path = os.path.join(package_dir, item)
                break
        if gif_path is None:
            # fallback to a static image if no gif is available
            gif_path = os.path.join(package_dir, 'logo.png')

        self.Layout = [
            [self.GText(SetText='Image GIF demo', xStretch=True)],
            [self.GImageGif(SetValue='gif', filename=gif_path, xStretch=True)],
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(self.Update)

    def Update(self):
        # If anim.gif is present, user can use GetWindow['gif'].update_animation in real usage
        return

if __name__ == '__main__':
    ImageGifTutorial()
