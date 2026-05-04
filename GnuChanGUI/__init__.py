from .gcLibrary import *
from .gcLibrary import __version__
from .version import __version_full__

import os
import random
import math
import threading
import time
from threading import Thread
from contextlib import contextmanager

"""
pip install  git+https://github.com/gnuchanos/gnuchangui
"""

"""
python -m venv ./venv
./venv/bin/activate 
"""

"""
Warning 0: popup_get_file('Select a file to open', no_window=True) isn't working with Thread(target=Create, args=[]).start()
The GUI is freezing, and you can only close the program using the task manager.
"""

class GTime:
    def __init__(self):
        self.last_time = time.perf_counter()
        self.FPS = 60
    
    def Ready(self):
        self.last_time = time.perf_counter()

    def DeltaTime(self):
        now = time.perf_counter()
        delta = now - self.last_time
        self.last_time = now

        if self.FPS > 0:
            frame_duration = 1 / self.FPS
            if delta < frame_duration:
                time.sleep(frame_duration - delta)

        return delta


# this is for spywareDOS  -> self.CurrentKey == self.space (from pynput import keyboard) i don't want to embed in main class
class GKeyboard_Winows:
    def __init__(self) -> None:
        # Function keys
        self.F1  = "F1:112"
        self.F2  = "F2:113"
        self.F3  = "F3:114"
        self.F4  = "F4:115"
        self.F5  = "F5:116"
        self.F6  = "F6:117"
        self.F7  = "F7:118"
        self.F8  = "F8:119"
        self.F9  = "F9:120"
        self.F10 = "F10:121"
        self.F11 = "F11:122"
        self.F12 = "F12:123"

        # Numbers (top row)
        self.Number_0 = "0:48"
        self.Number_1 = "1:49"
        self.Number_2 = "2:50"
        self.Number_3 = "3:51"
        self.Number_4 = "4:52"
        self.Number_5 = "5:53"
        self.Number_6 = "6:54"
        self.Number_7 = "7:55"
        self.Number_8 = "8:56"
        self.Number_9 = "9:57"

        # Letters (A–Z)
        self.A = "A:65"
        self.B = "B:66"
        self.C = "C:67"
        self.D = "D:68"
        self.E = "E:69"
        self.F = "F:70"
        self.G = "G:71"
        self.H = "H:72"
        self.I = "I:73"
        self.J = "J:74"
        self.K = "K:75"
        self.L = "L:76"
        self.M = "M:77"
        self.N = "N:78"
        self.O = "O:79"
        self.P = "P:80"
        self.Q = "Q:81"
        self.R = "R:82"
        self.S = "S:83"
        self.T = "T:84"
        self.U = "U:85"
        self.V = "V:86"
        self.W = "W:87"
        self.X = "X:88"
        self.Y = "Y:89"
        self.Z = "Z:90"

        # Control keys
        self.Backspace = "Backspace:8"
        self.Tab       = "Tab:9"
        self.Enter     = "Enter:13"
        self.Shift     = "Shift:160"
        self.LeftShit  = "Shift_r:161"
        self.Control   = "Control:162"
        self.ControlR  = "Ctrl_r:163"
        self.Alt       = "Alt_l:164"
        self.AltGR     = "Alt_gr:165"
        self.CapsLock  = "CapsLock:20"
        self.Escape    = "Escape:27"
        self.Space     = "Space:32"

        # Arrow keys
        self.Left  = "Left:37"
        self.Up    = "Up:38"
        self.Right = "Right:39"
        self.Down  = "Down:40"

        # Navigation
        self.PrintScreen = "Print_screen:44"
        self.ScrollLock = "Scroll_lock:145"
        self.Insert = "Insert:45"
        self.Delete = "Delete:46"
        self.Home   = "Home:36"
        self.End    = "End:35"
        self.PageUp = "PageUp:33"
        self.PageDown = "PageDown:34"

        # Numpad
        self.NumLock = "Num_Lock:144"
        self.Numpad0 = "<96>:96"
        self.Numpad1 = "<97>:97"
        self.Numpad2 = "<98>:98"
        self.Numpad3 = "<99>:99"
        self.Numpad4 = "<100>:100"
        self.Numpad5 = "<101>:101"
        self.Numpad6 = "<102>:102"
        self.Numpad7 = "<103>:103"
        self.Numpad8 = "<104>:104"
        self.Numpad9 = "<105>:105"
        self.NumpadMultiply = "*:106"
        self.NumpadAdd      = "+:107"
        self.NumpadSubtract = "-:109"
        self.NumpadDivide   = "/:111"




# more colors
class GColors:
    def __init__(self) -> None:
        # Red Colors and Shades
        self.red1 = "#FF0000"
        self.red2 = "#FF4500"
        self.red3 = "#DC143C"
        self.red4 = "#FF6347"
        self.red5 = "#FFA07A"
        self.red6 = "#B22222"
        self.red7 = "#FF0000"
        self.red8 = "#8B0000"

        # Green Colors and Shades
        self.green1 = "#008000"
        self.green2 = "#00FF00"
        self.green3 = "#7FFF00"
        self.green4 = "#228B22"
        self.green5 = "#32CD32"
        self.green6 = "#ADFF2F"
        self.green7 = "#556B2F"
        self.green8 = "#008B8B"

        # Blue Colors and Shades
        self.blue1 = "#0000FF"
        self.blue2 = "#000080"
        self.blue3 = "#87CEEB"
        self.blue4 = "#00008B"
        self.blue5 = "#ADD8E6"
        self.blue6 = "#1E90FF"
        self.blue7 = "#0000CD"
        self.blue8 = "#191970"

        # Yellow Colors and Shades
        self.yellow1 = "#FFFF00"
        self.yellow2 = "#FFD700"
        self.yellow3 = "#FFA500"
        self.yellow4 = "#FFC0CB"
        self.yellow5 = "#FF4500"
        self.yellow6 = "#FF6347"
        self.yellow7 = "#FFFFE0"
        self.yellow8 = "#FFFF66"

        # Orange Colors and Shades
        self.orange1 = "#FFA500"
        self.orange2 = "#FF4500"
        self.orange3 = "#FF6347"
        self.orange4 = "#FF8C00"
        self.orange5 = "#FF7F50"
        self.orange6 = "#FFA07A"
        self.orange7 = "#FFD700"
        self.orange8 = "#FFB6C1"

        # Navy Colors and Shades
        self.navy1 = "#000080"
        self.navy2 = "#00008B"
        self.navy3 = "#0000CD"
        self.navy4 = "#0000FF"
        self.navy5 = "#000066"
        self.navy6 = "#000044"
        self.navy7 = "#191970"
        self.navy8 = "#333399"

        # Pink Colors and Shades
        self.pink1 = "#FFC0CB"
        self.pink2 = "#FF69B4"
        self.pink3 = "#FF1493"
        self.pink4 = "#DB7093"
        self.pink5 = "#C71585"
        self.pink6 = "#FFB6C1"
        self.pink7 = "#FFC0CB"
        self.pink8 = "#FF69B4"

        # Purple Colors and Shades
        self.purple1 = "#aa66ff"
        self.purple2 = "#790dff"
        self.purple3 = "#680bdb"
        self.purple4 = "#5908bd"
        self.purple5 = "#460694"
        self.purple6 = "#33036e"
        self.purple7 = "#22024a"
        self.purple8 = "#0f0121"

        # this is little light purple yes have dark version
        self.LightPurple0 = "#a359ff"
        self.LightPurple1 = "#9652eb"
        self.LightPurple2 = "#874ad4"
        self.LightPurple3 = "#7843ba"
        self.LightPurple4 = "#64389c"
        self.LightPurple5 = "#522f80"
        self.LightPurple6 = "#3a215c"
        self.LightPurple7 = "#25163b"

        # Turquoise Colors and Shades
        self.turquoise1 = "#40E0D0"
        self.turquoise2 = "#00CED1"
        self.turquoise3 = "#20B2AA"
        self.turquoise4 = "#008B8B"
        self.turquoise5 = "#00FFFF"
        self.turquoise6 = "#00CED1"
        self.turquoise7 = "#20B2AA"
        self.turquoise8 = "#008B8B"

        # Gray Colors and Shades
        self.gray1 = "#808080"
        self.gray2 = "#A9A9A9"
        self.gray3 = "#C0C0C0"
        self.gray4 = "#D3D3D3"
        self.gray5 = "#DCDCDC"
        self.gray6 = "#F5F5F5"
        self.gray7 = "#696969"
        self.gray8 = "#2F4F4F"

        # Black and White
        self.black = "#000000"
        self.white = "#FFFFFF"

class RandColor:
    @property
    def take(self):
        randomColor = random.choice([
            "#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#00FFFF", "#FF00FF", "#FFFFFF", 
            "#000000", "#800080", "#FFA500", "#FFC0CB", "#008080", "#FFD700", "#A52A2A", 
            "#FF1493", "#4B0082", "#00FF7F", "#1E90FF", "#FF4500", "#FF69B4"
        ])
        return randomColor

class GnuChanOSColor:
    def __init__(self) -> None:
        self.BGColor = "#240046"
        self.TColor  = "#9d4edd"
        # First Part
        self.FColors0 = "#1f0047"
        self.FColors1 = "#240052"  
        self.FColors2 = "#260058" 
        self.FColors3 = "#2a0061" 

        self.FColors4 = "#30006f"  
        self.FColors5 = "#390082"
        self.FColors6 = "#400094"  
        self.FColors7 = "#4a00aa"

        self.FColors8 = "#4f00b5"  
        self.FColors9 = "#5600c6"
        self.FColors10 = "#6300e4"  
        self.FColors11 = "#6f00ff"

        # Second Part
        self.SColors0 = "#1d0031"
        self.SColors1 = "#1e0037"  
        self.SColors2 = "#39005f" 
        self.SColors3 = "#510087" 

        self.SColors4 = "#260046"  
        self.SColors5 = "#300058"
        self.SColors6 = "#3d0070"  
        self.SColors7 = "#4b008a"

        self.SColors4 = "#5700a0"  
        self.SColors5 = "#6300b8"
        self.SColors6 = "#6f00cd"  
        self.SColors7 = "#8a00ff"

class Themecolors:
    @property
    def GnuChanOS(self, themeName="GnuchanTheme", 
                text="#9d4edd", 
                background="#240046", 
                input="#3c096c", 
                text_input="#9d4edd", 
                scroll="#5a189a", 
                button=('#c77dff', '#3c096c'), 
                progress=('#c77dff', '#3c096c'), 
                border=0, slider_depth=0, progress_depth=0):
        LOOK_AND_FEEL_TABLE[themeName] = {
                                        'BACKGROUND': background, 'TEXT': text, 'INPUT': input, 'TEXT_INPUT': text_input,
                                        'SCROLL': scroll, 'BUTTON': button, 'PROGRESS': progress, 
                                        'BORDER': border, 'SLIDER_DEPTH': slider_depth, 'PROGRESS_DEPTH': progress_depth}
        theme(themeName)

    @property
    def Black(self, themeName="Black", 
            text="#fffcfc",  # text
            background="#131313", 
            input="#545454", # tab background
            text_input="#fffcfc", # tab text
            scroll="#a7a7a7", 
            button=('#fffcfc', '#383838'), # button text, background
            progress=('#fffcfc', '#383838'), # process, background
            border=0, slider_depth=0, progress_depth=0):
        LOOK_AND_FEEL_TABLE[themeName] = {
                                        'BACKGROUND': background, 'TEXT': text, 'INPUT': input, 'TEXT_INPUT': text_input,
                                        'SCROLL': scroll, 'BUTTON': button, 'PROGRESS': progress, 
                                        'BORDER': border, 'SLIDER_DEPTH': slider_depth, 'PROGRESS_DEPTH': progress_depth}
        theme(themeName)

    @property
    def Blue(self, themeName="Blue", 
            text="#cfe6f9",  # text
            background="#002342", 
            input="#545454", # tab background
            text_input="#cfe6f9", # tab text
            scroll="#0d62ad", 
            button=('#cfe6f9', '#1a3c59'), # button text, background
            progress=('#cfe6f9', '#1a3c59'), # process, background
            border=0, slider_depth=0, progress_depth=0):
        LOOK_AND_FEEL_TABLE[themeName] = {
                                        'BACKGROUND': background, 'TEXT': text, 'INPUT': input, 'TEXT_INPUT': text_input,
                                        'SCROLL': scroll, 'BUTTON': button, 'PROGRESS': progress, 
                                        'BORDER': border, 'SLIDER_DEPTH': slider_depth, 'PROGRESS_DEPTH': progress_depth}
        theme(themeName)

    @property
    def Red(self, themeName="Red", 
            text="#fca9a9",  # text
            background="#3a0202", 
            input="#c90e0e", # tab background
            text_input="#fca9a9", # tab text
            scroll="#0d62ad", 
            button=('#fca9a9', '#4f1d1d'), # button text, background
            progress=('#fca9a9', '#4f1d1d'), # process, background
            border=0, slider_depth=0, progress_depth=0):
        LOOK_AND_FEEL_TABLE[themeName] = {
                                        'BACKGROUND': background, 'TEXT': text, 'INPUT': input, 'TEXT_INPUT': text_input,
                                        'SCROLL': scroll, 'BUTTON': button, 'PROGRESS': progress, 
                                        'BORDER': border, 'SLIDER_DEPTH': slider_depth, 'PROGRESS_DEPTH': progress_depth}
        theme(themeName)

    @property
    def Green(self, themeName="Green", 
            text="#a9fc9c",  # text
            background="#0f6b01", 
            input="#168405", # tab background
            text_input="#a9fc9c", # tab text
            scroll="#0d62ad", 
            button=('#a9fc9c', '#2a4925'), # button text, background
            progress=('#a9fc9c', '#2a4925'), # process, background
            border=0, slider_depth=0, progress_depth=0):
        LOOK_AND_FEEL_TABLE[themeName] = {
                                        'BACKGROUND': background, 'TEXT': text, 'INPUT': input, 'TEXT_INPUT': text_input,
                                        'SCROLL': scroll, 'BUTTON': button, 'PROGRESS': progress, 
                                        'BORDER': border, 'SLIDER_DEPTH': slider_depth, 'PROGRESS_DEPTH': progress_depth}
        theme(themeName)



# i hope this become better one day
class GnuChanGUI:
    def __init__(self, Title: str = "Defaul Title", Size: tuple = (800, 600), resizable: bool = False, finalize: bool = True, winPosX: float = 1920/2, winPosY: float = 1080/2) -> None:
        self.size = Size
        self.title = Title
        self.resizable = resizable
        self.finalize = finalize

        self.WinPosX = winPosX
        self.WinPosY = winPosY

        self.fontName = "Sans"
        self.fontSize = 15
        self.font = f"{self.fontName}, {self.fontSize}"

        self.UpdateMissing = False
        self.ExitBeforeMissing = False

        self.code = """
        Example for window layout
            self.Layout = [
                [self.GC.GText(SetText="Hello foking world")]
            ]

            self.GC.GWindow(SetMainWindowLayout_List=self.Layout)
        """
        self.layout = [[self.GText(SetText=self.code, xStretch=True, yStretch=True, BColor="black", TFont="Sans, 13")]]

        self.GetEvent = None
        self.GetValues = None
        self.closeWindow = False
        self.TKroot = ""

        # don't remove ),<--)
        self.ImagesType = [("PNG (*.png)", "*.png"), ("JPEG (*.jpg)", "*.jpg")]
        self.VideoTypes = [("MKV (*.mkv)", "*.mkv"), ("MP4 (*.mp4)", "*.mp4")]
        self.MusicTypes = [("MP3 (*.mp3)", "*.mp3")]
        self.AllTypes   = [("All Files (*.*)", "*.*"), ("Linux Files (**)", "**")]

        # f"{gc.PathPythonFile}/music.mp3" or diffrent file
        self.PathPythonFile = os.path.dirname(os.path.abspath(__file__))

        self.Num0 = "0:48"
        self.Num1 = "1:49"
        self.Num2 = "2:50"
        self.Num3 = "3:51"
        self.Num4 = "4:52"
        self.Num5 = "5:53"
        self.Num6 = "6:54"
        self.Num7 = "7:55"
        self.Num8 = "8:56"
        self.Num9 = "9:57"

        self.A = "A:97"
        self.B = "B:98"
        self.C = "C:99"
        self.D = "D:100"
        self.E = "E:101"
        self.F = "F:102"
        self.G = "G:103"
        self.H = "H:104"
        self.I = "I:105"
        self.J = "J:106"
        self.K = "K:107"
        self.L = "L:108"
        self.M = "M:109"
        self.N = "N:110"
        self.O = "O:111"
        self.P = "P:112"
        self.Q = "Q:113"
        self.R = "R:114"
        self.S = "S:115"
        self.T = "T:116"
        self.U = "U:117"
        self.V = "V:118"
        self.W = "W:119"
        self.X = "X:120"
        self.Y = "Y:121"
        self.Z = "Z:122"

        self.Numpad0 = "0:None"
        self.Numpad1 = "1:None"
        self.Numpad2 = "2:None"
        self.Numpad3 = "3:None"
        self.Numpad4 = "4:None"
        self.Numpad5 = "<65437>:65437"
        self.Numpad6 = "6:None"
        self.Numpad7 = "7:None"
        self.Numpad8 = "8:None"
        self.Numpad9 = "9:None"

        self.Kp_add = "Keypad_Plus:65451"
        self.Kp_subtract = "Keypad_Minus:65453"
        self.Kp_multiply = "Keypad_Multiply:65450"
        self.Kp_divide = "Keypad_Divide:65455"
        self.Kp_enter = "Keypad_Enter:65421"
        self.Kp_decimal = "Keypad_Decimal:65454"

        self.Space = "Space:32"
        self.Enter = "Enter:65293"
        self.Tab = "Tab:65289" 
        self.Backspace = "Backspace:65288"
        self.Comma = "Comma:44"
        self.Period = "Period:46"
        self.Slash = "Slash:47"
        self.Backslash = "Backslash:92"
        self.Semicolon = "Semicolon:59"
        self.Quote = "Quote:39"
        self.Minus = "Minus:45"
        self.Equal = "Equal:61"
        self.Left_bracket = "Left_Bracket:91"
        self.Right_bracket = "Right_Bracket:93"
        self.Grave = "Grave:96"

        self.F1 = "F1:65470"
        self.F2 = "F2:65471"
        self.F3 = "F3:65472"
        self.F4 = "F4:65473"
        self.F5 = "F5:65474"
        self.F6 = "F6:65475"
        self.F7 = "F7:65476"
        self.F8 = "F8:65477"
        self.F9 = "F9:65478"
        self.F10 = "F10:65479"
        self.F11 = "F11:65480"
        self.F12 = "F12:65481"

        self.Up = "Up:65362"
        self.Down = "Down:65364"
        self.Left = "Left:65361"
        self.Right = "Right:65363"

        self.Ctrl_l = "Ctrl_L:65507"
        self.Ctrl_r = "Ctrl_R:65508"
        self.Alt_l = "Alt_L:65513"
        self.Alt_r = "Alt_R:65514"
        self.Shift_l = "Shift_L:65505"
        self.Shift_r = "Shift_R:65506"
        self.Caps_lock = "Caps_Lock:65509"
        self.Esc = "Esc:65307"
        self.Delete = "Delete:65535"
        self.Home = "Home:65360"
        self.End = "End:65367"
        self.Page_up = "Page_Up:65365"
        self.Page_down = "Page_Down:65366"
        self.Num_lock = "Num_Lock:65407"
        self.Print_screen = "Print_Screen:65377"
        self.Pause = "Pause:65299"

        self.Media_play_pause = "Media_Play_Pause:179"
        self.Media_volume_mute = "Media_Volume_Mute:173"
        self.Media_volume_up = "Media_Volume_Up:175"
        self.Media_volume_down = "Media_Volume_Down:174"
        self.Media_previous = "Media_Previous:177"
        self.Media_next = "Media_Next:176"

        self.CurrentKey = ""
        self.pressing = False

        self.PressTimer = 1
        self.PressWait  = False

        self.delta = GTime()

        threading.Thread(target=self.listen, daemon=True).start()

    def on_press(self, key):
        code = getattr(key, 'vk', getattr(getattr(key, 'value', None), 'vk', 'N/A'))
        try:
            if hasattr(key, 'char') and key.char is not None:
                key_name = key.char.upper()
            else:
                key_name = str(key).replace('Key.', '').capitalize()
        except AttributeError:
            key_name = str(key).replace('Key.', '')

        self.CurrentKey = f"{key_name}:{code}"
        self.pressing = True

    def on_release(self, key):
        self.pressing = False
        self.CurrentKey = ""


    def listen(self):
        try:
            from pynput import keyboard
        except ImportError:
            return
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

    def KeyPressed(self, Key: str):
        if Key == self.CurrentKey and not self.PressWait:
            self.PressWait = True
            return True
        
        if self.PressWait:
            if self.PressTimer > 0:
                self.PressTimer -= 1 * self.delta.DeltaTime()
            else:
                self.PressTimer = 1
                self.PressWait = False
  
    

    # Create Window
    def GWindow(self, SetMainWindowLayout_List = None, rightClickMenu = None, KeepOnTop = True, Borderless = False):
        if SetMainWindowLayout_List != None:
            self.layout = SetMainWindowLayout_List
        else:
            self.layout = [[self.GText(SetText=self.code, xStretch=True, yStretch=True, BColor="black", TFont="Sans, 13")]]
            # if main Window is None self.layout can warning user and self.layout is ready warning layout
        self.GetWindow = Window(
            self.title, 
            layout=self.layout, size=self.size, keep_on_top=KeepOnTop, resizable=self.resizable,
            finalize=self.finalize, right_click_menu=rightClickMenu, return_keyboard_events=True, margins=(0, 0), location=(self.WinPosX-self.size[0]/2, self.WinPosY-self.size[1]/2),
            no_titlebar=Borderless
        )
        self.GetWindow.finalize()

        self.TKroot = self.GetWindow.TKroot

        # this is new for close window good way
        return self.GetWindow
        """
        window have right click menu --> ["menu", ["inMenu1", "inMenu2"]]
        """

    def WindowONTOP(self, Transparant):
        self.TKroot.overrideredirect(True)
        self.TKroot.attributes("-topmost", True)
        self.TKroot.attributes("-toolwindow", True) #hide from alt+tab
        if Transparant > 1:
            Transparant = 1
        self.TKroot.attributes("-alpha", Transparant)

    def StillONTOP_UnderUpdate(self):
        self.TKroot.lift()
        self.TKroot.attributes("-topmost", True)

    def WindowONBOTTOM(self, Transparant):
        self.TKroot.overrideredirect(True)
        self.TKroot.attributes("-topmost", False)
        self.TKroot.attributes("-toolwindow", True) #hide from alt+tab
        if Transparant > 1:
            Transparant = 1
        self.TKroot.attributes("-alpha", Transparant)

    def StillONBOTTOM_UnderUpdate(self):
        self.TKroot.lift()
        self.TKroot.attributes("-topmost", False)
        self.TKroot.lower()

    def DisableMouseClick(self):
        self.TKroot.bind("<FocusIn>", lambda e: self.TKroot.focus_force())

    def SetUpdate(self, Update = None, exitBEFORE = None, TimeOUT: int = 100):
        while True:
            self.GetEvent, self.GetValues = self.GetWindow.read(timeout=TimeOUT)
            if self.GetEvent in (WIN_CLOSED, "Exit"):
                if exitBEFORE != None:
                    exitBEFORE()
                    break

            elif self.closeWindow:
                if exitBEFORE != None:
                    exitBEFORE()
                    break
                else:
                    self.ExitBeforeMissing = True
                    break

            if Update != None:
                Update()
            else:
                self.UpdateMissing = True
                break
            

        self.CloseNow
    
    @property
    def CloseNow(self):
        if self.ExitBeforeMissing:
            GMessage(
                WindowTitle="Warning",
                WindowText="closeWindow=True iken exitBEFORE verilmedi. SetUpdate(..., exitBEFORE=sizin_fonksiyon) ekleyin.",
            )
        elif self.UpdateMissing:
            GMessage(
                WindowTitle="Warning",
                WindowText="SetUpdate cagrilirken Update=None. Dongu icin Update=sizin_fonksiyon verin.",
            )

        self.GetWindow.close()

    def GTitleBar(self, title: str = "Window Title", icon: str = None, font: str = "Sans, 12", tcolor: str = None, bcolor: str = None):
        return Titlebar(title=title, icon=icon, font=font, text_color=tcolor, background_color=bcolor)
        """
        Titlebar: Disable window resizable, I don't know why.
        ı must ask this soon
        """

    # window top menu bar regular default or custom for theme
    def GMenu(self, WinMENU_List: list, TFont: str ="Sans, 20"):
        return Menu(menu_definition=WinMENU_List, font=TFont)

    def GMenuForTheme(self, WinMENU_List: list, TFont: str, TColor: str, BColor: str):
        return MenubarCustom(menu_definition=WinMENU_List, font=TFont, text_color=TColor, background_color=BColor)

    """
    gMenu = [ ["Info", ["GnuChanOS", "Youtube Channel", "Github Page"]], ["System", ["Exit"]] ]
    defaultFont = "Sans, 20"
    c = GColors()

    test1 = [
        [gc.GMenuForTheme(WinMENU_List=gMenu, TFont=defaultFont, TColor=c.black, BColor=c.red1)],
        [gc.GText(SetText="Text 1", xStretch=True, TPosition="center")]
    ]
    """
    

    # GetValue With GText
    def GetGTextValue(self, GTextValue: str):
        return self.GetWindow[GTextValue].get()


    def AddNewBorderWithColor(self, WindowValue: str, Color: str, BorderSize: int):
        _mw = self.GetWindow[WindowValue].Widget
        _mw.config(highlightbackground=Color, highlightcolor=Color, highlightthickness=BorderSize)

    def FontSize_Change(self, WindowValue: str, FontSize: int):
        self.GetWindow[WindowValue].update(font=f"{self.fontName}, {FontSize}")

    def TextColor_Change(self, WindowValue: str, Color: str):
        self.GetWindow[WindowValue].update(text_color=Color)

    def BackgroundColor_Change(self, WindowValue: str, Color: str):
        self.GetWindow[WindowValue].update(background_color=Color)

    # ekstra options
    # This setting only works under GWindow. "this is tk"
    def GBorder(self, WindowValue: str, Border: int, Color: str):
        _Q = self.GetWindow[WindowValue].Widget

        _Q.config(
            highlightthickness  = Border,
            highlightbackground = Color,
            highlightcolor      = Color
        )

    def GListboxReturnIndex(self, WindowValue: str):
        return self.GetWindow[WindowValue].Values.index(self.GetValues[WindowValue][0])

    def GSelectionBorderSize(self, Border: str, WindowValue: str, borderColor: str, highlightcolor: str):
        combo = self.GetWindow[WindowValue]
        combostyle, style_name = combo.ttk_style, combo.ttk_style_name
        combostyle.configure(style_name, selectbackground=borderColor, selectforeground=highlightcolor, borderwidth=Border)

    def GMultilineTabSpace(self, TFont: str, WindowValue: str):
        char = Text.char_width_in_pixels(TFont)
        tabs = (2*char, 'left', 4*char, 'left')
        multiline = self.GetWindow[WindowValue]
        multiline.Widget.configure(tabs=tabs)







    # this can change visible true or false but also change layer position! i don't know how to fix for now or never
    # Don't Forget to Pin Object or Index Can Change
    def GVisible(self, WindowValue: str , show: bool):
        self.GetWindow[WindowValue].update(visible=show)
        if show:
            self.GetWindow[WindowValue].unhide_row()
        else:
            self.GetWindow[WindowValue].hide_row()

    # Canvas: ham tk.Canvas; cizim icin .TKCanvas veya oyun icin asagidaki GCanvas sinifi (erase, focus_canvas)
    def GCanvas(
        self, SetValue: str, BColor: str = "black", xStretch: bool = False, yStretch: bool = False, Visible: bool = True, border: int = 0,
        Size: tuple = (None, None), EmptySpace: tuple = (None, None), tooltip: str = None, rclickMenu=None, metadata=None,
    ):

        return GCanvas(
            SetValue, BColor, xStretch, yStretch, Visible, border, Size, EmptySpace,
            tooltip=tooltip, rclickMenu=rclickMenu, metadata=metadata,
        )
    """
    2D oyun / sahne (Raylib-benzeri GCanvas API):
    - Sahne nesneleri: BeginScene2D / DrawRectangle / DrawCircle / DrawLine / DrawText / DrawRectanglePro
    - Toplu: LoadSceneBatch([{'kind':'rectangle','name':'p','x':0,'y':0,'w':40,'h':40,'fill':'teal'}, ...])
    - Secim: PickSceneObject(px,py), SelectSceneObject(name), SelectedSceneObjects(), MoveSceneObject(name,dx,dy)
    - Temizlik: ClearScene2D() veya UnloadSceneObject(name)
    - Tus (Raylib): cv.EnableSceneInput(); Update icinde cv.InputBeginFrame() sonra cv.IsKeyDown("w")
    - Ham tk: erase(), after_ms, kisa read timeout

    self.Layout = [[self.GCanvas(SetValue="cv", Size=(48, 24), xStretch=True, yStretch=True)]]
    self.GWindow(...)
    cv = self.GetWindow["cv"]
    with cv.BeginScene2D():
        cv.DrawRectangle("zemin", 0, 0, 400, 300, fill="#1a1a2e", outline="")
        cv.DrawCircle("oyuncu", 100, 80, 12, fill="orange")
    cv.EnableSceneInput()
    # Secim ornegi (tik canvas'ta odak icin EnableSceneInput ile cakisirsa click_to_focus=False kullanin):
    # cv.bind_canvas("<Button-1>", lambda e: cv.SelectSceneObject(cv.PickSceneObject(e.x, e.y)))
    """

    # window widgets
    def GFrame(
            self, GFText=None, InsideWindowLayout=[[]], SetValue=None, InfoWindow=None, Border=1, TFont="Sans, 20", Size=(None, None), 
            xStretch=False, yStretch=False, xStretch_weight=None, yStretch_weight=None, yStretch_row_weight=None, EmptySpace=(None, None), TColor=None, BColor=None, Visible=True
        ): 
        
        return Frame(
            title=GFText, layout=InsideWindowLayout, key=SetValue, border_width=Border, tooltip=InfoWindow, font=TFont, size=Size, pad=EmptySpace, 
            expand_x=xStretch, expand_y=yStretch, expand_weight_x=xStretch_weight, expand_weight_y=yStretch_weight, expand_weight_row=yStretch_row_weight, title_color=TColor, background_color=BColor, visible=Visible 
        )
    
    #self.GC.GText(SetText="   ") -> make space is fine for GFrame
    
    """
    gMenu = [ ["Info", ["GnuChanOS", "Youtube Channel", "Github Page"]], ["System", ["Exit"]] ]
    defaultFont = "Sans, 20"
    c = GColors()

    test1 = [
            [gc.GMenuForTheme(WinMENU_List=gMenu, TFont=defaultFont, TColor=c.black, BColor=c.red1)],
            [gc.GText(SetText="Text 1", xStretch=True, TPosition="center")]
        ]

    test2 = [
            [gc.GMenuForTheme(WinMENU_List=gMenu, TFont=defaultFont, TColor=c.black, BColor=c.red1)],
            [gc.GText(SetText="Text 2", xStretch=True, TPosition="center")]
        ]

    test3 = [
            [gc.GMenuForTheme(WinMENU_List=gMenu, TFont=defaultFont, TColor=c.black, BColor=c.red1)],
            [gc.GText(SetText="Text 3", xStretch=True, TPosition="center")]
        ]

    test4 = [
            [gc.GMenuForTheme(WinMENU_List=gMenu, TFont=defaultFont, TColor=c.black, BColor=c.red1)],
            [gc.GText(SetText="Text ", xStretch=True, TPosition="center")]
        ]

    layout = [
            [
                gc.GFrame(InsideWindowLayout=test1, SetValue="test1", xStretch=True, yStretch=True, BColor=c.blue1, Border=2),
                gc.GFrame(InsideWindowLayout=test2, SetValue="test2", xStretch=True, yStretch=True, BColor=c.blue1, Border=2)
            ],
            [
                gc.GFrame(InsideWindowLayout=test3, SetValue="test3", xStretch=True, yStretch=True, BColor=c.blue1, Border=2),
                gc.GFrame(InsideWindowLayout=test4, SetValue="test4", xStretch=True, yStretch=True, BColor=c.blue1, Border=2)
            ]
        ]

    gc.GWindow(SetMainWindowLayout_List=layout)
    """

    def GColumn(self, winColumnLayout_List=None, Size=(None, None), xStretch=None, yStretch=None, xStretch_weight=None, yStretch_weight=None, yStretch_row_weight=None, EmptySpace=(None, None), Visible=True, SetValue=None, BColor=None):
        return Column(
            layout=winColumnLayout_List, key=SetValue, size=Size, expand_x=xStretch, expand_y=yStretch, expand_weight_x=xStretch_weight, expand_weight_y=yStretch_weight, expand_weight_row=yStretch_row_weight, pad=EmptySpace, visible=Visible, background_color=BColor
        )
        """
        c = GColors()
        TopLayer = [
                    [gc.GText(SetText="Top Layer",    TPosition="center", TFont="Sans, 20",    BColor=c.blue1, xStretch=True, yStretch=True, EmptySpace=(0,0))]
                ]

        MiddleLeftLayer = [
                    [gc.GText(SetText="Middle Left",  TPosition="center", TFont="Sans, 20",  BColor=c.pink1, xStretch=True, yStretch=True, EmptySpace=(0,0))]
                ]

        MiddleRightLayer = [
                    [gc.GText(SetText="Middle Right", TPosition="center", TFont="Sans, 20", BColor=c.purple1, xStretch=True, yStretch=True, EmptySpace=(0,0))]
                ]

        BottomLayer = [
                    [gc.GText(SetText="Bottom Layer", TPosition="center", TFont="Sans, 20", BColor=c.pink8, xStretch=True, yStretch=True, EmptySpace=(0,0))]
                ]

        layout = [
                    [gc.GColumn(winColumnLayout_List=TopLayer, xStretch=True, yStretch=True)],
                    [gc.GColumn(winColumnLayout_List=MiddleLeftLayer, xStretch=True, yStretch=True), gc.GColumn(winColumnLayout_List=MiddleRightLayer, xStretch=True, yStretch=True)],
                    [gc.GColumn(winColumnLayout_List=BottomLayer, xStretch=True, yStretch=True)] 
                ]
        gc.GWindow(SetMainWindowLayout_List=layout)

        """

    # create Gtab and create GTap Group
    def GTabGroup(
            self, TabGroupLayout=None, SetValue=None, TFont="Sans, 20",
            BColor=None, TBColor=GnuChanOSColor().SColors3, TColor=None, STColor=GnuChanOSColor().TColor, SBColor=GnuChanOSColor().SColors0, Size=(None, None), TBorder=0, Border=0,
            xStretch_weight=None, yStretch_weight=None, yStretch_row_weight=None
        ): 
        
        return TabGroup(
            layout=TabGroupLayout, key=SetValue, expand_x=True, expand_y=True, expand_weight_x=xStretch_weight, expand_weight_y=yStretch_weight, expand_weight_row=yStretch_row_weight, size=Size,
            background_color=BColor, selected_background_color=SBColor, tab_background_color=TBColor, enable_events=True,
            title_color=TColor, selected_title_color=STColor, font=TFont, tab_border_width=TBorder, border_width=Border
        )
    def GTab(
            self, Text, TabLayout=None, SetValue=None, rclickMenu=None, Position="center", TColor=None, BColor=None, Border=0
        ): 
        
        return Tab(
            title=Text, layout=TabLayout, key=SetValue, right_click_menu=rclickMenu, element_justification=Position,
            title_color=TColor, background_color=BColor, border_width=Border
        )
        """
        c = GColors()

        tab1 = [
                [gc.GText(SetText="Top Layer",    TPosition="center", TFont="Sans, 20",    BColor=c.blue1, xStretch=True, yStretch=True, EmptySpace=(0,0))]
            ]

        tab2 = [
                [gc.GText(SetText="Middle Left",  TPosition="center", TFont="Sans, 20",  BColor=c.pink1, xStretch=True, yStretch=True, EmptySpace=(0,0))]
            ]

        layout = [
                [gc.GTabGroup(TabGroupLayout=[
                    [gc.GTab(Text="test1", TabLayout=tab1, SetValue="tab1")],
                    [gc.GTab(Text="test2", TabLayout=tab2, SetValue="tab2")],
                ], SetValue="tabG")]
            ]
        """

# All Widgets
    # text widget
    def GText(
            self, SetText="", TFont="Sans, 20", SetValue=None, Size=(None, None), TPosition="left", 
            xStretch=False, yStretch=False, xStretch_weight=None, yStretch_weight=None, yStretch_row_weight=None, EmptySpace=(None), TColor=None, BColor=None, border=None 
        ): 
        
        return Text(text=SetText, font=TFont, key=SetValue, size=Size, justification=TPosition, expand_x=xStretch, expand_y=yStretch, expand_weight_x=xStretch_weight, expand_weight_y=yStretch_weight, expand_weight_row=yStretch_row_weight, pad=EmptySpace, 
            text_color=TColor, background_color=BColor, border_width=border
        )
        """
        gc.GText(SetText="text")
        gc.GetWindow["text"].update("change text")
        """

    # button widget
    def GButton(
            self, Text="", bImage=None, TFont="Sans, 20", SetValue=None, Size=(None, None), 
            Visible=True, tcolor=None, bcolor=None, xStretch=False, yStretch=False, EmptySpace=(None), Border=None 
        ): 
        
        return Button(
                Text, button_color=(bcolor, tcolor), font=TFont, key=SetValue, size=Size, 
                expand_x=xStretch, expand_y=yStretch, pad=EmptySpace, image_filename=bImage, visible=Visible, border_width=Border
        )
        """
        layout = [
            [gc.GText(SetText="Default Text", TextValue="text", TPosition="center", xStretch=True)],
            [gc.GButton(Text="This Button", SetValue="button", Border=1)]
            ]

        gc.GWindow(SetMainWindowLayout_List=layout)
        """

    # listbox widget
    def GListBox(
            self, list=[], LFont="Sans, 20", SetValue=None, Size=(None, None), ActiveEvent=True, Visible=True, 
            LPosition="left", EmptySpace=(None, None), noScroolBar=False, xStretch=False, yStretch=False, TColor=None, BColor=None
        ):

        return Listbox(
            list, font=LFont, key=SetValue, enable_events=ActiveEvent, visible=Visible, justification=LPosition, size=Size, pad=EmptySpace,
            no_scrollbar=noScroolBar, expand_x=xStretch, expand_y=yStretch, text_color=TColor, background_color=BColor
        )
        """
        layout = [
            [gc.GListBox(list=(1,2,3,4,5), xStretch=True, yStretch=True, SetValue="List")],
            [gc.GText(SetText="Press Button", TextValue="text", xStretch=True, TPosition="center")],
            [gc.GButton(Text="Press")]
            ]

        gc.GWindow(SetMainWindowLayout_List=layout)

        def update():
            if gc.GetEvent == "Press":
                gc.GetWindow["text"].update(gc.GetValues["List"])
            """

    def GTable(
            self, TableLists:list=[], SetValue: str = None, CollonsPosition: str = None, TPosition: str = "left", TFont: str = "Sans, 20", Visible: bool = True,
            xStretch: bool = False, yStretch: bool = False, TColor: str = None, BColor: str = None,
            VisibleRows: int = 10, 
               ):

        return Table(
            values=TableLists, key=SetValue, cols_justification=CollonsPosition, justification=TPosition, font=TFont, visible=Visible, enable_events=True,
            num_rows=VisibleRows,
        )
        """
        rows = [
            [ "Elma",  "12", "Stok" ],
            [ "Armut", "5",  "Stok" ],
            [ "Uzum",  "0",  "Tukendi" ],
        ]
        layout = [
            [gc.GTable(TableLists=rows, SetValue="tbl", VisibleRows=5, xStretch=True)],
            [gc.GButton(Text="Secimi goster", SetValue="btn")],
        ]

        gc.GWindow(SetMainWindowLayout_List=layout)

        def update():
            if gc.GetEvent == "btn":
                print(gc.GetValues.get("tbl"))
        """

    # input widget
    def GInput (
            self, InText="", TFont="Sans, 20", SetValue=None, Size=(None, None), Focus=True, TPosition="left", Visible=True, 
            HidePassword=False, ReadOnly=False, xStretch=False, yStretch=False, EmptySpace=(None), TColor=None, BColor=None, Border=None
        ):

        return Input(
                default_text=InText, font=TFont, key=SetValue, size=Size, focus=Focus, justification=TPosition,  pad=EmptySpace, expand_x=xStretch, 
                expand_y=yStretch, password_char=HidePassword, visible=Visible, readonly=ReadOnly, text_color=TColor, background_color=BColor, border_width=Border
        )
        """
        layout = [
            [gc.GInput(InText="Write Something", SetValue="input", xStretch=True)],
            [gc.GText(SetText="Press Button", TextValue="text", xStretch=True, TPosition="center")],
            [gc.GButton(Text="Press")]
        ]

        gc.GWindow(SetMainWindowLayout_List=layout)

        def update():
            if gc.GetEvent == "Press":
                gc.GetWindow["text"].update(gc.GetValues["input"])
        """

    # multiLine widget
    def GMultiline (
            self, InText="", TFont=None, SetValue=None, Size=(None, None), Visible=True, TPosition="left", EnableEvent=True, WriteOnly=False, WrapLines=True,
            xStretch=False, yStretch=False, xStretch_weight=None, yStretch_weight=None, yStretch_row_weight=None, Focus=True, ReadOnly=False, NoScroolBar=True, EmptySpace=(None, None), TColor=None, BColor=None
        ):

        return Multiline(
                default_text=InText, font=TFont, key=SetValue, size=Size, focus=Focus, justification=TPosition, visible=Visible, disabled=ReadOnly, 
                expand_x=xStretch, expand_y=yStretch, expand_weight_x=xStretch_weight, expand_weight_y=yStretch_weight, expand_weight_row=yStretch_row_weight, no_scrollbar=NoScroolBar, text_color=TColor, background_color=BColor, pad=EmptySpace, border_width=0,
                autoscroll=True, auto_size_text=True, enable_events=EnableEvent, write_only=WriteOnly, wrap_lines=WrapLines
        )
        """
        layout = [
            [gc.GMultiline(InText="Write Something", SetValue="input", xStretch=True, yStretch=True)],
            [gc.GText(SetText="Press Button", SetValue="text", xStretch=True, TPosition="center")],
            [gc.GButton(Text="Press")]
        ]

        gc.GWindow(SetMainWindowLayout_List=layout)
        """
    
    # cheack mark
    def GCheackBox(self, CText: str=None, TFont: str="Sans, 20", SetValue: str=None, EmptySpace: tuple=(None, None), TColor: str=None, BColor: str=None, Checked: bool = True):
        return Checkbox(text=CText, font=TFont, key=SetValue, pad=EmptySpace, text_color=TColor, background_color=BColor, default=Checked)
        """
        layout = [
            [
                gc.GCheackBox(tiCTexttle="Half Life1", SetValue="hl1"),
                gc.GCheackBox(CText="Half Life2", SetValue="hl2"),
                gc.GCheackBox(CText="Half Life3", SetValue="hl3"),
            ],
            [gc.GText(SetText="Default", xStretch=True, SetValue="text")],
            [gc.GButton(Text="CheckBox", xStretch=True, )]
        ]

        gc.GWindow(SetMainWindowLayout_List=layout)

        def update():
            if gc.GetEvent == "CheckBox":
                if gc.GetValues["hl1"]:
                    gc.GetWindow["text"].update("half life 1")
                if gc.GetValues["hl2"]:
                    gc.GetWindow["text"].update("half life 2")
                if gc.GetValues["hl3"]:
                    gc.GetWindow["text"].update("half life 3 ?????")
        """

    GCheckBox = GCheackBox

    def GRadio(self, RText=None, TFont="Sans, 20", defaultSelect=False, groupID=None, SetValue=None, CEvent=True, EmptySpace=(None, None), TColor=None, BColor=None):
        return Radio(text=RText, font=TFont, group_id=groupID, key=SetValue, enable_events=CEvent, pad=EmptySpace, text_color=TColor, background_color=BColor, default=defaultSelect)
        """
        layout = [
            [
                gc.GRadio(RText="Half Life 1", groupID="VALVE", SetValue="hl1"),
                gc.GRadio(RText="Half Life 2", groupID="VALVE", SetValue="hl2"),
                gc.GRadio(RText="Half Life 3", groupID="VALVE", SetValue="hl3"),
            ],
            [gc.GText(SetText="Default", xStretch=True, TextValue="text")],
            [gc.GButton(Text="Press HERE!", xStretch=True, SetValue="button")]
        ]

        gc.GWindow(SetMainWindowLayout_List=layout)

        def update():
            if gc.GetEvent in ["hl1", "hl2", "hl3"]:
                if gc.GetEvent == "hl1":
                    gc.GetWindow["text"].update("can you play half life 1 before ?")
                elif gc.GetEvent == "hl2":
                    gc.GetWindow["text"].update("half life 2 good game")
                elif gc.GetEvent == "hl3":
                    gc.GetWindow["text"].update("there is no half life 3 :(")
        """

    # selections
    def GSelection(
        self, TFont="Sans, 20", ListValues=None, DefaultValue=None, SetValue=None, EmptySpace=(None, None), Visible=True, 
        TColor=None, BColor=None, xStretch=False, yStretch=False
        ):

        return Combo(
                values=ListValues, key=SetValue, default_value=DefaultValue, font=TFont, pad=EmptySpace, visible=Visible, text_color=TColor, background_color=BColor, 
                expand_x=xStretch, expand_y=yStretch, readonly=True
        )
        """
        layout = [
            [gc.GSelection(ListValues=[1,2,3,4,5], SetValue="GSelection", DefaultValue=1, Font=gc.font, xStretch=True)],
            [gc.GText(SetText="Default", xStretch=True, TextValue="text")],
            [gc.GButton(Text="Press HERE!", xStretch=True, SetValue="button")]
        ]

        gc.GWindow(SetMainWindowLayout_List=layout)

        def update():
            if gc.GetEvent == "button":
                gc.GetWindow["text"].update(gc.GetValues["GSelection"])
        """
    
    def GIncreaseSelection(
        self, ListValues=None, StartValue=None, SetValue=None, TFont="Sans, 20", Size=(None, None), EmptySpace=(None, None), 
        TColor=None, BColor=None, xStretch=False, yStretch=False, Visible=True
        ):

        return Spin(
                values=ListValues, initial_value=StartValue, font=TFont, key=SetValue, size=Size, pad=EmptySpace, expand_x=xStretch, expand_y=yStretch, 
                text_color=TColor, background_color=BColor, visible=Visible
        )
        """
        layout = [
            [gc.GIncreaseSelection(StartValue=1, ListValues=[1,2,3,4,5], SetValue="GIncreaseSelection", TFont=gc.font, xStretch=True)],
            [gc.GText(SetText="Default", xStretch=True, TextValue="text")],
            [gc.GButton(Text="Press HERE!", xStretch=True, SetValue="button")]
        ]

        gc.GWindow(SetMainWindowLayout_List=layout)
        gc.AddNewBorderWithColor(SetValue="GIncreaseSelection", Color="red", BorderSize=1)

        def update():
            if gc.GetEvent == "button":
                gc.GetWindow["text"].update(gc.GetValues["GIncreaseSelection"])
        """
    
    def GSlider(
            self, MaxRange=None, SetValue=None, DefaultValue=None, TFont="Sans, 20", Size=(None, None), SDirection="h", EmptySpace=(None, None), 
            TColor=None, BColor=None, xStretch=True, Visible=True
        ):

        return Slider(
                range=MaxRange, key=SetValue, default_value=DefaultValue, orientation=SDirection, font=TFont, size=Size, pad=EmptySpace, 
                text_color=TColor, background_color=BColor, expand_x=xStretch, visible=Visible
        )
        """
        layout = [
            [gc.GSlider(MaxRange=(0, 100), DefaultValue=20, SDirection="h", SetValue="slider", xStretch=True)],
            [gc.GText(SetText="Slider degeri", TextValue="text", xStretch=True, TPosition="center")],
            [gc.GButton(Text="Oku", xStretch=True, SetValue="button")]
        ]

        gc.GWindow(SetMainWindowLayout_List=layout)

        def update():
            if gc.GetEvent == "button":
                gc.GetWindow["text"].update(str(gc.GetValues["slider"]))
        """

    def GProgressBar(self, MaxRange=None, SetValue=None, Visible=True, PDirection="h", xStretch=True):
        return ProgressBar(max_value=MaxRange, key=SetValue, visible=Visible, orientation=PDirection, expand_x=xStretch)
        """
        layout = [
            [gc.GSlider(MaxRange=(0, 100), DefaultValue=20, SDirection="h", SetValue="slider")],
            [gc.GProgressBar(MaxRange=100, SetValue="pro", PDirection="h")],
            [gc.GText(SetText="Default", xStretch=True, TextValue="text")],
            [gc.GButton(Text="Press HERE!", xStretch=True, SetValue="button")]
        ]

        gc.GWindow(SetMainWindowLayout_List=layout)

        def update():
            if gc.GetEvent == "button":
                gc.GetWindow["text"].update(gc.GetValues["slider"])
            if gc.GetValues["slider"]:
                gc.GetWindow["pro"].update(gc.GetValues["slider"])
        """

    def GImage(
            self, SetValue=None, filename=None, data=None, source=None, Size=(None, None), EmptySpace=(None, None),
            BColor=None, subsample=None, zoom=None, rclickMenu=None, xStretch=False, yStretch=False, Visible=True,
            ActiveEvent=False,
        ):
        return Image(
            source=source, filename=filename, data=data, background_color=BColor, size=Size, pad=EmptySpace,
            key=SetValue, subsample=subsample, zoom=zoom, right_click_menu=rclickMenu,
            expand_x=xStretch, expand_y=yStretch, visible=Visible, enable_events=ActiveEvent,
        )
        """
        # Dosya yolu (paket yanindaki logo.png gibi) veya data= ile ham / base64 goruntu
        layout = [
            [gc.GImage(SetValue="pic", filename="logo.png", xStretch=True)],
            [gc.GButton(Text="Yenile", SetValue="btn")]
        ]

        gc.GWindow(SetMainWindowLayout_List=layout)
        """

    def GGraph(
            self, SetValue, canvas_size, graph_bottom_left, graph_top_right, BColor=None, EmptySpace=(None, None),
            enable_events=False, drag_submits=False, motion_events=False, rclickMenu=None,
            xStretch=False, yStretch=False, Visible=True, float_values=False, border_width=0,
        ):
        return Graph(
            canvas_size, graph_bottom_left, graph_top_right,
            background_color=BColor, pad=EmptySpace, enable_events=enable_events,
            drag_submits=drag_submits, motion_events=motion_events, key=SetValue,
            right_click_menu=rclickMenu, expand_x=xStretch, expand_y=yStretch,
            visible=Visible, float_values=float_values, border_width=border_width,
        )
        """
        layout = [
            [gc.GGraph(
                "graf", (400, 200), (0, 0), (200, 100),
                enable_events=False, xStretch=True, yStretch=True,
            )],
            [gc.GButton(Text="Cizgi ciz", SetValue="btn")]
        ]

        gc.GWindow(SetMainWindowLayout_List=layout)

        def update():
            if gc.GetEvent == "btn":
                gc.GetWindow["graf"].erase()
                gc.GetWindow["graf"].draw_line((10, 10), (180, 90), color="steel blue", width=3)
        """

    def GOutput(
            self, SetValue=None, Size=(None, None), EmptySpace=(None, None), BColor=None, TColor=None,
            xStretch=False, yStretch=False, Visible=True, rclickMenu=None, wrap_lines=None, horizontal_scroll=None,
        ):
        return Output(
            size=Size, pad=EmptySpace, background_color=BColor, text_color=TColor, key=SetValue,
            right_click_menu=rclickMenu, expand_x=xStretch, expand_y=yStretch, visible=Visible,
            wrap_lines=wrap_lines, horizontal_scroll=horizontal_scroll,
        )
        """
        # stdout / stderr bu alana yonlenir; finalize sonrasi print kullanin
        layout = [
            [gc.GOutput(SetValue="out", Size=(70, 12), xStretch=True, yStretch=True)],
            [gc.GButton(Text="print dene", SetValue="btn")]
        ]

        gc.GWindow(SetMainWindowLayout_List=layout)

        def update():
            if gc.GetEvent == "btn":
                print("Merhaba Output")
        """

    def GPane(
            self, PaneColumns, SetValue=None, BColor=None, Size=(None, None), EmptySpace=(None, None),
            Orientation="vertical", show_handle=True, relief=None, handle_size=None, Border=None,
            xStretch=None, yStretch=None, Visible=True,
        ):
        pane_kw = dict(
            pane_list=PaneColumns,
            background_color=BColor,
            size=Size,
            pad=EmptySpace,
            orientation=Orientation,
            show_handle=show_handle,
            handle_size=handle_size,
            border_width=Border,
            key=SetValue,
            expand_x=xStretch,
            expand_y=yStretch,
            visible=Visible,
        )
        if relief is not None:
            pane_kw["relief"] = relief
        return Pane(**pane_kw)
        """
        sol = gc.GColumn([[gc.GText(SetText="Sol panel", xStretch=True)]], xStretch=True, yStretch=True)
        sag = gc.GColumn([[gc.GText(SetText="Sag panel", xStretch=True)]], xStretch=True, yStretch=True)
        layout = [
            [gc.GPane(
                PaneColumns=[sol, sag],
                Orientation="horizontal",
                SetValue="pane",
                xStretch=True,
                yStretch=True,
                Size=(None, 12),
            )]
        ]

        gc.GWindow(SetMainWindowLayout_List=layout)
        """

    def GTree(
            self, TreeDATA=None, headings=None, SetValue=None, TFont="Sans, 20", Visible=True,
            xStretch=False, yStretch=False, EmptySpace=(None, None), TColor=None, BColor=None,
            ActiveEvent=True, num_rows=10, tree_kwargs=None,
        ):
        kw = dict(
            data=TreeDATA,
            headings=headings,
            key=SetValue,
            font=TFont,
            visible=Visible,
            pad=EmptySpace,
            text_color=TColor,
            background_color=BColor,
            enable_events=ActiveEvent,
            num_rows=num_rows,
            expand_x=xStretch,
            expand_y=yStretch,
        )
        if tree_kwargs:
            kw.update(tree_kwargs)
        return Tree(**kw)
        """
        td = gc.GTreeData()
        td.insert("", "n1", "Klasor", ["Aciklama A", "Deger 1"])
        td.insert("n1", "n2", "Alt oge", ["Aciklama B", "Deger 2"])

        layout = [
            [gc.GTree(
                TreeDATA=td,
                headings=["Aciklama", "Deger"],
                SetValue="tree",
                xStretch=True,
                yStretch=True,
                num_rows=8,
            )],
            [gc.GButton(Text="Secimi oku", SetValue="btn")],
        ]

        gc.GWindow(SetMainWindowLayout_List=layout)

        def update():
            if gc.GetEvent == "btn":
                print(gc.GetValues.get("tree"))
        """

    def GTreeData(self):
        return TreeData()
        """
        td = gc.GTreeData()
        td.insert("", "anahtar1", "Gorunen metin", ["kolon1", "kolon2"])
        td.insert("anahtar1", "anahtar2", "Cocuk", ["a", "b"])
        # td nesnesini gc.GTree(TreeDATA=td, headings=[...], ...) ile kullanin
        """

    def GOptionMenu(
            self, ListValues, DefaultValue=None, SetValue=None, TFont="Sans, 20", Size=(None, None),
            EmptySpace=(None, None), Visible=True, Disabled=False, TColor=None, BColor=None,
            xStretch=False, yStretch=False,
        ):
        return OptionMenu(
            ListValues,
            default_value=DefaultValue,
            key=SetValue,
            font=TFont,
            size=Size,
            pad=EmptySpace,
            visible=Visible,
            disabled=Disabled,
            text_color=TColor,
            background_color=BColor,
            expand_x=xStretch,
            expand_y=yStretch,
        )
        """
        layout = [
            [gc.GOptionMenu([ "Bir", "Iki", "Uc" ], DefaultValue="Bir", SetValue="opt", xStretch=True)],
            [gc.GText(SetText="Secim", TextValue="lbl", xStretch=True, TPosition="center")],
            [gc.GButton(Text="Goster", SetValue="btn")],
        ]

        gc.GWindow(SetMainWindowLayout_List=layout)

        def update():
            if gc.GetEvent == "btn":
                gc.GetWindow["lbl"].update(str(gc.GetValues["opt"]))
        """

    def GStatusBar(
            self, SetText="", SetValue=None, TFont="Sans, 20", Size=(None, None), EmptySpace=(None, None),
            TColor=None, BColor=None, TPosition="left", ActiveEvent=False, Visible=True,
            xStretch=False, yStretch=False, rclickMenu=None, relief=None,
        ):
        sb_kw = dict(
            text=SetText,
            size=Size,
            font=TFont,
            key=SetValue,
            pad=EmptySpace,
            text_color=TColor,
            background_color=BColor,
            justification=TPosition,
            enable_events=ActiveEvent,
            visible=Visible,
            expand_x=xStretch,
            expand_y=yStretch,
            right_click_menu=rclickMenu,
        )
        if relief is not None:
            sb_kw["relief"] = relief
        return StatusBar(**sb_kw)
        """
        layout = [
            [gc.GText(SetText="Ust", xStretch=True)],
            [gc.GStatusBar(SetText="Hazir", SetValue="sb", xStretch=True)],
            [gc.GButton(Text="Durumu guncelle", SetValue="btn")],
        ]

        gc.GWindow(SetMainWindowLayout_List=layout)

        def update():
            if gc.GetEvent == "btn":
                gc.GetWindow["sb"].update("Guncellendi: " + str(int(time.time()))[-4:])
        """

    def GButtonMenu(
            self, Text, menu_def, SetValue=None, TFont="Sans, 20", EmptySpace=(None, None),
            tcolor=None, bcolor=None, Disabled=False, Visible=True, xStretch=False, yStretch=False,
            tearoff=False, Border=None, tooltip=None, bImage=None,
        ):
        return ButtonMenu(
            Text,
            menu_def,
            key=SetValue,
            font=TFont,
            pad=EmptySpace,
            text_color=tcolor,
            background_color=bcolor,
            disabled=Disabled,
            visible=Visible,
            expand_x=xStretch,
            expand_y=yStretch,
            tearoff=tearoff,
            border_width=Border,
            tooltip=tooltip,
            image_filename=bImage,
        )
        """
        menu_def = [ "Menu", [ "Dosya Ac", "Kaydet", "---", "Cikis" ] ]
        layout = [
            [gc.GButtonMenu("Islemler", menu_def, SetValue="bmenu", xStretch=False)],
            [gc.GText(SetText="Son secilen menu ogesi", TextValue="lbl", xStretch=True)],
        ]

        gc.GWindow(SetMainWindowLayout_List=layout)

        def update():
            ev = gc.GetEvent
            if ev in ("Dosya Ac", "Kaydet", "Cikis"):
                gc.GetWindow["lbl"].update(ev)
        """

    def GSizegrip(self, SetValue=None, BColor=None, EmptySpace=None):
        if EmptySpace is None:
            EmptySpace = (0, 0)
        return Sizegrip(background_color=BColor, pad=EmptySpace, key=SetValue)
        """
        # Pencereyi GnuChanGUI(..., resizable=True) ile acin; fare ile yeniden boyutlandirma sag-alt tutamac
        layout = [
            [gc.GText(SetText="Icerik", xStretch=True, yStretch=True)],
            [gc.GPush(), gc.GSizegrip()],
        ]

        gc.GWindow(SetMainWindowLayout_List=layout)
        """

    # this is can change in the future
    def GetFilePath(
        self, defaultPATH=str(os.path.expanduser("~")), message="", title="", noWindow=True, noTitleBar=False, fileTypes=[("All files (*.*)", "*.*")],
        bcolor=GnuChanOSColor().FColors1, buttonColor = GnuChanOSColor().FColors3, showHidden=True,
        ):

        return popup_get_file(
            default_path=defaultPATH, message=message,  no_window=noWindow, file_types=fileTypes, no_titlebar=noTitleBar, title=title,
            button_color=buttonColor, background_color=bcolor, show_hidden=showHidden,
        )

    def GetFileForSave(
        self, defaultPATH=str(os.path.expanduser("~")), message="", title="", noWindow=True, noTitleBar=False, fileTypes=[("All files (*.*)", "*.*")],
        bcolor=GnuChanOSColor().FColors1, buttonColor = GnuChanOSColor().FColors3, showHidden=True,
        ):

        return popup_get_file(
            save_as=True, default_path=defaultPATH, message=message,  no_window=noWindow, file_types=fileTypes, no_titlebar=noTitleBar, title=title,
            button_color=buttonColor, background_color=bcolor, show_hidden=showHidden,
        )

    def GetFolderPath(
        self, defaultPATH=str(os.path.expanduser("~")), message="", title="", noWindow=True, noTitleBar=False,
        bcolor=GnuChanOSColor().FColors1, buttonColor = GnuChanOSColor().FColors3, showHidden=True,
        ):

        return popup_get_folder(default_path=defaultPATH, message=message,  no_window=noWindow, no_titlebar=noTitleBar, title=title,
                              button_color=buttonColor, background_color=bcolor, show_hidden=showHidden)

    # GFrame, xStretch and yStretch not working with pin
    # GColumn, it's same in here not working xStretch and yStretch
    def GPin(self, GObject, shrink=False):
        return pin(GObject, shrink=shrink)

    # with Property
    def GPush(self, BColor: str = "#240046"):
        return Push(background_color=BColor)

    def GHSep(self, Color: str = "#240046"):
        return HorizontalSeparator(color=Color)

    def GVSep(self, Color: str = "#240046"):
        return VerticalSeparator(color=Color)

    # this is just make short code that's it
    def ReturnGlistboxIndex(self, List: list, GlistboxValue: str):
        return List.index(self.GetValues[GlistboxValue][0])




# Simple Timer
class GTimer:
    def __init__(self) -> None:
        self.Second = 0
        self.Minute = 0
        self.Hour   = 0
        self.StringTime = ''

        self.TimerStarts = False
        self.KillThreads = False

        self.gcT = Thread(target=self.Go, args=[]).start()
        

    def Go(self):
        while True:
            if self.TimerStarts:
                self.StringTime = f"{self.Hour}:{self.Minute}:{self.Second}"
                self.Second += 1
                
                if self.Second == 60:
                    self.Second = 0
                    self.Minute += 1

                if self.Minute == 60:
                    self.Minute = 0
                    self.Hour += 1

                time.sleep(1)
            else:
                self.Second = self.Minute = self.Hour = 0
                self.StringTime = f"{self.Hour}:{self.Minute}:{self.Second}"
                if self.KillThreads:
                    break

# pygame mixer for play sound
class GMixer:
    def __init__(self, SoundFileList: list = [], MaxChannelLimit: int = 5) -> None:
        global pygame
        import pygame.mixer
        self.MaxChannelLimit = MaxChannelLimit
        self.SoundFileList = SoundFileList
        self.SoundIndex = 0
        self.Volume = 1
        self.SoundLength = 0
        self.SoundLength_Backup = 0
        self.PlayAgain = False
        self.GiveLength = False
        self.MusicName = ""

        pygame.mixer.init()
        pygame.mixer.set_num_channels(self.MaxChannelLimit)

    def SinglePlay(self, SoundPath):
        pygame.mixer.music.load(SoundPath)
        pygame.mixer.music.set_volume(self.Volume)
        pygame.mixer.music.play()

        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.unload()
            time.sleep(1)
            return True

    def PlaySound_MultiChannelNoLoop(self,  SoundPath="", ChannelID=0):
        _play = False
        if not _play:
            channel = pygame.mixer.Channel(ChannelID)
            channel.play(pygame.mixer.Sound(SoundPath))
            channel.set_volume(self.Volume)
            _play = True

    def StopSound(self):
        pygame.mixer.music.stop()

    def PlaySound_SingleChannel(self,  SoundPath=""):
        self.SoundIndex = self.SoundFileList.index(SoundPath)
        pygame.mixer.music.load(SoundPath)
        pygame.mixer.music.set_volume(self.Volume)
        pygame.mixer.music.play()
        self.MusicName = SoundPath

    def NextSound_SingleChannel(self):
        try:
            if self.SoundIndex < len(self.SoundFileList) - 1:
                self.SoundIndex += 1
            pygame.mixer.music.load(self.SoundFileList[self.SoundIndex])
            pygame.mixer.music.set_volume(self.Volume)
            pygame.mixer.music.play()
            self.MusicName = self.SoundFileList[self.SoundIndex]
        except Exception as ERR:
            print(ERR, "Next Sound ERR")

    def PreviousSound_SingleChannel(self):
        try:
            if self.SoundIndex > 0:
                self.SoundIndex -= 1
            pygame.mixer.music.load(self.SoundFileList[self.SoundIndex])
            pygame.mixer.music.set_volume(self.Volume)
            pygame.mixer.music.play()
            self.MusicName = self.SoundFileList[self.SoundIndex]
        except Exception as ERR:
            print(ERR, "Previous Sound ERR")

    def VolumeChange_Gslider(self, Volume):
        try:
            VolumeSlider = int(Volume)
            if VolumeSlider != 10:
                self.Volume = float(f"0.{VolumeSlider}")
            else:
                self.Volume = 1
            pygame.mixer.music.set_volume(self.Volume)
        except Exception as ERR:
            print(ERR, "Volume Changer ERR")


# Popup Message Window
class GMessage(GnuChanGUI):
    def __init__(self, 
        WindowTitle="Default Title", WindowText = "Default Text", 
        Size=(800, 600), resizable=False, finalize=True, winPosX=1920 / 2, winPosY=1080 / 2,
        WindowTextFont = "Sans", WindowTextFontSize = 20, 
        WindowTBC = GnuChanOSColor().FColors1, ButtonLBC = GnuChanOSColor().FColors5,
        WindowSize=(700, 300), WindowResizable = False 
    ):

        super().__init__(WindowTitle, Size, resizable, finalize, winPosX, winPosY)


        self.WindowTitle      = WindowTitle
        self.windowText       = WindowText
        self.WindowSize       = WindowSize
        self.WindowResizable  = WindowResizable
        self.TextFont         = f"{WindowTextFont}, {WindowTextFontSize}"
        self.WindowTextBackgroundColor = WindowTBC
        self.ButtonLayoutBackgroundColor = ButtonLBC

        Themecolors().GnuChanOS        # you can change theme color
        self.CGC = GnuChanOSColor()




        # main window layout you can use column and frame in here
        self.Layout = [
            [self.GMultiline(
                InText=self.windowText, TFont=self.TextFont, TPosition="center", 
                xStretch=True, yStretch=True, BColor=self.WindowTextBackgroundColor, ReadOnly=True
            )],
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)


    def Update(self):
        if "Exit" == self.GetEvent:
            self.closeWindow = True

    def BeforeExit(self):
        print(f"{self.WindowTitle} is closed")




class RlSceneObject:
    """
    Sahnedeki tek mantiksal nesne (Raylib tarzinda: isim + sinir kutusu + tk id listesi).
    """

    __slots__ = ("name", "kind", "item_ids", "bbox", "tag", "user_data", "visible")

    def __init__(self, name, kind, item_ids, bbox, tag=None, user_data=None):
        self.name = name
        self.kind = kind
        self.item_ids = list(item_ids)
        self.bbox = bbox
        self.tag = tag
        self.user_data = user_data
        self.visible = True


class GCanvas(Canvas):
    """
    gcLibrary.Canvas alt sinifi + Raylib-benzeri 2D sahne ve tus (yalnizca tk).
    Tus: EnableSceneInput() -> her kare InputBeginFrame(); IsKeyDown / IsKeyPressed / IsKeyReleased.
    Sahne: BeginScene2D, Draw*, PickSceneObject, SelectSceneObject, LoadSceneBatch, ClearScene2D.
    Ham tk: TKCanvas, bind_canvas (ileri duzey), after_ms, pixel_dimensions.
    """

    def __init__(
        self,
        SetValue: str,
        BColor: str = "black",
        xStretch: bool = False,
        yStretch: bool = False,
        Visible: bool = True,
        border: int = 0,
        Size: tuple = (None, None),
        EmptySpace: tuple = (None, None),
        tooltip: str = None,
        rclickMenu=None,
        metadata=None,
    ):
        super().__init__(
            canvas=None,
            background_color=BColor,
            size=Size,
            pad=EmptySpace,
            key=SetValue,
            expand_x=xStretch,
            expand_y=yStretch,
            visible=Visible,
            border_width=border,
            tooltip=tooltip,
            right_click_menu=rclickMenu,
            metadata=metadata,
        )
        self._rl_objects = {}
        self._rl_order = []
        self._rl_item_owner = {}
        self._rl_selection = set()
        self._rl_batch_depth = 0
        # Raylib-benzeri tus (sadece tk; pynput / bind_canvas sart degil)
        self._rl_keys_down = set()
        self._rl_keys_snapshot = frozenset()
        self._rl_pressed_this_frame = frozenset()
        self._rl_released_this_frame = frozenset()
        self._rl_input_installed = False
        self._rl_input_grab_default = True
        self._rl_input_click_focus = True

    # --- Raylib-benzeri sahne etiketi (tk tags) ---
    @staticmethod
    def _rl_canvas_tag(name):
        return "_rlscn_" + str(name).replace(" ", "\u00a0")

    _RL_KEY_ALIAS = {
        "up": "Up",
        "down": "Down",
        "left": "Left",
        "right": "Right",
        "space": "space",
        "return": "Return",
        "escape": "Escape",
        "tab": "Tab",
    }

    @classmethod
    def _canonical_keysym(cls, keysym):
        if not keysym:
            return ""
        s = str(keysym)
        lk = s.lower()
        if lk in cls._RL_KEY_ALIAS:
            return cls._RL_KEY_ALIAS[lk]
        if len(s) == 1 and s.isalpha():
            return s.lower()
        return s

    def _rl_canvas(self):
        c = self.TKCanvas
        if c is None or not self._widget_was_created():
            return None
        return c

    def EnableSceneInput(self, grab_focus=True, click_to_focus=True):
        """
        Canvas tuslarini kutuphane icinde yonetir (tk KeyPress/Release).
        Oyun dongusunde once InputBeginFrame(), sonra IsKeyDown / IsKeyPressed kullanin.
        """
        self._rl_input_grab_default = grab_focus
        self._rl_input_click_focus = click_to_focus
        self._rl_try_install_input()
        if grab_focus:
            self.grab_focus()

    def DisableSceneInput(self):
        """Tk baglarini kaldir (odak/tus takibi durur)."""
        c = self._rl_canvas()
        if c is not None and self._rl_input_installed:
            for seq in ("<KeyPress>", "<KeyRelease>", "<FocusOut>", "<Button-1>"):
                try:
                    c.unbind(seq)
                except Exception:
                    pass
        self._rl_input_installed = False
        self._rl_keys_down.clear()
        self._rl_keys_snapshot = frozenset()
        self._rl_pressed_this_frame = frozenset()
        self._rl_released_this_frame = frozenset()

    def _rl_try_install_input(self):
        if self._rl_input_installed:
            return
        c = self._rl_canvas()
        if c is None:
            return
        c.bind("<KeyPress>", self._rl_on_key_press)
        c.bind("<KeyRelease>", self._rl_on_key_release)
        c.bind("<FocusOut>", self._rl_on_focus_out)
        if self._rl_input_click_focus:
            c.bind("<Button-1>", self._rl_on_click_focus)
        self._rl_input_installed = True

    def _rl_on_key_press(self, event):
        ks = getattr(event, "keysym", None)
        if ks:
            self._rl_keys_down.add(self._canonical_keysym(ks))

    def _rl_on_key_release(self, event):
        ks = getattr(event, "keysym", None)
        if ks:
            self._rl_keys_down.discard(self._canonical_keysym(ks))

    def _rl_on_focus_out(self, event):
        self._rl_keys_down.clear()

    def _rl_on_click_focus(self, event):
        if self._rl_input_grab_default:
            self.grab_focus()

    def InputBeginFrame(self):
        """
        Kare basi cagirin: IsKeyPressed / IsKeyReleased icin kenar bilgisi guncellenir.
        Widget henuz yoksa baglanti bir sonraki karede kurulur.
        """
        self._rl_try_install_input()
        down = set(self._rl_keys_down)
        self._rl_pressed_this_frame = frozenset(down - self._rl_keys_snapshot)
        self._rl_released_this_frame = frozenset(self._rl_keys_snapshot - down)
        self._rl_keys_snapshot = frozenset(down)

    def IsKeyDown(self, key):
        """Raylib IsKeyDown: tus su an basili mi (canvas odakliyken)."""
        return self._canonical_keysym(key) in self._rl_keys_down

    def IsKeyPressed(self, key):
        """Raylib IsKeyPressed: bu karede yeni basildi mi (InputBeginFrame sonrasi)."""
        return self._canonical_keysym(key) in self._rl_pressed_this_frame

    def IsKeyReleased(self, key):
        """Bu karede birakildi mi."""
        return self._canonical_keysym(key) in self._rl_released_this_frame

    def _rl_bbox_union(self, bbox_a, bbox_b):
        if bbox_a is None:
            return bbox_b
        if bbox_b is None:
            return bbox_a
        return (
            min(bbox_a[0], bbox_b[0]),
            min(bbox_a[1], bbox_b[1]),
            max(bbox_a[2], bbox_b[2]),
            max(bbox_a[3], bbox_b[3]),
        )

    def _rl_register(self, name, kind, item_ids, bbox, tag=None, user_data=None, replace=True):
        if replace and name in self._rl_objects:
            self.RemoveSceneObject(name)
        c = self._rl_canvas()
        if c is None:
            return None
        tcanvas = self._rl_canvas_tag(name)
        for iid in item_ids:
            try:
                c.addtag_withtag(tcanvas, iid)
            except Exception:
                pass
            self._rl_item_owner[iid] = name
        obj = RlSceneObject(name, kind, item_ids, bbox, tag=tag, user_data=user_data)
        self._rl_objects[name] = obj
        if name not in self._rl_order:
            self._rl_order.append(name)
        return obj

    @contextmanager
    def BeginScene2D(self):
        """Toplu ekleme / senkron blok (Raylib BeginMode2D hissi); icinde Draw* cagirin."""
        self._rl_batch_depth += 1
        try:
            yield self
        finally:
            self._rl_batch_depth -= 1

    def EndScene2D(self):
        """BeginScene2D ile simetri; with kullanmiyorsaniz batch sonunda cagirin (derinligi azaltir)."""
        if self._rl_batch_depth > 0:
            self._rl_batch_depth -= 1

    def ClearScene2D(self):
        """Sahnedeki tum kayitli nesneleri siler (tk + ic kayit)."""
        for name in list(self._rl_order):
            self.RemoveSceneObject(name)
        self._rl_selection.clear()

    def RemoveSceneObject(self, name):
        """Tek nesneyi sahneden ve canvas'tan kaldir."""
        c = self._rl_canvas()
        tag = self._rl_canvas_tag(name)
        if c is not None:
            try:
                c.delete(tag)
            except Exception:
                pass
        obj = self._rl_objects.pop(name, None)
        if obj is not None:
            for iid in obj.item_ids:
                self._rl_item_owner.pop(iid, None)
        if name in self._rl_order:
            self._rl_order.remove(name)
        self._rl_selection.discard(name)

    def GetSceneObject(self, name):
        return self._rl_objects.get(name)

    def AllSceneObjects(self):
        """Cizim sirasina gore RlSceneObject listesi."""
        return [self._rl_objects[n] for n in self._rl_order if n in self._rl_objects]

    # --- Raylib Draw* benzeri: cizer + sahneye kaydeder ---
    def DrawRectangle(self, name, x, y, rect_w, rect_h, *, tag=None, user_data=None, **kw):
        """rect_w / rect_h: dikdortgen boyutu (tk 'width' cizgi kalinligi **kw ile verilir, isim cakismasin)."""
        c = self._rl_canvas()
        if c is None:
            return None
        ttag = self._rl_canvas_tag(name)
        iid = c.create_rectangle(x, y, x + rect_w, y + rect_h, tags=(ttag,), **kw)
        bbox = (x, y, x + rect_w, y + rect_h)
        return self._rl_register(name, "rectangle", (iid,), bbox, tag=tag, user_data=user_data)

    def DrawCircle(self, name, center_x, center_y, radius, *, tag=None, user_data=None, **kw):
        c = self._rl_canvas()
        if c is None:
            return None
        r = float(radius)
        x1, y1 = center_x - r, center_y - r
        x2, y2 = center_x + r, center_y + r
        ttag = self._rl_canvas_tag(name)
        iid = c.create_oval(x1, y1, x2, y2, tags=(ttag,), **kw)
        bbox = (x1, y1, x2, y2)
        return self._rl_register(name, "circle", (iid,), bbox, tag=tag, user_data=user_data)

    def DrawLine(self, name, x1, y1, x2, y2, *, tag=None, user_data=None, **kw):
        c = self._rl_canvas()
        if c is None:
            return None
        ttag = self._rl_canvas_tag(name)
        iid = c.create_line(x1, y1, x2, y2, tags=(ttag,), **kw)
        bbox = (min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))
        return self._rl_register(name, "line", (iid,), bbox, tag=tag, user_data=user_data)

    def DrawText(self, name, x, y, text, *, tag=None, user_data=None, **kw):
        c = self._rl_canvas()
        if c is None:
            return None
        ttag = self._rl_canvas_tag(name)
        iid = c.create_text(x, y, text=text, tags=(ttag,), **kw)
        try:
            bx1, by1, bx2, by2 = c.bbox(iid)
            bbox = (bx1, by1, bx2, by2)
        except Exception:
            bbox = (x, y, x, y)
        return self._rl_register(name, "text", (iid,), bbox, tag=tag, user_data=user_data)

    def DrawRectanglePro(self, name, x, y, rect_w, rect_h, origin_x, origin_y, rotation_deg, *, tag=None, user_data=None, **kw):
        """
        Dikdortgen + donme (origin gore); tk'da tek polygon ile yaklasim.
        rotation_deg: derece, saat yonu pozitif.
        """
        c = self._rl_canvas()
        if c is None:
            return None
        rad = math.radians(rotation_deg)
        cr, sr = math.cos(rad), math.sin(rad)
        corners = ((0, 0), (rect_w, 0), (rect_w, rect_h), (0, rect_h))
        pts = []
        minx = miny = float("inf")
        maxx = maxy = float("-inf")
        for cx, cy in corners:
            lx, ly = cx - origin_x, cy - origin_y
            wx = x + lx * cr - ly * sr
            wy = y + lx * sr + ly * cr
            pts.extend((wx, wy))
            minx, maxx = min(minx, wx), max(maxx, wx)
            miny, maxy = min(miny, wy), max(maxy, wy)
        ttag = self._rl_canvas_tag(name)
        iid = c.create_polygon(*pts, tags=(ttag,), **kw)
        bbox = (minx, miny, maxx, maxy)
        return self._rl_register(name, "rectangle_pro", (iid,), bbox, tag=tag, user_data=user_data)

    def LoadSceneBatch(self, specs):
        """
        Toplu nesne: her oge sozluk.
        Zorunlu: 'kind' ('rectangle'|'circle'|'line'|'text'|'rectangle_pro'), 'name'.
        Ornek: {'kind':'rectangle','name':'a','x':0,'y':0,'w':32,'h':32,'fill':'gray'}
        """
        out = []
        with self.BeginScene2D():
            for sp in specs:
                kind = sp.get("kind")
                name = sp.get("name")
                if not kind or name is None:
                    continue
                kw = {k: v for k, v in sp.items() if k not in ("kind", "name", "tag", "user_data")}
                tag = sp.get("tag")
                ud = sp.get("user_data")
                if kind == "rectangle":
                    o = self.DrawRectangle(
                        name, kw.pop("x"), kw.pop("y"), kw.pop("w"), kw.pop("h"), tag=tag, user_data=ud, **kw
                    )
                elif kind == "circle":
                    o = self.DrawCircle(
                        name, kw.pop("cx"), kw.pop("cy"), kw.pop("r"), tag=tag, user_data=ud, **kw
                    )
                elif kind == "line":
                    o = self.DrawLine(
                        name, kw.pop("x1"), kw.pop("y1"), kw.pop("x2"), kw.pop("y2"), tag=tag, user_data=ud, **kw
                    )
                elif kind == "text":
                    o = self.DrawText(
                        name, kw.pop("x"), kw.pop("y"), kw.pop("text"), tag=tag, user_data=ud, **kw
                    )
                elif kind == "rectangle_pro":
                    o = self.DrawRectanglePro(
                        name,
                        kw.pop("x"),
                        kw.pop("y"),
                        kw.pop("w"),
                        kw.pop("h"),
                        kw.pop("origin_x", 0),
                        kw.pop("origin_y", 0),
                        kw.pop("rotation_deg", 0),
                        tag=tag,
                        user_data=ud,
                        **kw
                    )
                else:
                    o = None
                if o is not None:
                    out.append(o)
        return out

    # --- Secim / vurus testi (Raylib CheckCollision / GetGesture hissi) ---
    def PickSceneObject(self, px, py):
        """Verilen canvas pikselinde en ustteki sahne nesnesinin adi veya None."""
        c = self._rl_canvas()
        if c is None:
            return None
        try:
            ids = c.find_overlapping(px, py, px, py)
        except Exception:
            return None
        for iid in reversed(ids):
            owner = self._rl_item_owner.get(iid)
            if owner is not None:
                return owner
        return None

    def QuerySceneRect(self, x1, y1, x2, y2):
        """Dikdortgenle kesisen tum sahne nesne isimleri (ustten alta sirali)."""
        c = self._rl_canvas()
        if c is None:
            return []
        xa, xb = (x1, x2) if x1 <= x2 else (x2, x1)
        ya, yb = (y1, y2) if y1 <= y2 else (y2, y1)
        try:
            ids = c.find_overlapping(xa, ya, xb, yb)
        except Exception:
            return []
        seen = set()
        ordered = []
        for iid in reversed(ids):
            owner = self._rl_item_owner.get(iid)
            if owner and owner not in seen:
                seen.add(owner)
                ordered.append(owner)
        return ordered

    def SelectSceneObject(self, name, additive=False):
        """Nesneyi sec; additive False ise onceki secim temizlenir."""
        if not additive:
            self._rl_selection.clear()
        if name in self._rl_objects:
            self._rl_selection.add(name)

    def DeselectAllSceneObjects(self):
        self._rl_selection.clear()

    def ToggleSelectSceneObject(self, name):
        if name in self._rl_selection:
            self._rl_selection.discard(name)
        elif name in self._rl_objects:
            self._rl_selection.add(name)

    def SelectedSceneObjects(self):
        """Secili nesne isimleri (tuple)."""
        return tuple(self._rl_selection)

    def SelectedSceneObjectRefs(self):
        """Secili RlSceneObject listesi."""
        return [self._rl_objects[n] for n in self._rl_selection if n in self._rl_objects]

    def IsSceneObjectSelected(self, name):
        return name in self._rl_selection

    def MoveSceneObject(self, name, dx, dy):
        """Sahne nesnesini piksel ote (tk move)."""
        obj = self._rl_objects.get(name)
        c = self._rl_canvas()
        if obj is None or c is None:
            return
        for iid in obj.item_ids:
            try:
                c.move(iid, dx, dy)
            except Exception:
                pass
        if obj.bbox:
            obj.bbox = (obj.bbox[0] + dx, obj.bbox[1] + dy, obj.bbox[2] + dx, obj.bbox[3] + dy)

    def SetSceneObjectVisible(self, name, visible):
        obj = self._rl_objects.get(name)
        c = self._rl_canvas()
        if obj is None or c is None:
            return
        st = "normal" if visible else "hidden"
        for iid in obj.item_ids:
            try:
                c.itemconfigure(iid, state=st)
            except Exception:
                pass
        obj.visible = bool(visible)

    # RaylibUnload* benzeri kisa isimler
    UnloadSceneObject = RemoveSceneObject
    UnloadAllSceneObjects = ClearScene2D

    def bind_canvas(self, sequence, callback, add=""):
        """Alt tk.Canvas uzerinde bind (Window/Element bind ile karismasin diye ayri isim)."""
        c = self.TKCanvas
        if c is None:
            return
        c.bind(sequence, callback, add=add)

    def unbind_canvas(self, sequence):
        c = self.TKCanvas
        if c is None:
            return
        try:
            c.unbind(sequence)
        except Exception:
            pass

    def after_ms(self, ms, callback):
        """
        Pencere kokunde tk.after(ms, callback). GWindow + finalize sonrasi calisir.
        Donen id ile after_cancel() iptal edin.
        """
        if self.ParentForm is None:
            return None
        root = getattr(self.ParentForm, "TKroot", None)
        if root is None:
            return None
        try:
            return root.after(int(ms), callback)
        except Exception:
            return None

    def after_cancel(self, after_id):
        if after_id is None:
            return
        root = getattr(self.ParentForm, "TKroot", None) if self.ParentForm else None
        if root is None:
            return
        try:
            root.after_cancel(after_id)
        except Exception:
            pass

    def pixel_dimensions(self):
        """Gercek tk canvas genislik/yukseklik (piksel); henuz yoksa (0, 0)."""
        if not self._widget_was_created():
            return (0, 0)
        c = self.TKCanvas
        if c is None:
            return (0, 0)
        try:
            c.update_idletasks()
            return (int(c.winfo_width()), int(c.winfo_height()))
        except Exception:
            return (0, 0)

    def delete_item(self, *item_ids):
        """create_* ile donen bir veya daha cok item id silinir."""
        c = self.TKCanvas
        if c is None:
            return
        for iid in item_ids:
            try:
                c.delete(iid)
            except Exception:
                pass

    def delete_tag(self, tag):
        """Etikete bagli tum ogeler silinir (tk delete tag)."""
        c = self.TKCanvas
        if c is None:
            return
        try:
            c.delete(tag)
        except Exception:
            pass

    grab_focus = Canvas.focus_canvas
