from .gcLibrary import *
from .gcLibrary import __version__
from threading import Thread
import random
import math
from PIL import Image, ImageTk
from shapely.geometry import box
from pydub import AudioSegment


"""
pip install  git+https://github.com/gnuchanos/gnuchangui
"""

"""
python -m venv ./venv
./venv/bin/activate 
"""

"""
Warning 0: popup_get_file('Select a file to open', no_window=True) isn't working with Thread(target=Create, args=[]).start(). 
The GUI is freezing, and you can only close the program using the task manager.
"""

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
        randomColor = random.choice(["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#00FFFF", "#FF00FF", "#FFFFFF", "#000000", "#800080", "#FFA500", "#FFC0CB", "#008080", "#FFD700", "#A52A2A", "#FF1493", "#4B0082", "#00FF7F", "#1E90FF", "#FF4500", "#FF69B4"])
        return randomColor

class GnuChanOSColor:
    def __init__(self) -> None:
        self.colors0 = "#150129"
        self.colors1 = "#240046"  
        self.colors2 = "#5a189a" 
        self.colors3 = "#9d4edd" 
        self.colors4 = "#c77dff"  
        self.colors5 = "#3c096c"

class Themecolors:
    @property
    def GnuChanOS(self, themeName="GnuchanTheme", text="#9d4edd", background="#240046", input="#3c096c", text_input="#9d4edd", 
                     scroll="#5a189a", button=('#c77dff', '#3c096c'), progress=('#c77dff', '#3c096c'), 
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
    def __init__(self, Title="Defaul Title", Size=(800, 600), resizable=False, finalize=True) -> None:
        self.size = Size
        self.title = Title
        self.resizable = resizable
        self.finalize = finalize

        self.fontName = "Sans"
        self.fontSize = 15
        self.font = f"{self.fontName}, {self.fontSize}"

        self.code = "missing Window list!!"
        self.layout = [[self.GText(title=self.code, xStretch=True, yStretch=True, bcolor="black", font="Sans, 13")]]

        self.event = None
        self.GetValues = None
        self.closeWindow = False

        # don't remove ),<--)
        self.ImagesType = [("PNG (*.png)", "*.png"), ("JPEG (*.jpg)", "*.jpg")]
        self.VideoTypes = [("MKV (*.mkv)", "*.mkv"), ("MP4 (*.mp4)", "*.mp4")]
        self.MusicTypes = [("MP3 (*.mp3)", "*.mp3")]
        self.AllTypes   = [("All files (*.*)", "*.*")]

        # f"{gc.PathPythonFile}/music.mp3" or diffrent file
        self.PathPythonFile = os.path.dirname(os.path.abspath(__file__))

    # Create Window
    def GWindow(self, mainWindow=None, TopMode=False, rightClickMenu=None, locationX=0, locationY=0):
        if mainWindow != None:
            self.layout = mainWindow
            # if main Window is None self.layout can warning user and self.layout is ready warning layout
        self.window = Window(self.title, layout=self.layout, size=self.size, keep_on_top=TopMode, resizable=self.resizable, 
                                finalize=self.finalize, right_click_menu=rightClickMenu, return_keyboard_events=True, margins=(0, 0), location=(locationX, locationY))
        self.window.finalize()
        # this is new for close window good way
        return self.window
        """
        window have right click menu --> ["menu", ["inMenu1", "inMenu2"]]
        """

    def update(self, GUpdate="", exitBEFORE="", timeout=1000):
        while True:
            self.event, self.GetValues = self.window.read(timeout=timeout)
            if self.event in (WIN_CLOSED, "Exit"):
                try:
                    if exitBEFORE != "":
                        exitBEFORE()
                except Exception as ERR:
                    print(ERR, "This is not an error, just a warning if you do not add extra functions for exitBEFORE. it's in .update()")
                break
            if self.closeWindow:
                try:
                    if exitBEFORE != "":
                        exitBEFORE()
                except Exception as ERR:
                    print(ERR, "This is not an error, just a warning if you do not add extra functions for exitBEFORE. it's in .update()")
                break
            if GUpdate != "":
                GUpdate()
        self.window.close() # if loop finish wnidow close
    
    @property
    def close(self):
        self.window.close()

    # Note there is no delta time
    @property
    def dt(self):
        dt = 1 # use this with timeout 1000/MS still not like real second slow or sometimes is fast
        return dt

    def GTitleBar(self, title="Window Title", icon=None, font="Sans, 12", tcolor=None, bcolor=None):
        return Titlebar(title=title, icon=icon, font=font, text_color=tcolor, background_color=bcolor)
        """
        Titlebar: Disable window resizable, I don't know why.
        ı must ask this soon
        """

    # window top menu bar regular default or custom for theme
    def GMenu(self, winMenu=None, font="Sans, 20"):
        return Menu(menu_definition=winMenu, font=font)

    def GMenuForTheme(self, winMenu=None, font="Sans, 20", tcolor=None, bcolor=None, ):
        return MenubarCustom(menu_definition=winMenu, font=font, text_color=tcolor, background_color=bcolor)

    def GFocus(self, GetValues=None):
        return self.window[GetValues].set_focus() 
        """
        focus not Finish
        """

    # GetValue With GText
    def GetGTextValue(self, GTextValue):
        return self.window[GTextValue].get()

    # ekstra options
    # This setting only works under GWindow. "this is tk"
    def GListBoxBorderSize(self, border=0, windowValue=None):
        return self.window[windowValue].Widget.configure(borderwidth=border, relief=tk.GROOVE)

    def GSelectionBorderSize(self, border=0, windowValue=None, borderColor=None, highlightcolor=None):
        combo = self.window[windowValue]
        combostyle, style_name = combo.ttk_style, combo.ttk_style_name
        combostyle.configure(style_name, selectbackground=borderColor, selectforeground=highlightcolor, borderwidth=border)

    def GMultilineTabSpace(self, gMultilineFont, gMultilineValue):
        char = Text.char_width_in_pixels(gMultilineFont)
        tabs = (2*char, 'left', 4*char, 'left',)
        multiline = self.window[gMultilineValue]
        multiline.Widget.configure(tabs=tabs)

    def AddNewBorderWithColor(self, Value, Color, BorderSize):
        _mw = self.window[Value].Widget
        _mw.config(highlightbackground=Color, highlightcolor=Color, highlightthickness=BorderSize)

    def FontSize_Change(self, windowValue, fontSize=20):
        self.window[windowValue].update(font=f"{self.fontName}, {fontSize}")

    def TextColor_Change(self, windowValue, color="white"):
        self.window[windowValue].update(text_color=color)

    def BackgroundColor_Change(self, windowValue, color="black"):
        self.window[windowValue].update(background_color=color)

    # this can change visible true or false but also change layer position! i don't know how to fix for now or never
    # Don't Forget to Pin Object
    def GVisible(self, Value, show):
        self.window[Value].update(visible=show)
        if show:
            self.window[Value].unhide_row()
        else:
            self.window[Value].hide_row()

    # Experimantal
    def GCanvas(self, value, bcolor=None, xStretch=False, yStretch=False, Visible=True, border=0, size=(None, None), EmptySpace=(None, None)):
        return Canvas(
                key=value, background_color=bcolor, expand_x=xStretch, expand_y=yStretch, 
                visible=Visible, border_width=border, size=size, pad=EmptySpace
        )
    """
    This is not finish yet!
    but you can draw someting in canvas use GCanvas Class
    """

    # window widgets
    def GFrame(
            self, title=None, winLayout=[[]], value=None, infoWındow=None, border=1, font="Sans, 20", size=(None, None), 
            xStretch=False, yStretch=False, EmptySpace=(None, None), tColor=None, bcolor=None, visible=True
        ): return Frame(
            title=title, layout=winLayout, key=value, border_width=border, tooltip=infoWındow, font=font, size=size, pad=EmptySpace, 
            expand_x=xStretch, expand_y=yStretch, title_color=tColor, background_color=bcolor, visible=visible )
    
    """
        gMenu = [ ["Info", ["GnuChanOS", "Youtube Channel", "Github Page"]], ["System", ["Exit"]] ]
        defaultFont = "Sans, 20"
        c = GColors()

        test1 = [[gc.GMenuForTheme(winMenu=gMenu, font=defaultFont)],
                [gc.GText("test", xStretch=True, position="center")]]

        test2 = [[gc.GMenuForTheme(winMenu=gMenu, font=defaultFont)],
                [gc.GText("test", xStretch=True, position="center")]]

        test3 = [[gc.GMenuForTheme(winMenu=gMenu, font=defaultFont)],
                [gc.GText("test", xStretch=True, position="center")]]

        test4 = [[gc.GMenuForTheme(winMenu=gMenu, font=defaultFont)],
                [gc.GText("test", xStretch=True, position="center")]]

        layout = [
                [gc.GFrame(winLayout=test1, value="test1", xStretch=True, yStretch=True, bcolor=c.blue1, border=2),
                gc.GFrame(winLayout=test2, value="test2", xStretch=True, yStretch=True, bcolor=c.blue1, border=2)],

                [gc.GFrame(winLayout=test3, value="test3", xStretch=True, yStretch=True, bcolor=c.blue1, border=2),
                gc.GFrame(winLayout=test4, value="test4", xStretch=True, yStretch=True, bcolor=c.blue1, border=2)]]

        default.GWindow(mainWindow=layout)
    """

    def GColumn(self, winColumn=None, size=(None, None), xStretch=None, yStretch=None, EmptySpace=(None, None), visible=True, value=None, bcolor=None):
        return Column(
                layout=winColumn, key=value, size=size, expand_x=xStretch, expand_y=yStretch, pad=EmptySpace, 
                visible=visible, background_color=bcolor
        )
        """
        TopLayer = [[gc.GText(title="Top Layer", position="center", font="Sans, 20", bcolor=c.blue1, xStretch=True, yStretch=True, 
                            EmptySpace=(0,0))]]

        MiddleLeftLayer = [[gc.GText(title="Middle Left", position="center", font="Sans, 20",bcolor=c.pink1, xStretch=True, yStretch=True, 
                                    EmptySpace=(5,0))]]

        MiddleRightLayer = [[gc.GText(title="Middle Right", position="center", font="Sans, 20", bcolor=c.purple1, xStretch=True, yStretch=True, 
                                    EmptySpace=(0,0))]]

        BottomLayer = [[gc.GText(title="Bottom Layer", position="center", font="Sans, 20", bcolor=c.pink8, xStretch=True, yStretch=True, 
                                EmptySpace=(0,0))]]

        layout = [
        [gc.GColumn(TopLayer, xStretch=True, yStretch=True)],
        [gc.GColumn(MiddleLeftLayer, xStretch=True, yStretch=True), 
            gc.GColumn(MiddleRightLayer, xStretch=True, yStretch=True)],
        [gc.GColumn(BottomLayer, xStretch=True, yStretch=True)] ]
        """

    # this is can grab print
    def GLog(
            self, value=None, font="Sans, 15", size=(None, None), EmptySpace=(None, None), 
            xStretch=False, yStretch=False, visible=True, tcolor=None, bcolor=None):
        return Output(
                key=value, font=font, size=size, pad=EmptySpace, expand_x=xStretch, expand_y=yStretch, 
                text_color=tcolor, background_color=bcolor, visible=visible, autoscroll_only_at_bottom=True
        )
        """
        I must disable the scrollbar and make it readonly.

        i love this becouse this can show print() in screen
        """

    # create Gtab and create GTap Group
    def GTabGroup(self, TabGroupLayout=None, value=None, font="Sans, 20",
        bcolor=None, sbcolor=None, tbcolor=None, tcolor=None, fcolor=None, stcolor=None, size=(None, None)):
        return TabGroup(
                layout=TabGroupLayout, key=value, expand_x=True, expand_y=True, size=size,
                background_color=bcolor, selected_background_color=sbcolor, tab_background_color=tbcolor, enable_events=True,
                title_color=tcolor, focus_color=fcolor, selected_title_color=stcolor, font=font, tab_border_width=0, border_width=0
        )
    def GTab(self, title, TabLayout=None, value=None, rclickMenu=None):
        return Tab(title=title, layout=TabLayout, key=value, right_click_menu=rclickMenu)
    def GTabNewTab(self, TabGroupValue, TabTitle, WinLayout, TabValue):
        return self.window[TabGroupLayout].add_tab(self.GTab(title=TabTitle, TabLayout=WinLayout, value=TabValue))

        """
        TabGroup Value: TabG : | tab1 value | tab2 value |
        [gc.GTabGroup(TabGroupLayout=[
            [gc.GTab(title="test1", TabLayout=tab1, value="tab1")],
            [gc.GTab(title="test2", TabLayout=tab2, value="tab2")],
        ], value="tabG")]

        Active tab
        def update():
            new = gc.GetValues["tabG"]
            if new == "tab1":
                print("tab1 is goooo")
            elif new == "tab2":
                print("tab2 is gooo")
        """   

# All Widgets
    # text widget
    def GText(
            self, title="", font="Sans, 20", value=None, size=(None, None), position="left", 
            xStretch=False, yStretch=False, EmptySpace=(None), tColor=None, bcolor=None, border=None ):
        return Text(text=title, font=font, key=value, size=size, justification=position, expand_x=xStretch, expand_y=yStretch,  pad=EmptySpace, 
            text_color=tColor, background_color=bcolor, border_width=border
        )
        """
        gc.GText(value="text")
        gc.window["text"].update("change text")
        """

    # button widget
    def GButton(
            self, title="", bImage=None, font="Sans, 20", value=None, size=(None, None), 
            visible=True, tcolor=None, bcolor=None, xStretch=False, yStretch=False, EmptySpace=(None), border=None ):
        return Button(
                title, button_color=(bcolor, tcolor), font=font, key=value, size=size, 
                expand_x=xStretch, expand_y=yStretch, pad=EmptySpace, image_filename=bImage, visible=visible, border_width=border
        )
        """
        gc.GButton(title="button")
        if gc.event == "button name or value": click event
            gc.window["text"].update(gc.GetValues["textInput"])
        """

    # listbox widget
    def GListBox(
            self, list=[], font="Sans, 20", value=None, size=(None, None), ActiveEvent=True, visible=True, 
            position="left", EmptySpace=(None, None), noScroolBar=False, xStretch=False, yStretch=False, tColor=None, bcolor=None):
        return Listbox(list, font=font, key=value, enable_events=ActiveEvent, visible=visible, justification=position, size=size, pad=EmptySpace,
                   no_scrollbar=noScroolBar, expand_x=xStretch, expand_y=yStretch, text_color=tColor, background_color=bcolor
        )
        """
        [gc.GListBox(value="list", xStretch=True, yStretch=True)],

        if gc.event == "addList":
            for i in range(1, 10):
                testList.append(i)
            gc.window["glist"].update(testList)

        gc.getvalue["glist"][0] # for select
        """
    
    # input widget
    def GInput (self, InText="", font="Sans, 20", value=None, size=(None, None), focus=True, position="left", visible=True, 
                PwChars=False, readonly=False, xStretch=False, yStretch=False, EmptySpace=(None), tcolor=None, bcolor=None, border=None):
        return Input(
                default_text=InText, font=font, key=value, size=size, focus=focus, justification=position,  pad=EmptySpace, expand_x=xStretch, 
                expand_y=yStretch, password_char=PwChars, visible=visible, readonly=readonly, background_color=bcolor, text_color=tcolor, border_width=border
        )
        """
        [gc.GText(value="text")],
        [gc.GInput(value="input", xStretch=True),  gc.GButton(title="Click", value="button", xStretch=True)],
        if gc.event == "change text":
            gc.window["text"].update(gc.GetValues["textInput"]) #text input value
        """

    # multiLine widget
    def GMultiline (self, InText="", font=None, value=None, size=(None, None), visible=True, position="left", enableEvent=True, WriteOnly=False, wrapLines=True,
                    xStretch=False, yStretch=False, focus=True, readonly=False, noScroolBar=True, EmptySpace=(None, None), tcolor=None, bcolor=None, border=None):
        return Multiline(
                default_text=InText, font=font, key=value, size=size, focus=focus, justification=position, visible=visible, disabled=readonly, 
                expand_x=xStretch, expand_y=yStretch, no_scrollbar=noScroolBar, text_color=tcolor, background_color=bcolor, pad=EmptySpace, border_width=border,
                autoscroll=True, auto_size_text=True, enable_events=enableEvent, write_only=WriteOnly, wrap_lines=wrapLines
        )
        """
        if gc.event == "addList":
            testList += str(random.randint(0, 50)) + "\n"
            gc.window["glist"].update(testList)
        """
    
    # cheack mark
    def GCheackBox(self, title=None, font="Sans, 20", value=None, EmptySpace=(None, None), tcolor=None, bcolor=None):
        return Checkbox(text=title, font=font, key=value, pad=EmptySpace, text_color=tcolor, background_color=bcolor)
        """
        [
            gc.GCheackBox(title="Half Life", value="hl"),
            gc.GCheackBox(title="Mafia", value="mf"),
            gc.GCheackBox(title="GTA San Andreas", value="gta"),
            gc.GCheackBox(title="Age Of Empires 2", value="age2")
        ],
        [gc.GButton(title="CheckBox", xStretch=True)]

        
        # gc.event in not working with button
        if gc.event == "CheckBox":
            if gc.GetValues["hl1"]:
                print("half life 1")
            if gc.GetValues["hl2"]:
                print("half life 2")
            if gc.GetValues["hl3"]:
                print("half life 3 ?????")
        """

    def GRadio(self, title=None, font="Sans, 20", groupID=None, value=None, cEvent=True, EmptySpace=(None, None), tcolor=None, bcolor=None):
        return Radio(text=title, font=font, group_id=groupID, key=value, enable_events=cEvent, pad=EmptySpace, text_color=tcolor, background_color=bcolor)
        """
        [
            gc.GRadio(title="Half Life 3", groupID="VALVE", value="hl3"),
            gc.GRadio(title="Portal 3", groupID="VALVE", value="portal3"),
            gc.GRadio(title="Left 4 Dead 3", groupID="VALVE", value="lfd3"),
            gc.GRadio(title="Team Fortress 3", groupID="VALVE", value="tf3"),
        ],

        # gc.event in not working with button
        if gc.event in ["hl1", "hl2", "hl3"]:
            if gc.event == "hl1":
                gc.window["hlGame"].update("can you play half life 1 before ?")
            elif gc.event == "hl2":
                gc.window["hlGame"].update("half life 2 good game")
            elif gc.event == "hl3":
                gc.window["hlGame"].update("there is no half life 3 :(")
        """

    # selections
    def GSelection(self, font="Sans, 20", values=None, defaultValue=None, value=None, EmptySpace=(None, None), visible=True, 
                   tcolor=None, bcolor=None, xStretch=False, yStretch=False):
        return Combo(
                values=values, key=value, default_value=defaultValue, font=font, pad=EmptySpace, visible=visible, text_color=tcolor, background_color=bcolor, 
                expand_x=xStretch, expand_y=yStretch, readonly=True
        )
        """
        [gc.GSelection(values=[1,2,3,4,5], value="GSelection", defaultValue=1, font=gc.font, xStretch=True)],
        if gc.GetValues["GSelection"]:
            print(gc.GetValues["GSelection"])
        """
    
    def GIncreaseSelection(self, rangeValue=None, startValue=None, value=None, font="Sans, 20", size=(None, None), EmptySpace=(None, None), 
                           tcolor=None, bcolor=None, xStretch=False, yStretch=False, Visible=True):
        return Spin(
                values=rangeValue, initial_value=startValue, font=font, key=value, size=size, pad=EmptySpace, expand_x=xStretch, expand_y=yStretch, 
                text_color=tcolor, background_color=bcolor, visible=Visible
        )
        """
        [gc.GIncreaseSelection(startValue=1, rangeValue=[1,2,3,4,5], value="GIncreaseSelection", font=gc.font, xStretch=True)],
        if gc.GetValues["GIncreaseSelection"]:
            print(gc.GetValues["GIncreaseSelection"])
        """
    
    def GSlider(self, range=None, value=None, defaultValue=None, font="Sans, 20", size=(None, None), direction="h", EmptySpace=(None, None), tcolor=None, 
                bcolor=None, xStretch=False, yStretch=False, Visible=True):
        
        return Slider(
                range=range, key=value, default_value=defaultValue, orientation=direction, font=font, size=size, pad=EmptySpace, text_color=tcolor, 
                background_color=bcolor, expand_x=xStretch, expand_y=yStretch, visible=Visible
        )   

    def GProgressBar(self, MaxValue=None, value=None, visible=True, direction="h"):
        return ProgressBar(max_value=MaxValue, key=value, visible=visible, orientation=direction)
        """
        [gc.GSlider(range=(0, 100), defaultValue=20, direction="h", value="slider" )],
        [gc.GProgressBar(MaxValue=100, value="pro", direction="h")]
        if gc.GetValues["GSlider1"]:
                gc.window["health"].update(gc.GetValues["GSlider1"])
                    health progressbar       sliderGSelectionBorderSize is give value
        """

    # Little things
    def GetFilePath(self, defaultPATH=str(os.path.expanduser("~")), message="", title="", noWindow=True, noTitleBar=False, fileTypes=[("All files (*.*)", "*.*")]):
        return popup_get_file(default_path=defaultPATH, message=message,  no_window=noWindow, file_types=fileTypes, no_titlebar=noTitleBar, title=title)

    def GetFileForSave(self, defaultPATH=str(os.path.expanduser("~")), message="", title="", noWindow=True, noTitleBar=False, fileTypes=[("All files (*.*)", "*.*")]):
        return popup_get_file(save_as=True, default_path=defaultPATH, message=message,  no_window=noWindow, file_types=fileTypes, no_titlebar=noTitleBar, title=title)

    def GetFolderPath(self, defaultPATH=str(os.path.expanduser("~")), message="", title="", noWindow=True, noTitleBar=False):
        return popup_get_folder(default_path=defaultPATH, message=message,  no_window=noWindow, no_titlebar=noTitleBar, title=title)

    # GFrame, xStretch and yStretch not working with pin
    # GColumn, it's same in here not working xStretch and yStretch
    def GPin(self, GObject):
        return pin(GObject)

    # with Property
    @property
    def Push(self):
        return Push()

    @property
    def hsep(self):
        return HSeparator()

    @property
    def vsep(self):
        return VSeparator()

    def GMessage(self, message=None, wmTitle="default Window", font="Sans, 15", tcolor=None, bcolor=None):
        return popup(message, title=wmTitle, font=font, text_color=tcolor, background_color=bcolor)

# This is not finished yet! And man, it's not good. It can't read two keys at the same time. This is why I make my own thing, but it's a bad way to read keyboard press events.
class GKeyboard:
    def __init__(self, window) -> None:
        self.window = window
        self.ReadKey = None
        self.key = ""
        self.ActiveKeys = []
        self.timeout = 2

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

        self.LeftMouseKey = "NoneValue-LEFT"
        self.RightMouseKey = "NoneValue-RIGHT"
        self.MiddleMouseKey = "NoneValue-MIDDLE"

    # mouse event only works with this
    def AddMouseEvent(self, MouseTrigerValue):
        self.graph = self.window[MouseTrigerValue]

        self.graph.bind("<Button-1>", "-LEFT")
        self.graph.bind("<Button-2>", "-MIDDLE")
        self.graph.bind("<Button-3>", "-RIGHT")

        self.LeftMouseKey = f"{MouseTrigerValue}-LEFT"
        self.RightMouseKey = f"{MouseTrigerValue}-RIGHT"
        self.MiddleMouseKey = f"{MouseTrigerValue}-MIDDLE"

# for canvas Object Transform and Scale
class GVector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

# this is not finish yet!
class GCanvas:
    def __init__(self, Window, CanvasValue) -> None:
        self.GWindow = Window
        self.Canvas = self.GWindow[CanvasValue].Widget # widget
        self.CanvasID = self.Canvas.winfo_id()         # widget ID
        self.DrawList = {}

        self.Scene_LOGO = 0
        self.Scene_MENU = 1
        self.Scene_GAMEPLAY = 2
        self.Scene_End = 3

        self.MousePosition = GVector2(0, 0)

        self.Transform = "transform"
        self.Scale = "scale"
        self.Color = "fcolor"
        self.BorderColor = "ocolor"
        self.Radius = "radius"
        self.Active = "active"
        self.Thickness = 'b'
        self.RecordX = 0
        self.RecordY = 0
        self.Hit0 = False
        self.Hit1 = False
        self.speed = 75
        self.stop = False

    # Clear Man or 23123123123 Gender
    def ClearCanvas(self):
        try:
            self.Canvas.delete('all')
        except Exception as ERR:
            print(ERR, " Clear Canvas")

    # Get Variable
    def OpenImage(self, ImagePath, Scale):
        try:
            image = Image.open(ImagePath)
            resized_image = image.resize(size=(Scale.x, Scale.y))
            return ImageTk.PhotoImage(resized_image)
        except Exception as ERR:
            print(ERR, "OpenImage Function ERR")

    # Canvas Size
    def GetCanvasScale_X(self):
        try:
            return self.Canvas.winfo_width()
        except Exception as ERR:
            print(ERR, " Get Canvas Scale X")

    def GetCanvasScale_Y(self):
        try:
            return self.Canvas.winfo_height()
        except Exception as ERR:
            print(ERR, " Get Canvas Scale Y")

    # get Mouse Position using Motion
    def ReadMousePosition(self):
        try:
            self.Canvas.bind('<Motion>', self.GetMousePosition)
        except Exception as ERR:
            print(ERR, " Read Mouse Position")

    def GetMousePosition(self, event):
        try:
            self.MousePosition = GVector2( event.x, event.y )
            return self.MousePosition
        except Exception as ERR:
            print(ERR, " Get Mouse Position")

    # Add add object in render pipline  # object name is index Number --------------------------------------------------------------------------------------------------------------------------
    def AddCircleObject(self, ObjectName, Transform, Radius, OutLineColor, FillColor, Active=True):
        try:
            self.DrawList[ObjectName] = {
                "type"      : 'c',
                'transform' : Transform,
                'radius'    : Radius,
                "ocolor"    : OutLineColor,
                "fcolor"    : FillColor,
                "active"    : Active   }
            return ObjectName
        except Exception as ERR:
            print(ERR, "Add Circle Object Function ERR")

    # need update
    def AddRectangleObject(self, ObjectName, Transform, Scale, OutLineColor, FillColor, Active=True):
        try:
            self.DrawList[ObjectName] = {
                "type"      : 'r',
                'transform' : Transform,
                'scale' : Scale,
                "ocolor" : OutLineColor,
                "fcolor" : FillColor,
                "active" : Active   }
            return ObjectName
        except Exception as ERR:
            print(ERR, "Add Circle Object Function ERR")

    def AddLineObject(self, ObjectName, Transform, Scale, FillColor, Thickness, Active=True):
        try:
            self.DrawList[ObjectName] = {
                "type"      : 'l',
                "transform" : Transform,
                "scale" : Scale,
                "fcolor" : FillColor,
                'b'  : Thickness,
                "active" : Active   }
            return ObjectName
        except Exception as ERR:
            print(ERR, "Add Circle Object Function ERR")

    def AddTextObject(self, ObjectName, Transform, Text, Color, Font, Scale, Active=True):
        try:
            self.DrawList[ObjectName] = {
                "type"      : 't',
                'transform'     : Transform,
                "text"          : Text,
                "color"         : Color,
                "font"          : Font,
                "scale"         : Scale,
                "active"        : Active    }
            return ObjectName
        except Exception as ERR:
            print(ERR, "Add Circle Object Function ERR")

    def AddImageObject(self, ObjectName, Transform, Image, Active=True, Scale=GVector2(20, 20)):
        try:
            self.DrawList[ObjectName] = {
                "type"      : 'i',
                "transform" : Transform,
                "Image"     : Image,
                "scale"     : Scale,
                "active"    : Active    }
            return ObjectName
        except Exception as ERR:
            print(ERR, "Add Circle Object Function ERR")
    # need update

    # get object Things
    def GetObjectPosition(self, Object, xOrY='x'):
        try:
            _Return = GVector2(self.DrawList[Object][self.Transform].x, self.DrawList[Object][self.Transform].y)
            if xOrY == 'x':
                return _Return.x
            elif xOrY == 'y':
                return _Return.y
        except Exception as ERR:
            print(ERR, " Get Object Position X")

    def GetObjectScale(self, Object=0, xOrY='x'):
        try:
            if xOrY == 'x':
                return self.DrawList[Object][self.Scale].x
            elif xOrY == 'y':
                return self.DrawList[Object][self.Scale].y
        except Exception as ERR:
            print(ERR, " Get object Scale X")

    def GetObjectScale_noXY(self, Object):
        try:
            returnValue = self.DrawList[Object][self.Scale]
            return returnValue
        except Exception as ERR:
            print(ERR, " Get Object Scale Y")

    def GetObjectRadius(self, Object):
        try:
            returnValue = self.DrawList[Object][self.Radius]
            return returnValue
        except Exception as ERR:
            print(ERR, " Get Object Scale Y")

    def GetObjectThickness(self, Object):
        try:
            returnValue = self.DrawList[Object][self.Thickness]
            return returnValue.y
        except Exception as ERR:
            print(ERR, " Get Object Thickness ERR")

    def GetObjectVisible(self, Object):
        try:
            return self.DrawList[Object][self.Active]
        except Exception as ERR:
            print(ERR, " Get Object Visible")

    # move object realtime this is not teleport like thing
    def MoveObject(self, Object=0, Speed=50, WhichDirection="left", XorY='x'):
        if str(XorY.startswith('x')).lower():
            try:
                if str(WhichDirection).startswith("l"):
                    self.DrawList[Object][self.Transform].x -= Speed * 0.1
                elif str(WhichDirection).startswith("r"):
                    self.DrawList[Object][self.Transform].x += Speed * 0.1
            except Exception as ERR:
                print(ERR, "Move Circle X withUpdate Function ERR")
        if str(XorY.startswith('y')).lower():
            try:
                if str(WhichDirection).startswith("u"):
                    self.DrawList[Object][self.Transform].y -= Speed * 0.1
                elif str(WhichDirection).startswith("d"):
                    self.DrawList[Object][self.Transform].y += Speed * 0.1
            except Exception as ERR:
                print(ERR, "Move Circle Y withUpdate Function ERR")

    # this is works like teleport
    def TeleportObject(self, Object, XorY, Position):
        try:
            if str(XorY).startswith('x'):
                self.DrawList[Object][self.Transform].x = Position
            elif str(XorY).startswith('y'):
                self.DrawList[Object][self.Transform].y = Position
        except Exception as ERR:
            print(ERR, "Change Object Transform Function ERR")

    def ChangeObjectColor(self, Object=None, Color=None, BorderColor=None):
        try:
            if Color != None:
                self.DrawList[Object][self.Color] = Color
            if BorderColor != None:
                self.DrawList[Object][self.BorderColor] = BorderColor
        except Exception as ERR:
            print(ERR, " Change Object Color ERR")

    def ChangeObjectVisible(self, Object, Visible):
        try:
            if Visible:
                self.DrawList[Object]["active"] = True
            else:
                self.DrawList[Object]["active"] = False
        except Exception as ERR:
            print(ERR, " Change Object Visible ERR")

    # Render Object
    def RenderCircle(self, Transform=GVector2(0, 0), Radius=20, OutLineColor="red", FillColor="blue"):
        try:
            self.Canvas.create_oval(Transform.x-Radius, Transform.y-Radius, Transform.x+Radius, Transform.y+Radius, outline=OutLineColor, fill=FillColor)
        except Exception as ERR:
            print(ERR, " Render Circle ERR for ")

    def RenderRectangle(self, Transform=GVector2(0, 0), Scale=GVector2(20, 30), OutLineColor="red", FillColor="blue"):
        try:
            self.Canvas.create_rectangle(Transform.x, Transform.y, Transform.x+Scale.x, Transform.y+Scale.y, outline=OutLineColor, fill=FillColor)
        except Exception as ERR:
            print(ERR, " Render Rectangle ERR for ")

    # StartX, StartY, EndX, EndY
    def RenderLine(self, Transform, Scale, Color='black', width=1):
        try:
            self.Canvas.create_line(Transform.x, Transform.y, Transform.x+Scale, Transform.y, fill=Color, width=width)
        except Exception as ERR:
            print(ERR, " Render Line ERR for ")

    def RenderText(self, Transform=GVector2(0, 0), Text="Default text", Color="red", Font="Sans", Size=12):
        try:
            self.Canvas.create_text(Transform.x, Transform.y, text=Text, fill=Color, font=(Font, Size))
        except Exception as ERR:
            print(ERR, " Render Text ERR for ")

    # only use this with OpenImage() 
    def RenderImage(self, Transform, Image):
        try:
            self.Canvas.create_image(Transform.x, Transform.y, anchor='nw', image=Image)
        except Exception as ERR:
            print(ERR, " Render Image")

    # Thi is all Circle Colllions
    def CheckMouseInCircle(self, mouse_x, mouse_y, circle_x, circle_y, radius):
        try:
            # Fare pozisyonunun daire içinde olup olmadığını kontrol et
            distance = math.sqrt((mouse_x - circle_x) ** 2 + (mouse_y - circle_y) ** 2)
            is_inside = distance <= radius
            if is_inside: return True
            else: return False
        except Exception as ERR:
            print(ERR, " Check Mouse In Circle")

    def GetCircleCollision(self, Object0, Object1, radius):
        try:
            dx = Object0.x  - Object1.x
            dy = Object0.y  - Object1.y
            distance = math.sqrt(dx * dx + dy * dy)
            return distance < radius + radius
        except Exception as ERR:
            print(ERR, " get circle collision")

    # This is all Rectangle Collisions
    def CheckMouseInRectangle(self, mouse_x, mouse_y, rect_x, rect_y, rect_width, rect_height):
        try:
            return rect_x <= mouse_x <= (rect_x + rect_width) and rect_y <= mouse_y <= (rect_y + rect_height)
        except Exception as ERR:
            print(ERR, " Check Mouse In Rectangle")

    def SingleObject_RectangleCollisionCheck(self, Player=0, SingleObject=0, IfHit=""):
        try:
            pTransform = GVector2( self.GetObjectPosition(Object=Player, xOrY='x'), self.GetObjectPosition(Object=Player, xOrY='y') )
            pScale = GVector2( self.GetObjectScale(Object=Player, xOrY='x'), self.GetObjectScale(Object=Player, xOrY='y') )
            if self.DrawList[SingleObject]["active"]:
                SolidTransform = self.DrawList[SingleObject][self.Transform]
                SolidScale = self.DrawList[SingleObject][self.Scale]
                player_box = box(pTransform.x, pTransform.y, pTransform.x + pScale.y, pTransform.y + pScale.y)
                hit_box = box(SolidTransform.x, SolidTransform.y, SolidTransform.x + SolidScale.x, SolidTransform.y + SolidScale.y)
                if player_box.intersects(hit_box):
                    if IfHit != "":
                        IfHit()
                    return True
                else:
                    return False
        except Exception as ERR:
            print(ERR, " Simple object rectangle collision check ERR")

    def MultiObjectCollision(self, Player, ObjectList, DebugMode, IfHitTrue):
        try:
            for i in ObjectList:
                self.Hit0 = self.SingleObject_RectangleCollisionCheck(Player=Player, SingleObject=i, DebugMode=DebugMode, IfHit=IfHitTrue)
        except Exception as ERR:
            print(ERR, "Multi Object Collision ERR...")

    def Mooo(self, Player=0, SolidObjectList=[]):
        try:
            pTransform = GVector2( self.GetObjectPosition(Object=Player, xOrY='x'), self.GetObjectPosition(Object=Player, xOrY='y') )
            pScale = GVector2( self.GetObjectScale(Object=Player, xOrY='x'), self.GetObjectScale(Object=Player, xOrY='y') )
            for i in SolidObjectList:
                if self.DrawList[i]["active"]:
                    SolidTransform = self.DrawList[i][self.Transform]

                    SolidScale = self.DrawList[i][self.Scale]
                    player_box = box(pTransform.x, pTransform.y, pTransform.x + pScale.y, pTransform.y + pScale.y)
                    hit_box = box(SolidTransform.x, SolidTransform.y, SolidTransform.x + SolidScale.x, SolidTransform.y + SolidScale.y)

                    if player_box.intersects(hit_box):
                        self.Hit = True
                        break
                    else: 
                        self.Hit = False
            return self.Hit
        except Exception as ERR:
            print(ERR, " what cow say ERR...")


    # this is simple player control With Wall Collision
    def SimplePlayer2D(self, Event, Keyboard, Player, SolidObjectList):
        try:
            if not self.stop:
                if Event == Keyboard.w:
                    self.MoveObject(Object=Player, WhichDirection="up", XorY='y', Speed=self.speed)
                elif Event == Keyboard.s:
                    self.MoveObject(Object=Player, WhichDirection="down", XorY='y', Speed=self.speed)
                if Event == Keyboard.a:
                    self.MoveObject(Object=Player, WhichDirection="left", XorY='x', Speed=self.speed)
                elif Event == Keyboard.d:
                    self.MoveObject(Object=Player, WhichDirection="right", XorY='x', Speed=self.speed)
            self.Hit1 = self.Mooo(Player=Player, SolidObjectList=SolidObjectList)
            if self.Hit1:
                self.TeleportObject(Object=Player, Position=self.RecordX, XorY='x')
                self.TeleportObject(Object=Player, Position=self.RecordY, XorY='y')
            else:
                self.RecordX = self.GetObjectPosition(Object=Player, xOrY='x')
                self.RecordY = self.GetObjectPosition(Object=Player, xOrY='y')
        except Exception as ERR:
            print(ERR, "2D Player Move ERR...")

    # this is simple way render pipline
    def Draw(self):
        try:
            self.ClearCanvas()
            for i in self.DrawList:
                if self.DrawList[i][self.Active]:
                    if self.DrawList[i]["type"] == 'c':
                        self.RenderCircle(
                            Transform=self.DrawList[i]["transform"],
                            Radius=self.DrawList[i]["radius"],
                            FillColor=self.DrawList[i]["fcolor"],
                            OutLineColor=self.DrawList[i]["ocolor"] )
                    if self.DrawList[i]["type"] == 'r':
                        self.RenderRectangle(
                            Transform=self.DrawList[i]["transform"],
                            Scale=self.DrawList[i]["scale"],
                            FillColor=self.DrawList[i]["fcolor"],
                            OutLineColor=self.DrawList[i]["ocolor"] )
                    if self.DrawList[i]["type"] == 'l':
                        self.RenderLine(
                            Transform=self.DrawList[i]["transform"],
                            Scale=self.DrawList[i]["scale"],
                            Color=self.DrawList[i]["fcolor"],
                            width=self.DrawList[i]["b"] )
                    if self.DrawList[i]["type"] == 't':
                        self.RenderText(
                            Text=self.DrawList[i]["text"],
                            Transform=self.DrawList[i]["transform"],
                            Font=self.DrawList[i]["font"],
                            Size=self.DrawList[i]["scale"],
                            Color=self.DrawList[i]["color"] )
                    if self.DrawList[i]["type"] == 'i':
                        self.RenderImage(
                            Image=self.DrawList[i]["Image"],
                            Transform=self.DrawList[i]["transform"] )
        except Exception as ERR:
            print(ERR, "This is Error")



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

    def PlaySound_MultiChannelLoop(self,  SoundPath="", Loop=True, ChannelID=0, AutoPlayList=False):
        try:
            pygame.mixer.init()
            pygame.mixer.set_num_channels(self.MaxChannelLimit)

            if not self.GiveLength:
                if str(SoundPath.strip(" ")).endswith(".wav") or str(SoundPath.strip(" ")).endswith(".wp3"):
                    audio = AudioSegment.from_file(SoundPath)
                    self.SoundLength = len(audio) / 1000.0
                    self.SoundLength_Backup = self.SoundLength
                    self.GiveLength = True

            if self.SoundLength > 0:
                if not self.PlayAgain:
                    if not AutoPlayList:
                        if Loop:
                            channel = pygame.mixer.Channel(ChannelID)
                            channel.play(pygame.mixer.Sound(SoundPath))
                            channel.set_volume(self.Volume)
                    else:
                        pass
                    self.PlayAgain = True
                self.SoundLength -= 1 * 0.1
            else:
                self.SoundLength = self.SoundLength_Backup
                self.PlayAgain = False
        except Exception as ERR:
            print(ERR, "Play Sound ERR")

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

    def VolumeChange_Gslider(self, Value):
        try:
            VolumeSlider = int(self.GetValue[Value])
            if VolumeSlider != 10:
                self.Volume = float(f"0.{VolumeSlider}")
            else:
                self.Volume = 1
            pygame.mixer.music.set_volume(self.Volume)
        except Exception as ERR:
            print(ERR, "Volume Changer ERR")

