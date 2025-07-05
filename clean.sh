#!/bin/bash

cp -r ~/.local/lib/python3.13/site-packages/GnuChanGUI/  /SSD/Github/GnuChanGE/src/Engine/Python/lib/python3.13/site-packages/

# extra
cp -r ~/.local/lib/python3.13/site-packages/pygame  ~/.local/lib/python3.13/site-packages/pygame-2.6.1.dist-info  ~/.local/lib/python3.13/site-packages/pygame.libs /SSD/Github/GnuChanGE/src/Engine/Python/lib/python3.13/site-packages/
cp -r ~/.local/lib/python3.13/site-packages/shapely ~/.local/lib/python3.13/site-packages/shapely-2.1.0.dist-info ~/.local/lib/python3.13/site-packages/shapely.libs /SSD/Github/GnuChanGE/src/Engine/Python/lib/python3.13/site-packages/
cp -r ~/.local/lib/python3.13/site-packages/pynput  ~/.local/lib/python3.13/site-packages/pynput-1.8.1.dist-info /SSD/Github/GnuChanGE/src/Engine/Python/lib/python3.13/site-packages
cp -r /usr/lib/python3.13/site-packages/psutil /usr/lib/python3.13/site-packages/psutil-7.0.0.dist-info /SSD/Github/GnuChanGE/src/Engine/Python/lib/python3.13/site-packages/

pip install .
rm -r GnuChanGUI.egg-info build