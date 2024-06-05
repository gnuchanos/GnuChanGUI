import pyautogui
from PIL import Image
import os, random

screenshot = pyautogui.screenshot()
Dir = os.path.expanduser("~")
rand = random.randrange(1, 1000)
screenshot.save(f"{Dir}/screenshot{rand}.png")
