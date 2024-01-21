from PySimpleGUI import *
import random
import threading

"""
pip install  git+https://github.com/gnuchanos/gnuchangui
"""

"""
python -m venv ./venv
./venv/bin/activate 
"""

"""
```
python -m PySimpleGUI.PySimpleGUI upgrade
position | left - center - right

font -> font
visible -> visible
readonly -> readonly and  disabled -> readonly
no_scrollbar -> noScroolBar
group_id -> groupID
default_value -> defaultValue

expand_x --> xStretch
expand_y --> yStretch
justification -> position
text_color -> tColor
background_color -> bcolor
border_width -> border
image_filename -> bImage
password_char -> PwChars
ReadyTheme -> more costume color theme
```
"""



# testing Func System
class GFunc():
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def __call__(self):
        self.finished = True
        return self.func(*self.args, **self.kwargs)

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
        self.purple1 = "#7005fc"
        self.purple2 = "#7005fc"
        self.purple3 = "#7005fc"
        self.purple4 = "#4d09a5"
        self.purple5 = "#3c0682"
        self.purple6 = "#33076d"
        self.purple7 = "#220549"
        self.purple8 = "#160230"

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
    


    # Create Window
    def GWindow(self, mainWindow=None, TopMode=False, rightClickMenu=None, locationX=100, locationY=100):
        if mainWindow != None:
            self.layout = mainWindow
            #if mainWindow is None self.layout can warning user and self.layout is ready warning layout
        self.window = Window(self.title, layout=self.layout, size=self.size, keep_on_top=TopMode, resizable=self.resizable, 
                                finalize=self.finalize, right_click_menu=rightClickMenu, return_keyboard_events=True, margins=(0, 0), location=(locationX, locationY))
        self.window.finalize() # this is new for close window good way
        return self.window
        """
        window have right click menu --> ["menu", ["inMenu1", "inMenu2"]]
        """

    def update(self, GUpdate=GFunc(None)):
        while True:
            self.event, self.GetValues = self.window.read(timeout=60)
            if self.event in (WIN_CLOSED, "Exit"):
                break
            if self.closeWindow:
                break
            GUpdate()
        self.window.close() # if loop finish wnidow close
    
    @property
    def close(self):
        self.window.close()

    @property
    def dt(self):
        dt = .05
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

    # key press event
    def GKey(self, GetValues=None, key1="Return", Action=GFunc(None)):
        if key1 == "Return":
            self.window[GetValues].bind("<Return>", "_Enter")
            if self.event == GetValues + "_Enter":
                Action()
        elif key1 == "Tab":
            self.window[GetValues].bind("<Tab>", "+TAB")
            if self.event == GetValues + "+TAB":
                Action()
        """
        def sPrint():
            return gc.window["multiLineText"].update("")
        gc.GKey(GetValues="multiLineText",Action=sPrint,key1="Tab")
        """

    # this is works only input not multiline
    def GInputSelectALL(self, gInputValue):
        self.window[gInputValue].bind("<Control-A>", " CTRL-A", propagate=False)
        self.window[gInputValue].bind("<Control-a>", " CTRL-A", propagate=False)

    def GFocus(self, GetValues=None):
        return self.window[GetValues].set_focus() 
        """
        focus not Finish
        """

    def GLog(self, value=None, font="Sans, 15", size=(None, None), EmptySpace=(None, None), xStretch=False, yStretch=False, visible=True):
        return Output(key=value, font=font, size=size, pad=EmptySpace, expand_x=xStretch, expand_y=yStretch, text_color=None, background_color=None, visible=visible, 
                      autoscroll_only_at_bottom=True)
        """
        I must disable the scrollbar and make it readonly.

        i love this becouse this can show print() in screen
        """

    # ekstra options
    # This setting only works under GWindow. #"this is tk"
    def GListBoxBorderSize(self, border=0, value=None):
        return self.window[value].Widget.configure(borderwidth=border, relief=tk.GROOVE)

    def GSelectionBorderSize(self, border=0, value=None, borderColor=None, highlightcolor=None):
        combo = self.window[value]
        combostyle, style_name = combo.ttk_style, combo.ttk_style_name
        combostyle.configure(style_name, selectbackground=borderColor, selectforeground=highlightcolor, borderwidth=border)

    def GMultilineTabSpace(self, gMultilineFont, gMultilineValue):
        char = Text.char_width_in_pixels(gMultilineFont)
        tabs = (2*char, 'left', 4*char, 'left',)
        multiline = self.window[gMultilineValue]
        multiline.Widget.configure(tabs=tabs)

    # ALL Style Changer
    # Font Size Changer
    def fontSizePlus(self, windowValue=None):
        self.fontSize += 2
        self.window[windowValue].update(font=f"{self.fontName}, {self.fontSize}")
    def fontSizeMinus(self, windowValue=None):
        self.fontSize -= 2
        self.window[windowValue].update(font=f"{self.fontName}, {self.fontSize}")
    def ChangeTextColor(self, textValue, color="white"):
        self.window[textValue].update(text_color=color)
    def ChangeBackgroundColor(self, Value, color="black"):
        self.window[Value].update(background_color=color)

    # window widgets
    def GFrame(self, title=None, winLayout=[[]], value=None, infoWındow=None, border=1, font="Sans, 20", size=(None, None), xStretch=False, yStretch=False, EmptySpace=(None, None), tColor=None, bcolor=None, visible=True):
        return Frame(title=title, layout=winLayout, key=value, border_width=border, tooltip=infoWındow, font=font, size=size, pad=EmptySpace, expand_x=xStretch, expand_y=yStretch, title_color=tColor, background_color=bcolor, visible=visible)
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
        return Column(layout=winColumn, key=value, size=size, expand_x=xStretch, expand_y=yStretch, pad=EmptySpace, visible=visible, background_color=bcolor)
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

    # create Gtab and create GTap Group
    def GTab(self, title, TabLayout=None, value=None, rclickMenu=None):
        return Tab(title=title, layout=TabLayout, key=value, right_click_menu=rclickMenu)

    def GTabGroup(self, TabGroupLayout=None, value=None, font="Sans, 20",
        bcolor=None, sbcolor=None, tbcolor=None, tcolor=None, fcolor=None, stcolor=None, size=(None, None)):
        return TabGroup(layout=TabGroupLayout, key=value, expand_x=True, expand_y=True, size=size,
        background_color=bcolor, selected_background_color=sbcolor, tab_background_color=tbcolor, enable_events=True,
        title_color=tcolor, focus_color=fcolor, selected_title_color=stcolor, font=font, tab_border_width=0, border_width=0)
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
    def GText(self, title="", font="Sans, 20", value=None, size=(None, None), position="left", xStretch=False, yStretch=False, EmptySpace=(None), tColor=None, bcolor=None,
              border=None):
        return Text(text=title, font=font, key=value, size=size, justification=position, expand_x=xStretch, expand_y=yStretch,  pad=EmptySpace, 
                       text_color=tColor, background_color=bcolor, border_width=border)
        """
        gc.GText(value="text")
        gc.window["text"].update("change text")
        """

    # button widget
    def GButton(self, title="", bImage=None, font="Sans, 20", value=None, size=(None, None), visible=True, tcolor=None, bcolor=None, xStretch=False, yStretch=False, EmptySpace=(None), border=None):
        return Button(title, button_color=(bcolor, tcolor), font=font, key=value, size=size, expand_x=xStretch, expand_y=yStretch, pad=EmptySpace, image_filename=bImage, visible=visible, 
                         border_width=border)
        """
        gc.GButton(title="button")
        if gc.event == "button name or value": click event
            gc.window["text"].update(gc.GetValues["textInput"])
        """

    # image
    def GImage(self, image=None, value=None, EmptySpace=(None, None), visible=True, size=[None, None]):
        return Image(filename=image, key=value, pad=EmptySpace, visible=visible, size=size)  
        """
        if gc.event == "imgButton":
            gc.window["img"].update("logo2.png")
        """

    # listbox widget
    def GListBox(self, list=[], font="Sans, 20", value=None, size=(None, None), ActiveEvent=True, visible=True, position="left", EmptySpace=(None, None), noScroolBar=False, 
                 xStretch=False, yStretch=False, tColor=None, bcolor=None):
        return Listbox(list, font=font, key=value, enable_events=ActiveEvent, visible=visible, justification=position, size=size, pad=EmptySpace,
                   no_scrollbar=noScroolBar, expand_x=xStretch, expand_y=yStretch, text_color=tColor, background_color=bcolor)
        """
        [gc.GListBox(value="list", xStretch=True, yStretch=True)],

        if gc.event == "addList":
            for i in range(1, 10):
                testList.append(i)
            gc.window["glist"].update(testList)

        gc.getvalue["glist"][0] # for select
        """
    
    # input widget
    def GInput (self, InText="", font="Sans, 20", value=None, size=(None, None), focus=True, position="left", visible=True, PwChars=False, readonly=False, 
                xStretch=False, yStretch=False, EmptySpace=(None), tcolor=None, bcolor=None, border=None):
        return Input(default_text=InText, font=font, key=value, size=size, focus=focus, justification=position,  pad=EmptySpace, expand_x=xStretch, expand_y=yStretch, 
                        password_char=PwChars, visible=visible, readonly=readonly,  background_color=bcolor, text_color=tcolor, border_width=border)
        """
        [gc.GText(value="text")],
        [gc.GInput(value="input", xStretch=True),  gc.GButton(title="Click", value="button", xStretch=True)],
        if gc.event == "change text":
            gc.window["text"].update(gc.GetValues["textInput"]) #text input value
        """

    # multiLine widget
    def GMultiline (self, InText="", font=None, value=None, size=(None, None), visible=True, position="left", enableEvent=True, WriteOnly=False, wrapLines=True,
                    xStretch=False, yStretch=False, focus=True, readonly=False, noScroolBar=True, EmptySpace=(None, None), tcolor=None, bcolor=None, border=None):
        return Multiline(default_text=InText, font=font, key=value, size=size, focus=focus, justification=position, visible=visible, disabled=readonly, 
                            expand_x=xStretch, expand_y=yStretch, no_scrollbar=noScroolBar, text_color=tcolor, background_color=bcolor, pad=EmptySpace, border_width=border,
                            autoscroll=True, auto_size_text=True, enable_events=enableEvent, write_only=WriteOnly, wrap_lines=wrapLines)
        """
        if gc.event == "addList":
            testList += str(random.randint(0, 50)) + "\n"
            gc.window["glist"].update(testList)
        """
    
    # cheack mark
    def GCheackBox(self, title=None, font="Sans, 20", value=None, EmptySpace=(None, None), tcolor=None, bcolor=None):
        return Checkbox(text=title, font=font, key=value, pad=EmptySpace, text_color=tcolor, background_color=bcolor)
        """
        [gc.GCheackBox(title="Half Life", value="hl"),
        gc.GCheackBox(title="Mafia", value="mf"),
        gc.GCheackBox(title="GTA San Andreas", value="gta"),
        gc.GCheackBox(title="Age Of Empires 2", value="age2")],
        [gc.GButton(title="CheckBox", xStretch=True)]

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

        if gc.event in ["hl1", "hl2", "hl3"]:
            if gc.event == "hl1":
                gc.window["hlGame"].update("can you play half life 1 before ?")
            elif gc.event == "hl2":
                gc.window["hlGame"].update("half life 2 good game")
            elif gc.event == "hl3":
                gc.window["hlGame"].update("there is no half life 3 :(")
        """

    # selections
    def GSelection(self, font="Sans, 20", values=None, defaultValue=None, value=None, EmptySpace=(None, None), visible=True, tcolor=None, bcolor=None, xStretch=False, yStretch=False):
        return Combo(values=values, key=value, default_value=defaultValue, font=font, pad=EmptySpace, visible=visible, text_color=tcolor, background_color=bcolor, expand_x=xStretch, expand_y=yStretch, readonly=True)
        """
        [gc.GSelection(values=[1,2,3,4,5], value="GSelection", defaultValue=1, font=gc.font, xStretch=True)],
        if gc.GetValues["GSelection"]:
                print(gc.GetValues["GSelection"])
        """
    
    def GIncreaseSelection(self, rangeValue=None, startValue=None, value=None, font="Sans, 20", size=(None, None), EmptySpace=(None, None), tcolor=None, bcolor=None, xStretch=False, yStretch=False, Visible=True):
        return Spin(values=rangeValue, initial_value=startValue, font=font, key=value, size=size, pad=EmptySpace, expand_x=xStretch, expand_y=yStretch, text_color=tcolor, background_color=bcolor, visible=Visible)
        """
        [gc.GIncreaseSelection(startValue=1, rangeValue=[1,2,3,4,5], value="GIncreaseSelection", font=gc.font, xStretch=True)],
        if gc.GetValues["GIncreaseSelection"]:
                print(gc.GetValues["GIncreaseSelection"])
        """
    
    def GSlider(self, range=None, value=None, defaultValue=None, font="Sans, 20", size=(None, None), direction="h", EmptySpace=(None, None), tcolor=None, bcolor=None, xStretch=False, yStretch=False, Visible=True):
        return Slider(range=range, key=value, default_value=defaultValue, orientation=direction, font=font, size=size, pad=EmptySpace, text_color=tcolor, background_color=bcolor, expand_x=xStretch, expand_y=yStretch, visible=Visible)   
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





# for multiLine Open/Save/save as
class FileSave:
    def __init__(self, value=None, window=None) -> None:
        self.value = value
        self.window = window
        self.content = None
        self.filename = None
        self.fileOpen = False

    @property
    def Open(self):
            self.filename = popup_get_file('Select a file to open', no_window=True)
            #file path text file path
            # open text file with popup_get_file
            if self.filename:
                with open(self.filename, 'r') as file:
                    self.content = file.read()
                    self.window[self.value].update(self.content)
                    self.fileOpen = True
    @property
    def SaveAs(self):
        self.filename = popup_get_file('Select a file to save', save_as=True, no_window=True)
        if self.filename:
            self.content = self.window[self.value].get()
            with open(self.filename, 'w') as file:
                file.write(self.content)
                self.fileOpen = True

    @property
    def Save(self):
        if self.fileOpen == True:
            self.content = self.window[self.value].get()
            with open(self.filename, 'w') as file:
                file.write(self.content)
    """
    textOpen = FileSave(value="multiLineText", window=gc.window)
    def update():
        if gc.event == "Open File":
            textOpen.Open
        elif gc.event == "Save As":
            textOpen.SaveAs
        elif gc.event == "Save":
            textOpen.save
    """


if __name__ == "__main__":
    gc = GnuChanGUI(Title="", Size=(300, 200), resizable=False, finalize=True)
    Themecolors().GnuChanOS

    layout = [ [gc.GText(title="test", xStretch=True, position="center")] ]

    gc.GWindow(mainWindow=layout)

    def update():
        pass

    gc.update(GUpdate=update)