Tutorials for GnuChanGUI

Quick run:

1) (optional) create and activate a venv

2) Install optional dependencies for advanced examples:

```bash
pip install -r Examples/Tutorials/requirements.txt
```

3) Run a tutorial (example):

```bash
python Examples/Tutorials/tutorial_button.py
```

Notes:
- `Pillow` is required for `GGameCanvas` examples.
- `pygame` is required for `GMixer` examples.
- `logo.png` is available under `GnuChanGUI/GnuChanGUI/logo.png` and is used by the image tutorials.
- `welcome.mp3` is available in the repo root and can be used by the mixer tutorial.
- If there is no `.gif` file, `tutorial_imagegif.py` falls back to the static logo image.
