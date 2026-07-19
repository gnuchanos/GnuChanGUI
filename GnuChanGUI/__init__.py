from tkinter import font

from .gcLibrary_original import *


import os
import random
import math
import threading
import time

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

        # Keyboard
        self.bindings = {}  # Store bindings: {bind_string: callback}
        self.enabled = True

        # Letters
        self.A = 'a'
        self.B = 'b'
        self.C = 'c'
        self.D = 'd'
        self.E = 'e'
        self.F = 'f'
        self.G = 'g'
        self.H = 'h'
        self.I = 'i'
        self.J = 'j'
        self.K = 'k'
        self.L = 'l'
        self.M = 'm'
        self.N = 'n'
        self.O = 'o'
        self.P = 'p'
        self.Q = 'q'
        self.R = 'r'
        self.S = 's'
        self.T = 't'
        self.U = 'u'
        self.V = 'v'
        self.W = 'w'
        self.X = 'x'
        self.Y = 'y'
        self.Z = 'z'

        # Numbers
        self.ZERO = '0'
        self.ONE = '1'
        self.TWO = '2'
        self.THREE = '3'
        self.FOUR = '4'
        self.FIVE = '5'
        self.SIX = '6'
        self.SEVEN = '7'
        self.EIGHT = '8'
        self.NINE = '9'

        # Function keys
        self.F1 = 'F1'
        self.F2 = 'F2'
        self.F3 = 'F3'
        self.F4 = 'F4'
        self.F5 = 'F5'
        self.F6 = 'F6'
        self.F7 = 'F7'
        self.F8 = 'F8'
        self.F9 = 'F9'
        self.F10 = 'F10'
        self.F11 = 'F11'
        self.F12 = 'F12'

        # Navigation / editing
        self.ENTER = 'Return'
        self.ESCAPE = 'Escape'
        self.SPACE = 'space'
        self.TAB = 'Tab'
        self.BACKSPACE = 'BackSpace'
        self.DELETE = 'Delete'
        self.INSERT = 'Insert'
        self.HOME = 'Home'
        self.END = 'End'
        self.PAGE_UP = 'Prior'
        self.PAGE_DOWN = 'Next'
        self.LEFT = 'Left'
        self.RIGHT = 'Right'
        self.UP = 'Up'
        self.DOWN = 'Down'

        # Modifier keys (use inside key sequences)
        self.CONTROL = 'Control'
        self.SHIFT = 'Shift'
        self.ALT = 'Alt'
        self.META = 'Meta'

        # Common combos
        self.CTRL_A = 'Control-a'
        self.CTRL_C = 'Control-c'
        self.CTRL_V = 'Control-v'
        self.CTRL_X = 'Control-x'
        self.CTRL_Z = 'Control-z'
        self.CTRL_S = 'Control-s'
        self.CTRL_O = 'Control-o'
        self.CTRL_SHIFT_S = 'Control-Shift-S'
        self.CTRL_ALT_DELETE = 'Control-Alt-Delete'

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

    def IsWindowReady(self):
        """Returns True if the window has been created and is not destroyed."""
        if not hasattr(self, 'GetWindow') or self.GetWindow is None:
            return False
        return not self.GetWindow.is_closed(quick_check=True)

    def IsWindowFullscreen(self):
        """Returns True if the window is in fullscreen mode."""

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

    def SetUpdate(self, Update: callable = None, exitBEFORE: callable = None, TimeOUT: int = 100):
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

        return Canvas(
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
            xStretch=False, yStretch=False, xStretch_weight=None, yStretch_weight=None, yStretch_row_weight=None, Focus=True, ReadOnly=False, NoScroolBar=True, EmptySpace=(None, None), TColor=None, BColor=None, EnableUndo=True
        ):

        return Multiline(
                default_text=InText, font=TFont, key=SetValue, size=Size, focus=Focus, justification=TPosition, visible=Visible, disabled=ReadOnly, 
                expand_x=xStretch, expand_y=yStretch, expand_weight_x=xStretch_weight, expand_weight_y=yStretch_weight, expand_weight_row=yStretch_row_weight, no_scrollbar=NoScroolBar, text_color=TColor, background_color=BColor, pad=EmptySpace, border_width=0,
                autoscroll=True, auto_size_text=True, enable_events=EnableEvent, write_only=WriteOnly, wrap_lines=WrapLines, undo=EnableUndo
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

    def GImageGif(
            self, SetValue=None, filename=None, data=None, source=None, Size=(None, None), EmptySpace=(None, None),
            BColor=None, subsample=None, zoom=None, rclickMenu=None, xStretch=False, yStretch=False, Visible=True,
            ActiveEvent=False,
        ):
        """Create an Image element for an animated GIF.

        Use the returned element's update_animation() or update_animation_no_buffering() methods to advance frames.
        """
        return Image(
            source=source, filename=filename, data=data, background_color=BColor, size=Size, pad=EmptySpace,
            key=SetValue, subsample=subsample, zoom=zoom, right_click_menu=rclickMenu,
            expand_x=xStretch, expand_y=yStretch, visible=Visible, enable_events=ActiveEvent,
        )

        """
        layout = [
            [gc.GImageGif(SetValue="gif", filename="anim.gif", xStretch=True)]
        ]

        GetWindow["gif"].update_animation("anim.gif", time_between_frames=100)
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

    def GPanel(
            self, PaneColumns, SetValue=None, BColor=None, Size=(None, None), EmptySpace=(None, None),
            Orientation="vertical", show_handle=True, relief=None, handle_size=None, Border=None,
            xStretch=None, yStretch=None, Visible=True,
        ):
        pane_kw = dict( 
            pane_list=PaneColumns,  background_color=BColor, size=Size, pad=EmptySpace,
            orientation=Orientation, show_handle=show_handle, handle_size=handle_size,
            border_width=Border, key=SetValue,
            expand_x=xStretch, expand_y=yStretch, visible=Visible,
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
            data=TreeDATA, headings=headings, key=SetValue, font=TFont, visible=Visible,
            pad=EmptySpace, text_color=TColor, background_color=BColor, enable_events=ActiveEvent,
            num_rows=num_rows, expand_x=xStretch, expand_y=yStretch,
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
            ListValues, default_value=DefaultValue, key=SetValue, font=TFont, size=Size,
            pad=EmptySpace,  visible=Visible, disabled=Disabled, text_color=TColor,
            background_color=BColor, expand_x=xStretch, expand_y=yStretch,
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
            text=SetText, size=Size, font=TFont, key=SetValue, pad=EmptySpace, text_color=TColor,
            background_color=BColor, justification=TPosition, enable_events=ActiveEvent, visible=Visible,
            expand_x=xStretch, expand_y=yStretch, right_click_menu=rclickMenu,
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
            Text, menu_def, key=SetValue, font=TFont, pad=EmptySpace, text_color=tcolor,
            background_color=bcolor, disabled=Disabled, visible=Visible, expand_x=xStretch, expand_y=yStretch,
            tearoff=tearoff, border_width=Border,
            tooltip=tooltip, image_filename=bImage,
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

    def GAddTab(self, tab_group_key, tab_title, tab_layout):
        try:
            # Get the TabGroup element
            tab_group = self.GetWindow[tab_group_key]
            if tab_group is None:
                print(f"Error: TabGroup with key '{tab_group_key}' not found")
                return None
            
            # Create a new Tab element
            new_tab = Tab(title=tab_title, layout=tab_layout, key=None)
            
            # Use the TabGroup's add_tab method
            tab_group.add_tab(new_tab)
            
            print(f"Tab '{tab_title}' added successfully to '{tab_group_key}'")
            return new_tab
        except Exception as e:
            print(f"Error adding tab: {e}")
            return None

    def GRemoveTab(self, tab_group_key, tab_identifier):
        try:
            # Get the TabGroup element
            tab_group = self.GetWindow[tab_group_key]
            if tab_group is None:
                print(f"Error: TabGroup with key '{tab_group_key}' not found")
                return False
            
            # Use the TabGroup's remove_tab method
            tab_group.remove_tab(tab_identifier)
            
            identifier_str = str(tab_identifier)
            print(f"Tab '{identifier_str}' removed successfully from '{tab_group_key}'")
            return True
        except Exception as e:
            print(f"Error removing tab: {e}")
            return False


# Simple Timer
class GTimer:
    def __init__(self) -> None:
        self.Second = 0
        self.Minute = 0
        self.Hour   = 0
        self.StringTime = ''

        self.TimerStarts = False
        self.KillThreads = False

        self.gcT = threading.Thread(target=self.Go, args=[]).start()
        

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




# for game development
class GVector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    @property
    def get(self):
        return (self.x, self.y)

class GColor_RGBA:
    def __init__(self, r=0, g=0, b=0, a=255):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    @property
    def get(self):
        # convert RGBA to hex color string
        return f"#{self.r:02X}{self.g:02X}{self.b:02X}{self.a:02X}"

class GColor_HEX:
    def __init__(self, HVS: str):
        # tk color string to "#FF0000"
        self.HVS = HVS

    @property
    def get(self):
        return self.HVS

class GCamera2D:
    def __init__(self, offset: GVector2, target: GVector2, rotation: float, zoom: float, origin: GVector2):
        self.offset = offset
        self.target = target
        self.rotation = rotation
        self.zoom = zoom
        self.origin = origin

class GFont:
    def BuildFont(self, FontName: str, FontSize: int):
        if FontName not in font.families():
            raise ValueError(f"Font '{FontName}' not found in system fonts")

        return f"{FontName}, {FontSize}"

    def customFont(self, FontPath: str, FontSize: int):
        if not os.path.isfile(FontPath):
            raise FileNotFoundError(f"Font file not found: {FontPath}")

        _FONT = font.Font(file=FontPath, size=FontSize)

        return _FONT


class GGameCanvas(Canvas):
    def __init__(self, SetValue=None, Size=(None, None), EmptySpace=(None, None), BColor=None, xStretch=False, yStretch=False, Visible=True):
        super().__init__(size=Size, pad=EmptySpace, background_color=BColor, key=SetValue, expand_x=xStretch, expand_y=yStretch, visible=Visible)

        from PIL import Image, ImageTk

        if PIL not in sys.modules:
            raise ImportError("PIL (Pillow) library is required for GGameCanvas. Please install it with 'pip install Pillow'.")

        self.Image = Image
        self.ImageTk = ImageTk

        self.Entities = {} # dict entitiy {type, value, visible}
        self.uiEntities = {} # dict ui entitiy {type, value, visible}
        self.closeWindow = False

    # how to draw 2D
    def ClearBackground(self, color: GColor_HEX):
        # Set background color for canvas
        self.configure(background=color.get)

    def BeginDrawing(self, Entitys: callable = None, ClearColor: GColor_HEX = "#000000"):
        # Setup canvas (framebuffer) to start drawin canvas
        if Entitys == None:
            warnings.warn("Entitys is None, no entities to draw")

        if ClearColor != None:
            warnings.warn("ClearColor is not None, but you didn't provide ClearColor, so it will be ignored")

        Entitys() # call entitys function to update entities before drawing
        self.ClearBackground(ClearColor) # clear background with color

    def BeginMode2D(self, camera: GCamera2D, Entitys: callable = None):
        # Begin 2D mode with custom camera (2D)
        if Entitys == None:
            warnings.warn("Entitys is None, no entities to draw")
        
        Entitys() # call entitys function to update entities before drawing

    def EndMode2D(self):
        self.uiEntities.clear()


    def EndDrawing(self):
        self.Entities.clear()
        self.delete("all")


    def GetCanvasWidth(self):
        # Get current screen width
        self.update_idletasks() # update canvas to get correct width
        return self.winfo_width()

    def GetCanvasHeight(self):
        # Get current screen height
        self.update_idletasks() # update canvas to get correct height
        return self.winfo_height()

    # keyboard and mouse input
    def IsKeyPressed(key: str, GnuChanGUI: GnuChanGUI):
        # Check if a key has been pressed once
        return GnuChanGUI.GetEvent == key

    def IsKeyPressedRepeat(key: str, GnuChanGUI: GnuChanGUI):
        # Check if a key has been pressed again
        return GnuChanGUI.GetEvent == key

    def IsKeyDown(key: str, GnuChanGUI: GnuChanGUI):
        # Check if a key is being pressed
        return GnuChanGUI.GetEvent == key

    def IsKeyReleased(key: str, GnuChanGUI: GnuChanGUI):
        # Check if a key has been released once
        return GnuChanGUI.GetEvent == key

    def IsKeyUp(key: str, GnuChanGUI: GnuChanGUI):
        # Check if a key is NOT being pressed
        return GnuChanGUI.GetEvent != key

    # entitiys un tk canvas elementleri gibi dusunulebilir ama bu entitiyler sadece canvas icinde gosterilir ve hareket ederler
    def CreateText(self, text: str, fontAndSize: str, posX: int, posY: int, color: GColor_HEX):
        self.Entities[text] = {"type": "text", "value": text, "visible": True}

    def CreateTextPro(self, text: str, fontAndSize: GFont, position: GVector2, origin: GVector2, rotation: float, spacing: int, color: GColor_RGBA):
        self.Entities[text] = {"type": "text", "value": text, "visible": True}

    def CreateLine(self, startPos: GVector2, endPos: GVector2, color: GColor_HEX, thickness: int):
        self.Entities[f"line_{id(startPos)}_{id(endPos)}"] = {"type": "line", "value": (startPos, endPos), "visible": True}

    def CreateCircle(self, center: GVector2, radius: int, color: GColor_HEX, thickness: int):
        self.Entities[f"circle_{id(center)}_{radius}"] = {"type": "circle", "value": (center, radius), "visible": True}

    def CreateRectangle(self, position: GVector2, scale: GVector2, rotation: float, color: GColor_HEX, thickness: int, fill=False, fillColor: GColor_HEX = None):
        self.Entities[f"rectangle_{id(position)}_{scale.x}_{scale.y}"] = {"type": "rectangle", "value": (position, scale, rotation, fill, fillColor), "visible": True}

    def CreateSprite(self, imagePath: str, position: GVector2, rotation: float, scale: float, color: GColor_RGBA):
        self.Entities[f"sprite_{id(position)}"] = {"type": "sprite", "value": (imagePath, position, rotation, scale, color), "visible": True}

    # Draw functions, these functions will be called in BeginDrawing and BeginMode2D, you can update entities in these functions before drawing
    # entitiys un tk canvas elementleri gibi dusunulebilir ama bu entitiyler sadece canvas icinde gosterilir ve hareket ederler
    def DrawText(self, text: str, fontAndSize: str, posX: int, posY: int, color: GColor_HEX):
        self.create_text(posX, posY, text=text, font=fontAndSize, fill=color.get)
        self.Entities[text] = {"type": "text", "value": text, "visible": True}

    def DrawTextPro(self, text: str, fontAndSize: GFont, position: GVector2, origin: GVector2, rotation: float, spacing: int, color: GColor_RGBA):
        # text drawing with custom font, rotation and spacing
        self.create_text(position.get, text=text, font=fontAndSize, fill=color.get)
        self.Entities[text] = {"type": "text", "value": text, "visible": True}

    def DrawLine(self, startPos: GVector2, endPos: GVector2, color: GColor_HEX, thickness: int):
        self.create_line(startPos.get, endPos.get, fill=color.get, width=thickness)
        self.Entities[f"line_{id(startPos)}_{id(endPos)}"] = {"type": "line", "value": (startPos, endPos), "visible": True}

    def DrawCircle(self, center: GVector2, radius: int, color: GColor_HEX, thickness: int):
        self.create_oval(
            center.x - radius, center.y - radius, center.x + radius, center.y + radius,
            outline=color.get, width=thickness
        )
        self.Entities[f"circle_{id(center)}_{radius}"] = {"type": "circle", "value": (center, radius), "visible": True}

    def DrawRectangle(self, position: GVector2, scale: GVector2, rotation: float, color: GColor_HEX, thickness: int, fill=False, fillColor: GColor_HEX = None):
        self.create_rectangle(
            position.x, position.y, position.x + scale.x, position.y + scale.y,
            outline=color.get, width=thickness
        )
        self.Entities[f"rectangle_{id(position)}_{scale.x}_{scale.y}"] = {"type": "rectangle", "value": (position, scale, rotation, fill, fillColor), "visible": True}

    def DrawSprite(self, imagePath: str, position: GVector2, rotation: float, scale: float, color: GColor_RGBA):
        #  Image, ImageTk for rotate and scale, better optimization needed for large images and many sprites
        try:
            img = self.Image.open(imagePath)
            img = img.resize((int(img.width * scale), int(img.height * scale)), self.Image.ANTIALIAS)
            img = img.rotate(rotation, expand=True)
            tk_img = self.ImageTk.PhotoImage(img)
            self.create_image(position.get, image=tk_img, anchor="center")
            self.Entities[f"sprite_{id(position)}"] = {"type": "sprite", "value": (imagePath, position, rotation, scale, color), "visible": True}

        except Exception as e:
            print(f"Error loading sprite: {e}")
        
        
    # draw all
    def EntitiyDraw(self):
        for i in self.Entities:
            entity = self.Entities[i]
            if entity["visible"]:
                if entity["type"] == "text":
                    self.DrawText(entity["value"], "Sans, 20", 100, 100, GColor_HEX("#FFFFFF"))
                elif entity["type"] == "line":
                    startPos, endPos = entity["value"]
                    self.DrawLine(startPos, endPos, GColor_HEX("#FFFFFF"), 1)
                elif entity["type"] == "circle":
                    center, radius = entity["value"]
                    self.DrawCircle(center, radius, GColor_HEX("#FFFFFF"), 1)
                elif entity["type"] == "rectangle":
                    position, scale, rotation, fill, fillColor = entity["value"]
                    self.DrawRectangle(position, scale, rotation, GColor_HEX("#FFFFFF"), 1, fill=fill, fillColor=fillColor)
                elif entity["type"] == "sprite":
                    imagePath, position, rotation, scale, color = entity["value"]
                    self.DrawSprite(imagePath, position, rotation, scale, color)


    # game start in here
    def run(self, Update: callable, Draw: callable):
        while not self.closeWindow:
            Update() # update game logic
            Draw() # draw everything

        # must clean
        self.clear()
        
    def test(self):
        # this is just a test function to show how to use GGameCanvas, you can remove it
        self.BeginDrawing()
        self.DrawText("Hello World", "Sans, 20", 100, 100, GColor_HEX("#FFFFFF"))
        self.DrawLine(GVector2(50, 50), GVector2(150, 150), GColor_HEX("#FF0000"), 2)
        self.DrawCircle(GVector2(200, 200), 50, GColor_HEX("#00FF00"), 3)
        self.DrawRectangle(GVector2(300, 300), GVector2(100, 50), 0, GColor_HEX("#0000FF"), 4, fill=True, fillColor=GColor_HEX("#0000FF"))
        self.EndDrawing()