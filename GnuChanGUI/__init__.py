from .gcLibrary import *
from .gcLibrary import __version__

from PIL import Image, ImageTk
import os, random, math
from threading import Thread

# Is Program Running
import psutil as p
import time

# Better Keyboard Event
from pynput import keyboard

import time

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

    def DeltaTime(self):
        now = time.perf_counter()
        delta = now - self.last_time
        self.last_time = now

        if self.FPS > 0:
            frame_duration = 1 / self.FPS
            if delta < frame_duration:
                time.sleep(frame_duration - delta)

        return delta

# Warning You can use this gnu/linux, Windows/Spyware/garbage or mac/spyware
# if you use gnu/linux use GnuChanGUI().num2 == GnuChanGUI().CurrentKey
class GKeyboard:
    def __init__(self) -> None:
        # all keyboard keys
        self.f1 = "F1:67"
        self.f2 = "F2:68"
        self.f3 = "F3:69"
        self.f4 = "F4:70"
        self.f5 = "F5:71"
        self.f6 = "F6:72"
        self.f7 = "F7:73"
        self.f8 = "F8:74"
        self.f9 = "F9:75"
        self.f10 = "F10:76"
        self.f11 = "F11:95"
        self.f12 = "F12:96"

        self._1 = "1:10"
        self._2 = "2:11"
        self._3 = "3:12"
        self._4 = "4:13"
        self._5 = "5:14"
        self._6 = "6:15"
        self._7 = "7:16"
        self._8 = "8:17"
        self._9 = "9:18"
        self._0 = "0:19"

        self.q = "q:24"
        self.w = "w:25"
        self.e = "e:26"
        self.r = "r:27"
        self.t = "t:28"
        self.y = "y:29"
        self.u = "u:30"
        self.o = "o:32"
        self.p = "p:33"
        self.a = "a:38"
        self.s = "s:39"
        self.d = "d:40"
        self.f = "f:41"
        self.g = "g:42"
        self.h = "h:43"
        self.j = "j:44"
        self.k = "k:45"
        self.l = "l:46"
        self.z = "z:52"
        self.x = "x:53"
        self.c = "c:54"
        self.v = "v:55"
        self.b = "b:56"
        self.n = "n:57"
        self.m = "w:58"
        self.i = "i:48"

        self.Super_L = "Super_L:133"
        self.quotedbl = "quotedbl:49"
        self.asterisk = "asterisk:20"
        self.minus = "minus:21"
        self.BackSpace = "BackSpace:22"
        self.Tab = "Tab:23"
        self.idotless = "idotless:31"
        self.gbreve = "gbreve:34"
        self.udiaeresis = "udiaeresis:35"
        self.Caps_Lock = "Caps_Lock:66"
        self.scedilla = "scedilla:47"
        self.comma = "comma:51"
        self.Shift_L = "Shift_L:50"
        self.less = "less:94"
        self.Odiaeresis = "Odiaeresis:59"
        self.Ccedilla = "Ccedilla:60"
        self.period = "period:61"
        self.Shift_R = "Shift_R:62"
        self.Control_L = "Control_L:37"
        self.Alt_L = "Alt_L:64"
        self.space = "space:65"
        self.ISO_Level3_Shift = "ISO_Level3_Shift:108"
        self.Super_R = "Super_R:134"
        self.Menu = "Menu:135"
        self.Control_R = "Control_R:105"
        self.Up = "Up:111"
        self.Left = "Left:113"
        self.Down = "Down:116"
        self.Right = "Right:114"
        self.KP_Delete = "KP_Delete:91"
        self.Delete = "Delete:119"
        self.Insert = "Insert:118"
        self.Home = "Home:110"
        self.End = "End:115"
        self.Next = "Next:117"
        self.Prior = "Prior:112"
        self.Return = "Return:36"

        self.KP_Insert = "KP_Insert:90"
        self.KP_End = "KP_End:87"
        self.KP_Down = "KP_Down:88"
        self.KP_Next = "KP_Next:89"
        self.KP_Enter = "KP_Enter:104"
        self.KP_Add = "KP_Add:86"
        self.KP_Right = "KP_Right:85"
        self.KP_Begin = "KP_Begin:84"
        self.KP_Left = "KP_Left:83"
        self.KP_Home = "KP_Home:79"
        self.KP_Up = "KP_Up:80"
        self.KP_Prior = "KP_Prior:81"
        self.KP_Subtract = "KP_Subtract:82"
        self.KP_Multiply = "KP_Multiply:63"
        self.KP_Divide = "KP_Divide:106"
        self.Num_Lock = "Num_Lock:77"

# Warning You can use this gnu/linux, Windows/Spyware/garbage or mac/spyware
# if you use gnu/linux use GnuChanGUI().num2 == GnuChanGUI().CurrentKey


# Keyboard event / Colors / ready theme and gui class
# Simple timer System works in diffrent thread
# pygame mixer for sound
# simple warning window


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

        # don't remove ),<--)
        self.ImagesType = [("PNG (*.png)", "*.png"), ("JPEG (*.jpg)", "*.jpg")]
        self.VideoTypes = [("MKV (*.mkv)", "*.mkv"), ("MP4 (*.mp4)", "*.mp4")]
        self.MusicTypes = [("MP3 (*.mp3)", "*.mp3")]
        self.AllTypes   = [("All Files (*.*)", "*.*"), ("Linux Files (**)", "**")]

        # f"{gc.PathPythonFile}/music.mp3" or diffrent file
        self.PathPythonFile = os.path.dirname(os.path.abspath(__file__))

        self.num0 = "0:48"
        self.num1 = "1:49"
        self.num2 = "2:50"
        self.num3 = "3:51"
        self.num4 = "4:52"
        self.num5 = "5:53"
        self.num6 = "6:54"
        self.num7 = "7:55"
        self.num8 = "8:56"
        self.num9 = "9:57"

        self.a = "A:97"
        self.b = "B:98"
        self.c = "C:99"
        self.d = "D:100"
        self.e = "E:101"
        self.f = "F:102"
        self.g = "G:103"
        self.h = "H:104"
        self.i = "I:105"
        self.j = "J:106"
        self.k = "K:107"
        self.l = "L:108"
        self.m = "M:109"
        self.n = "N:110"
        self.o = "O:111"
        self.p = "P:112"
        self.q = "Q:113"
        self.r = "R:114"
        self.s = "S:115"
        self.t = "T:116"
        self.u = "U:117"
        self.v = "V:118"
        self.w = "W:119"
        self.x = "X:120"
        self.y = "Y:121"
        self.z = "Z:122"

        self.numpad0 = "0:None"
        self.numpad1 = "1:None"
        self.numpad2 = "2:None"
        self.numpad3 = "3:None"
        self.numpad4 = "4:None"
        self.numpad5 = "<65437>:65437"
        self.numpad6 = "6:None"
        self.numpad7 = "7:None"
        self.numpad8 = "8:None"
        self.numpad9 = "9:None"

        self.kp_add = "Keypad_Plus:65451"
        self.kp_subtract = "Keypad_Minus:65453"
        self.kp_multiply = "Keypad_Multiply:65450"
        self.kp_divide = "Keypad_Divide:65455"
        self.kp_enter = "Keypad_Enter:65421"
        self.kp_decimal = "Keypad_Decimal:65454"

        self.space = "Space:32"
        self.enter = "Enter:65293"
        self.tab = "Tab:65289" 
        self.backspace = "Backspace:65288"
        self.comma = "Comma:44"
        self.period = "Period:46"
        self.slash = "Slash:47"
        self.backslash = "Backslash:92"
        self.semicolon = "Semicolon:59"
        self.quote = "Quote:39"
        self.minus = "Minus:45"
        self.equal = "Equal:61"
        self.left_bracket = "Left_Bracket:91"
        self.right_bracket = "Right_Bracket:93"
        self.grave = "Grave:96"

        self.f1 = "F1:65470"
        self.f2 = "F2:65471"
        self.f3 = "F3:65472"
        self.f4 = "F4:65473"
        self.f5 = "F5:65474"
        self.f6 = "F6:65475"
        self.f7 = "F7:65476"
        self.f8 = "F8:65477"
        self.f9 = "F9:65478"
        self.f10 = "F10:65479"
        self.f11 = "F11:65480"
        self.f12 = "F12:65481"

        self.up = "Up:65362"
        self.down = "Down:65364"
        self.left = "Left:65361"
        self.right = "Right:65363"

        self.ctrl_l = "Ctrl_L:65507"
        self.ctrl_r = "Ctrl_R:65508"
        self.alt_l = "Alt_L:65513"
        self.alt_r = "Alt_R:65514"
        self.shift_l = "Shift_L:65505"
        self.shift_r = "Shift_R:65506"
        self.caps_lock = "Caps_Lock:65509"
        self.esc = "Esc:65307"
        self.delete = "Delete:65535"
        self.home = "Home:65360"
        self.end = "End:65367"
        self.page_up = "Page_Up:65365"
        self.page_down = "Page_Down:65366"
        self.num_lock = "Num_Lock:65407"
        self.print_screen = "Print_Screen:65377"
        self.pause = "Pause:65299"

        self.media_play_pause = "Media_Play_Pause:179"
        self.media_volume_mute = "Media_Volume_Mute:173"
        self.media_volume_up = "Media_Volume_Up:175"
        self.media_volume_down = "Media_Volume_Down:174"
        self.media_previous = "Media_Previous:177"
        self.media_next = "Media_Next:176"

        self.CurrentKey = ""
        self.pressing = False

        self.PressTimer = 1
        self.PressWait  = False

        self.Time = GTime()

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
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

    def KeyPressed(self, Key: str):
        if Key == self.CurrentKey and not self.PressWait:
            self.PressWait = True
            return True
        
        if self.PressWait:
            if self.PressTimer > 0:
                self.PressTimer -= 1 * self.Time.DeltaTime()
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
        # this is new for close window good way
        return self.GetWindow
        """
        window have right click menu --> ["menu", ["inMenu1", "inMenu2"]]
        """

    def SetUpdate(self, Update: str = "", exitBEFORE: str = "", TimeOUT: int = 100):
        while True:
            self.GetEvent, self.GetValues = self.GetWindow.read(timeout=TimeOUT)
            if self.GetEvent in (WIN_CLOSED, "Exit"):
                try:
                    if exitBEFORE != "":
                        exitBEFORE()
                except Exception as ERR:
                    print(ERR, "if you do not add extra functions for exitBEFORE. it's in .update()")
                break
            if self.closeWindow:
                try:
                    if exitBEFORE != "":
                        exitBEFORE()
                except Exception as ERR:
                    print(ERR, "if you do not add extra functions for exitBEFORE. it's in .update()")
                break
            if Update != "":
                Update()
        self.GetWindow.close() # if loop finish wnidow close
    
    @property
    def CloseNow(self):
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

    # Not Working      -> GSelection
    # Working          -> GIncreaseSelection
    # Working          -> GSlider
    # Not Working      -> GProgressBar
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
    def GListBoxBorderSize(self, Border: int, WindowValue: str):
        return self.GetWindow[WindowValue].Widget.configure(borderwidth=Border, relief=tk.GROOVE)

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

    # Experimantal -> GCanvas Class
    def GCanvas(
        self, SetValue: str, BColor: str = "black", xStretch: bool = False, yStretch: bool = False, Visible: bool = True, border: int = 0, 
        Size: tuple = (None, None), EmptySpace: tuple = (None, None)
    ): 
        
        return Canvas(
            key=SetValue, background_color=BColor, expand_x=xStretch, expand_y=yStretch, visible=Visible, border_width=border, size=Size, pad=EmptySpace
        )
    """
    This is not finish yet!
    but you can draw someting in canvas use GCanvas Class

    self.Layout = [
        [self.GC.GCanvas(SetValue="canvas", xStretch=True, yStretch=True)]
    ]
    
    self.Canvas = GCanvas(CanvasValue="canvas", Window=self.GC.GetWindow)
    """

    # window widgets
    def GFrame(
            self, GFText=None, InsideWindowLayout=[[]], SetValue=None, InfoWindow=None, Border=1, TFont="Sans, 20", Size=(None, None), 
            xStretch=False, yStretch=False, EmptySpace=(None, None), TColor=None, BColor=None, Visible=True
        ): 
        
        return Frame(
            title=GFText, layout=InsideWindowLayout, key=SetValue, border_width=Border, tooltip=InfoWindow, font=TFont, size=Size, pad=EmptySpace, 
            expand_x=xStretch, expand_y=yStretch, title_color=TColor, background_color=BColor, visible=Visible 
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

    def GColumn(self, winColumnLayout_List=None, Size=(None, None), xStretch=None, yStretch=None, EmptySpace=(None, None), Visible=True, SetValue=None, BColor=None):
        return Column(
            layout=winColumnLayout_List, key=SetValue, size=Size, expand_x=xStretch, expand_y=yStretch, pad=EmptySpace, visible=Visible, background_color=BColor
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
            BColor=None, TBColor=GnuChanOSColor().SColors3, TColor=None, STColor=GnuChanOSColor().TColor, SBColor=GnuChanOSColor().SColors0, Size=(None, None), TBorder=0, Border=0
        ): 
        
        return TabGroup(
            layout=TabGroupLayout, key=SetValue, expand_x=True, expand_y=True, size=Size,
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
            xStretch=False, yStretch=False, EmptySpace=(None), TColor=None, BColor=None, border=None 
        ): 
        
        return Text(text=SetText, font=TFont, key=SetValue, size=Size, justification=TPosition, expand_x=xStretch, expand_y=yStretch,  pad=EmptySpace, 
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
            xStretch=False, yStretch=False, Focus=True, ReadOnly=False, NoScroolBar=True, EmptySpace=(None, None), TColor=None, BColor=None, Border=0
        ):

        return Multiline(
                default_text=InText, font=TFont, key=SetValue, size=Size, focus=Focus, justification=TPosition, visible=Visible, disabled=ReadOnly, 
                expand_x=xStretch, expand_y=yStretch, no_scrollbar=NoScroolBar, text_color=TColor, background_color=BColor, pad=EmptySpace, border_width=Border,
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

    def GRadio(self, RText=None, TFont="Sans, 20", groupID=None, SetValue=None, CEvent=True, EmptySpace=(None, None), TColor=None, BColor=None):
        return Radio(text=RText, font=TFont, group_id=groupID, key=SetValue, enable_events=CEvent, pad=EmptySpace, text_color=TColor, background_color=BColor)
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

    # this is can change in the future
    def GetFilePath(
        self, defaultPATH=str(os.path.expanduser("~")), message="", title="", noWindow=True, noTitleBar=False, fileTypes=[("All files (*.*)", "*.*")],
        bcolor=GnuChanOSColor().FColors1, buttonColor = GnuChanOSColor().FColors3
        ):

        return popup_get_file(
            default_path=defaultPATH, message=message,  no_window=noWindow, file_types=fileTypes, no_titlebar=noTitleBar, title=title,
            button_color=buttonColor, background_color=bcolor
        )

    def GetFileForSave(
        self, defaultPATH=str(os.path.expanduser("~")), message="", title="", noWindow=True, noTitleBar=False, fileTypes=[("All files (*.*)", "*.*")],
        bcolor=GnuChanOSColor().FColors1, buttonColor = GnuChanOSColor().FColors3
        ):

        return popup_get_file(
            save_as=True, default_path=defaultPATH, message=message,  no_window=noWindow, file_types=fileTypes, no_titlebar=noTitleBar, title=title,
            button_color=buttonColor, background_color=bcolor
        )

    def GetFolderPath(
        self, defaultPATH=str(os.path.expanduser("~")), message="", title="", noWindow=True, noTitleBar=False,
        bcolor=GnuChanOSColor().FColors1, buttonColor = GnuChanOSColor().FColors3
        ):

        return popup_get_folder(default_path=defaultPATH, message=message,  no_window=noWindow, no_titlebar=noTitleBar, title=title,
                              button_color=buttonColor, background_color=bcolor)

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
    def __init__(self, MaxChannelLimit=5) -> None:
        global pygame
        import pygame.mixer
        self.MaxChannelLimit = MaxChannelLimit
        self.SoundFileList = []
        self.SoundIndex = 0
        self.Volume = 1
        self.SoundLength = 0
        self.SoundLength_Backup = 0
        self.PlayAgain = False
        self.GiveLength = False
        self.MusicName = ""

        pygame.mixer.init()
        pygame.mixer.set_num_channels(self.MaxChannelLimit)

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
        WindowTitle="Default Title", Size=(800, 600), resizable=False, finalize=True, winPosX=1920 / 2, winPosY=1080 / 2,
        WindowText = "Default Text", WindowTextFont = "Sans", WindowTextFontSize = 20, 
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
        self.button = [
            [
                self.GPush(self.CGC.FColors11),
                self.GButton(Text = "Exit"),
                self.GPush(self.CGC.FColors11),
            ]
        ]

        self.Layout = [
            [self.GMultiline(
                InText=self.windowText, TFont=self.TextFont, TPosition="center", 
                xStretch=True, yStretch=True, BColor=self.WindowTextBackgroundColor, ReadOnly=True
            )],
            [self.GColumn(winColumnLayout_List=self.button, BColor=self.ButtonLayoutBackgroundColor, xStretch=True)]
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)


    def Update(self):
        if self.GetEvent == "exit":
            self.closeWindow = True

    def BeforeExit(self):
        print(f"{self.WindowTitle} is closed")
