from PySimpleGUI import *
import os, subprocess, random



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
background_color -> bColor
border_width -> border
image_filename -> bImage
password_char -> PwChars
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


class GColors:
    def __init__(self, colors=0) -> None:
        self.colors = colors

    @property
    def gnuChanColors(self):
        try:
            gnuChanColors = ["#9d4edd", "#240046", "#3c096c", "#5a189a"]
            return gnuChanColors[self.colors-1]
        except IndexError:
            popup(f"There is no much color in here-> {len(gnuChanColors)}")
            
    @property
    def purple(self):
        try:
            purples = ["#10011f", "#220242", "#340463", "#440582", "#5608a3", "#6a0cc7", "#7a10e3", "#8812fc"]
            return purples[self.colors-1]
        except IndexError:
            popup(f"There is no much color in here-> {len(purples)}")
        
    @property
    def blue(self):
        try:
            blues = ["#02011c", "#04023d", "#080469", "#0b068f", "#0d07a8", "#130cc4", "#130be0", "#1108fc"]
            return blues[self.colors-1]
        except IndexError:
            popup(f"There is no much color in here-> {len(blues)}")
 
    @property
    def green(self):
        try:
            greens = ["#013001", "#035703", "#057a05", "#069606", "#09ba09", "#0dd10d", "#0ee60e", "#05fa05"]
            return greens[self.colors-1]
        except IndexError:
            popup(f"There is no much color in here-> {len(greens)}")

class Random:
    @property
    def Color(self):
        randomColor = random.choice(["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#00FFFF", "#FF00FF", "#FFFFFF", "#000000", "#800080", "#FFA500", "#FFC0CB", "#008080", "#FFD700", "#A52A2A", "#FF1493", "#4B0082", "#00FF7F", "#1E90FF", "#FF4500", "#FF69B4"])
        return randomColor


class GnuChanGUI:
    def __init__(self, Title="Defaul Title", Size=(None, None), resizable=False, finalize=True) -> None:
        self.size = Size
        self.title = Title
        self.resizable = resizable
        self.finalize = finalize

        self.fontName = "Sans"
        self.fontSize = 15
        self.font = f"{self.fontName}, {self.fontSize}"

        self.event = None
        self.GetValues = None
    

    def update(self, GUpdate=GFunc(None)):
        while True:
            self.event, self.GetValues = self.window.read(timeout=60)
            if self.event in (WIN_CLOSED, "Exit"):
                break
            GUpdate()
    

    @property
    def close(self):
        self.window.close()


    @property
    def dt(self):
        dt = .05
        return dt


    # Theme
    def Theme(self, themeName="GnuchanTheme", text="#9d4edd", background="#240046", input="#3c096c", text_input="#9d4edd", 
                     scroll="#5a189a", button=('#c77dff', '#3c096c'), progress=('#c77dff', '#3c096c'), 
                     border=0, slider_depth=0, progress_depth=0):
        LOOK_AND_FEEL_TABLE[themeName] = {
                                        'BACKGROUND': background, 'TEXT': text, 'INPUT': input, 'TEXT_INPUT': text_input,
                                        'SCROLL': scroll, 'BUTTON': button, 'PROGRESS': progress, 
                                        'BORDER': border, 'SLIDER_DEPTH': slider_depth, 'PROGRESS_DEPTH': progress_depth}
        theme(themeName)


    # Create Window
    def GWindow(self, mainWindow="Default", TopMode=False, rightClickMenu=None, location=None):
        self.window = Window(self.title, layout=mainWindow, size=self.size, keep_on_top=TopMode, resizable=self.resizable, 
                                finalize=self.finalize, right_click_menu=rightClickMenu, return_keyboard_events=True, margins=(0, 0), location=location)
        return self.window
    """
    window have right click menu --> ["menu", ["inMenu1", "inMenu2"]]
    """


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

    def GWidgetUpdate(self, GWidgetValue=None, getValue=None):
        return self.window[GWidgetValue].update(getValue)
    # getValue change GWidgetValue value


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
    def GListBoxFixer(self, border=0, value=None):
        return self.window[value].Widget.configure(borderwidth=border, relief=tk.GROOVE)
    #GlistBoxFixer Finish
    def GframeFixer(self, value=None, border=1, borderColor="black"):
        return self.window[value].Widget.configure(highlightthickness=border, highlightbackground=borderColor, relief=tk.GROOVE)
    #GFrameFixer Finish
    def GSelectionFixer(self, value=None):
        combo = self.window[value]
        combostyle, style_name = combo.ttk_style, combo.ttk_style_name
        combostyle.configure(style_name, selectbackground=None, selectforeground=None, borderwidth=0)
    #GSelectionFixer border=0
    def GMultilineSpaceFixer(self, value=None):
        char = Text.char_width_in_pixels(self.font)
        tabs = (4*char, 'left', 4*char, 'left')
        multiline = self.window[value]
        multiline.Widget.configure(tabs=tabs)
    #GMultilineSpaceFixer tab space


    # change font size real time
    def fontSizePlus(self, windowValue=None):
        self.fontSize += 2
        self.window[windowValue].update(font=f"{self.fontName}, {self.fontSize}")
    def fontSizeMinus(self, windowValue=None):
        self.fontSize -= 2
        self.window[windowValue].update(font=f"{self.fontName}, {self.fontSize}")


    # window widgets
    def GFrame(self, title=None, winLayout=[[]], value=None, infoWındow=None, border=1, font="Sans, 20", size=(None, None), xStretch=False, yStretch=False, EmptySpace=(None, None), tColor=None, bColor=None, visible=True):
        return Frame(title=title, layout=winLayout, key=value, border_width=border, tooltip=infoWındow, font=font, size=size, pad=EmptySpace, expand_x=xStretch, expand_y=yStretch, title_color=tColor, background_color=bColor, visible=visible)
    """
    test1 = [[default.GMenuForTheme(winMenu=gMenu, font=defaultFont)],
             [default.GText("test", xStretch=True, position="center")]]
    test2 = [[default.GMenuForTheme(winMenu=gMenu, font=defaultFont)],
             [default.GText("test", xStretch=True, position="center")]]
    test3 = [[default.GMenuForTheme(winMenu=gMenu, font=defaultFont)],
             [default.GText("test", xStretch=True, position="center")]]
    test4 = [[default.GMenuForTheme(winMenu=gMenu, font=defaultFont)],
             [default.GText("test", xStretch=True, position="center")]]

    layout = [
        [default.GFrame(winLayout=test1, value="test1", xStretch=True, yStretch=True, bColor=GColors(colors=1).blues()),
         default.GFrame(winLayout=test2, value="test2", xStretch=True, yStretch=True, bColor=GColors(colors=1).blues())],
        [default.GFrame(winLayout=test3, value="test3", xStretch=True, yStretch=True, bColor=GColors(colors=1).blues()),
         default.GFrame(winLayout=test4, value="test4", xStretch=True, yStretch=True, bColor=GColors(colors=1).blues())]]

    default.GWindow(mainWindow=layout)
    """


    def GColumn(self, winColumn=None, xStretch=None, yStretch=None, EmptySpace=(None, None), visible=True, value=None, bcolor=None):
        return Column(layout=winColumn, key=value, expand_x=xStretch, expand_y=yStretch, pad=EmptySpace, visible=visible, background_color=bcolor)
    """
    TopLayer = [[default.GText(title="Top Layer", position="center", font="Sans, 20", bColor=GColors(colors=1).blues(), xStretch=True, yStretch=True, EmptySpace=(0,0))]]
    MiddleLeftLayer = [[default.GText(title="Middle Left", position="center", font="Sans, 20",bColor=GColors(colors=1).greens(), xStretch=True, yStretch=True, EmptySpace=(0,0))]]
    MiddleRightLayer = [[default.GText(title="Middle Right", position="center", font="Sans, 20", bColor=GColors(colors=1).purples(), xStretch=True, yStretch=True, EmptySpace=(0,0))]]
    BottomLayer = [[default.GText(title="Bottom Layer", position="center", font="Sans, 20", bColor=GColors(colors=5).blues(), xStretch=True, yStretch=True, EmptySpace=(0,0))]]

    layout = [
        [default.GColumn(TopLayer, xStretch=True, yStretch=True)],
        [default.GColumn(MiddleLeftLayer, xStretch=True, yStretch=True), 
         default.GColumn(MiddleRightLayer, xStretch=True, yStretch=True)],
        [default.GColumn(BottomLayer, xStretch=True, yStretch=True)] ]
    """


    # create Gtab and create GTap Group
    def GTab(self, title, TabLayout=None, value=None):
        return Tab(title, layout=TabLayout, key=value)
    def GTabGroup(self, TabGroupLayout=None, value=None):
        return TabGroup(layout=TabGroupLayout, key=value, expand_x=True, expand_y=True)
    """
    tab1 = [[default.GText(title="tab1", font=defaultFont, bColor="black", xStretch=True)]]
    tab2 = [[default.GText(title="tab2", font=defaultFont, bColor="black", xStretch=True)]]
    layout = [
        [default.GTabGroup( TabGroupLayout=[[
            default.GTab(title="tab1", TabLayout=tab1),
            default.GTab(title="tab2", TabLayout=tab2),
            
            ]] )]
    ],
    """   


# All Widgets
    # text widget
    def GText(self, title="", font="Sans, 20", value=None, size=(None, None), position="left", xStretch=False, yStretch=False, EmptySpace=(None), tColor=None, bColor=None,
              border=None):
        return Text(text=title, font=font, key=value, size=size, justification=position, expand_x=xStretch, expand_y=yStretch,  pad=EmptySpace, 
                       text_color=tColor, background_color=bColor, border_width=border)
    """
    gc.window["text"].update()
    """
    

    # button widget
    def GButton(self, title="", bImage=None, font="Sans, 20", value=None, size=(None, None), visible=True, tcolor=None, bcolor=None, xStretch=False, yStretch=False, EmptySpace=(None), border=None):
        return Button(title, button_color=(bcolor, tcolor), font=font, key=value, size=size, expand_x=xStretch, expand_y=yStretch, pad=EmptySpace, image_filename=bImage, visible=visible, 
                         border_width=border)
    """
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
                 xStretch=False, yStretch=False, tColor=None, bColor=None):
        return Listbox(list, font=font, key=value, enable_events=ActiveEvent, visible=visible, justification=position, size=size, pad=EmptySpace,
                   no_scrollbar=noScroolBar, expand_x=xStretch, expand_y=yStretch, text_color=tColor, background_color=bColor)
    """
    if gc.event == "addList":
        for i in range(1, 10):
            testList.append(i)
        gc.window["glist"].update(testList)
    """
    

    # input widget
    def GInput (self, InText="", font="Sans, 20", value=None, size=(None, None), focus=True, position="left", visible=True, PwChars=False, readonly=False, 
                xStretch=False, yStretch=False, EmptySpace=(None), tcolor=None, bcolor=None, border=None):
        return Input(default_text=InText, font=font, key=value, size=size, focus=focus, justification=position,  pad=EmptySpace, expand_x=xStretch, expand_y=yStretch, 
                        password_char=PwChars, visible=visible, readonly=readonly,  background_color=bcolor, text_color=tcolor, border_width=border)
    """
    if gc.event == "change text":
        gc.window["text"].update(gc.GetValues["textInput"]) #text input value
    """
    

    # multiLine widget
    def GMultiline (self, InText="", font=None, value=None, size=(None, None), visible=True, position="left", 
                    xStretch=False, yStretch=False, focus=True, readonly=False, noScroolBar=True, EmptySpace=(None, None), tcolor=None, bcolor=None, border=None):
        return Multiline(default_text=InText, font=font, key=value, size=size, focus=focus, justification=position, visible=visible, disabled=readonly, 
                            expand_x=xStretch, expand_y=yStretch, no_scrollbar=noScroolBar, text_color=tcolor, background_color=bcolor, pad=EmptySpace, border_width=border,
                            autoscroll=True, enable_events=True, auto_size_text=True)
    """
    if gc.event == "addList":
        testList += str(random.randint(0, 50)) + "\n"
        gc.window["glist"].update(testList)
    """
    
    
    # cheack mark
    def GCheack(self, title=None, font="Sans, 20", value=None, EmptySpace=(None, None), tcolor=None, bcolor=None):
        return Checkbox(text=title, font=font, key=value, pad=EmptySpace, text_color=tcolor, background_color=bcolor)
    """
    if gc.event == "checkbox":
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
    if gc.GetValues["GSlider1"]:
            gc.window["health"].update(gc.GetValues["GSlider1"])
                health progressbar       slider is give value
    """




    # littile things
    @property
    def Push(self):
        return Push()
    @property
    def hsep(self):
        return HSeparator(color="purple")
    @property
    def vsep(self):
        return VSeparator(color="purple")
    def GMessage(self, message=None, wmTitle="default Window", font="Sans, 15", tcolor=None, bcolor=None):
        return popup(message, title=wmTitle, font=font, text_color=tcolor, background_color=bcolor)




# for multiLine Open/Save As 
class FileSave:
    def __init__(self, value=None, filepath=None, getValue=None, window=None) -> None:
        self.value = value
        self.filepath = filepath
        self.getValue = getValue
        self.window = window

        self.content = None
        self.filename = None

        self.fileOpen = False

    @property
    def Open(self):
            self.filename = popup_get_file('Select a file to open', no_window=True)
            #file path text file path
            if self.filepath != None:
                self.window[self.filepath].update(self.filename)
            # open text file with popup_get_file
            if self.filename:
                with open(self.filename, 'r') as file:
                    self.content = file.read()
                    self.window[self.value].update(self.content)
                    self.fileOpen = True
    @property
    def SaveAs(self):
        self.filename = popup_get_file('Select a file to save', save_as=True, no_window=True)
        if self.filepath != None:
            self.window[self.filepath].update(self.filename)
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
textOpen = FileSave(getValue="multiLineText", value="multiLineText", filepath="textPath", window=gc.window)
def update():
    if gc.event == "Open File":
        textOpen.Open
    elif gc.event == "Save As":
        textOpen.SaveAs
    elif gc.event == "Save":
        textOpen.save
        print(textOpen.filepath, " | ")
"""


