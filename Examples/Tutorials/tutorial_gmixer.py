"""GMixer tutorial - demonstrates GMixer audio playback (requires pygame).
"""

try:
    import GnuChanGUI as gc
except Exception:
    raise

import os

class GMixerTutorial(gc.GnuChanGUI):
    def __init__(self):
        super().__init__(Title='GMixer Tutorial', Size=(480,220), finalize=True)

        # try to auto-detect some audio files in package root or repository root
        base_dirs = [os.path.dirname(os.path.abspath(gc.__file__)), os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(gc.__file__)), '..')), os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(gc.__file__)), '..', '..'))]
        candidates = []
        for base in base_dirs:
            if not os.path.isdir(base):
                continue
            for ext in ('mp3','wav','ogg'):
                candidates.extend([os.path.join(base, f) for f in os.listdir(base) if f.lower().endswith(ext)])
        candidates = list(dict.fromkeys(candidates))
        if not candidates:
            # fallback to welcome.mp3 from repo root if present
            fallback = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(gc.__file__)), '..', 'welcome.mp3'))
            if os.path.isfile(fallback):
                candidates.append(fallback)

        self.mixer = None
        try:
            self.mixer = gc.GMixer(SoundFileList=candidates)
        except Exception as e:
            self.mixer = None
            self.err = str(e)

        self.Layout = [
            [self.GText(SetText='GMixer demo', xStretch=True)],
            [self.GButton(Text='Play', SetValue='play'), self.GButton(Text='Stop', SetValue='stop')],
            [self.GButton(Text='Prev', SetValue='prev'), self.GButton(Text='Next', SetValue='next')],
            [self.GSlider(MaxRange=(0,10), DefaultValue=10, SetValue='vol', xStretch=True)],
            [self.GText(SetText='Status: ', SetValue='status', xStretch=True)],
        ]

        if self.mixer is None:
            self.Layout = [[self.GText(SetText='GMixer unavailable: ' + getattr(self, 'err', 'pygame missing'), xStretch=True)]]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(self.Update)

    def Update(self):
        if not self.GetValues:
            return
        ev = self.GetEvent
        if ev == 'play' and self.mixer:
            if self.mixer.SoundFileList:
                self.mixer.PlaySound_SingleChannel(self.mixer.SoundFileList[self.mixer.SoundIndex])
                self.GetWindow['status'].update('Playing: ' + str(self.mixer.MusicName))
            else:
                self.GetWindow['status'].update('No sound files found')
        elif ev == 'stop' and self.mixer:
            self.mixer.StopSound()
            self.GetWindow['status'].update('Stopped')
        elif ev == 'next' and self.mixer:
            self.mixer.NextSound_SingleChannel()
            self.GetWindow['status'].update('Playing: ' + str(self.mixer.MusicName))
        elif ev == 'prev' and self.mixer:
            self.mixer.PreviousSound_SingleChannel()
            self.GetWindow['status'].update('Playing: ' + str(self.mixer.MusicName))
        elif ev == 'vol' and self.mixer:
            v = self.GetValues.get('vol')
            if v is not None:
                try:
                    # slider range 0-10 -> convert to 0.0-1.0
                    self.mixer.Volume = float(v) / 10.0
                    self.mixer.VolumeChange_Gslider(int(v))
                    self.GetWindow['status'].update(f'Volume: {self.mixer.Volume:.2f}')
                except Exception:
                    pass

if __name__ == '__main__':
    GMixerTutorial()
