import PySimpleGUI as sg
import os, subprocess


# python -m PySimpleGUI.PySimpleGUI upgrad
# position | left - center - right

# font -> font
# visible -> visible
# readonly -> readonly and  disabled -> readonly
# no_scrollbar -> noScroolBar
# group_id -> groupID
# default_value -> defaultValue

# expand_x --> xStretch
# justification -> position
# text_color -> tColor
# background_color -> bColor
# border_width -> border
# image_filename -> bImage
# password_char -> PwChars


class GnuChanGUI:
    def __init__(self, Title="Defaul Title", Size=(None, None), resizable=False, finalize=True) -> None:
        self.size = Size
        self.title = Title
        self.resizable = resizable
        self.finalize = finalize
    
    # Theme
    def Theme(self, themeName="GnuchanTheme", text="#9d4edd", background="#240046", input="#3c096c", text_input="#9d4edd", 
                     scroll="#5a189a", button=('#c77dff', '#3c096c'), progress=('#c77dff', '#3c096c'), 
                     border=0, slider_depth=0, progress_depth=0):
        sg.LOOK_AND_FEEL_TABLE[themeName] = {
                                        'BACKGROUND': background, 'TEXT': text, 'INPUT': input, 'TEXT_INPUT': text_input,
                                        'SCROLL': scroll, 'BUTTON': button, 'PROGRESS': progress, 
                                        'BORDER': border, 'SLIDER_DEPTH': slider_depth, 'PROGRESS_DEPTH': progress_depth}
        sg.theme(themeName)



    # Create Window
    def GWindow(self, mainWindow="Default", TopMode=False, rightClickMenu=None):
        self.window = sg.Window(self.title, layout=mainWindow, size=self.size, keep_on_top=TopMode, resizable=self.resizable, 
                                finalize=self.finalize, right_click_menu=rightClickMenu, return_keyboard_events=True) 
    """
    menu = ['file', ['open', 'save', 'exit']] ---> right_click_menu = menu
    """
    def GLog(self, value=None, font="Sans, 20", size=(None, None), EmptySpace=(None, None), xStretch=False, yStretch=False, visible=True):
        return sg.Output(key=value, font=font, size=size, pad=EmptySpace, expand_x=xStretch, expand_y=yStretch, text_color=None, background_color=None, visible=visible)


# note class.window["str"].update(values["test"])
# event, GetValues = default.window.read(timeout=60) # ı use GetValues --> value --> key


# ekstra options
    # This setting only works under GWindow. #"this is tk"
    def GListBoxFixer(self, border=None, value=None):
        return self.window[value].Widget.configure(borderwidth=border, relief=sg.tk.GROOVE)
    def GSelectionFixer(self, windowCall=None, value=None, GSBorder=1, SelectBcolor=None, SelectTcolor=None):
        combo = windowCall[value]
        combostyle, style_name = combo.ttk_style, combo.ttk_style_name
        combostyle.configure(style_name, selectbackground=SelectBcolor, selectforeground=SelectTcolor, borderwidth=GSBorder)

    # window widgets
    def GFrame(self, title=None, winLayout=[[]], infoWındow=None, font="Sans, 20", size=(None, None), xStretch=False, yStretch=False, EmptySpace=(None, None), tColor=None, bColor=None, visible=True):
        return sg.Frame(title=title, layout=winLayout, tooltip=infoWındow, font=font, size=size, pad=EmptySpace, expand_x=xStretch, expand_y=yStretch, title_color=tColor, background_color=bColor, visible=visible)
    """
            dlayout = [ [ sg.Text("test") ] ]

            layout = [ 
                [sg.Text("this is test")],
                [sg.Frame(title="test", layout=dlayout)]  
                
                
                ]
    """

    def GColumn(self, winColumn=None, xStretch=None, yStretch=None, EmptySpace=(None, None), visible=True, value=None, bcolor=None):
        return sg.Column(layout=winColumn, key=value, expand_x=xStretch, expand_y=yStretch, pad=EmptySpace, visible=visible, background_color=bcolor)
    
    # create Gtab and create GTap Group
    def GTab(self, title, TabLayout=None, value=None):
        return sg.Tab(title, layout=TabLayout, key=value)
    def GTabGroup(self, TabGroupLayout=None, value=None):
        return sg.TabGroup(layout=TabGroupLayout, key=value)
    """
        tab1_layout = [[sg.Text('This is the first tab')]]
        tab2_layout = [[sg.Text('This is the second tab')]]
        tabgroup_layout = [ [GTab('Tab 1', tab1_layout, key="tab1")], [GTab('Tab 2', tab2_layout, key="tab2")] ]
        window_layout = [ [GTabGroup(tabgroup_layout, key="tabgroup")] ]
    """

    def GMenu(self, winMenu=None, tcolor=None, bcolor=None):
        return sg.Menu(menu_definition=winMenu, background_color=bcolor, text_color=tcolor)
    """
    menu_def = [
        ['&File', ['&Open', '&Save', '---', '&Close']],
        ['&Edit', ['&Undo', '&Redo', '---', '&Cut', '&Copy', '&Paste', '&Delete', '---', '&Select All']]
            ]
    layout = [[GMenu(menu_def)]]
    """

# All Widgets
    # text widget
    def GText(self, title="", font="Sans, 20", value=None, size=(None, None), position="left", xStretch=False, yStretch=False, EmptySpace=(None), tColor=None, bColor=None,
              border=None):
        
        return sg.Text(text=title, font=font, key=value, size=size, justification=position, expand_x=xStretch, expand_y=yStretch,  pad=EmptySpace, 
                       text_color=tColor, background_color=bColor, border_width=border)

    # button widget
    def GButton(self, title="", bImage=None, font="Sans, 20", value=None, size=(None, None), visible=True, xStretch=False, yStretch=False, EmptySpace=(None), border=None):
        return sg.Button(title, font=font, key=value, size=size, expand_x=xStretch, expand_y=yStretch, pad=EmptySpace, image_filename=bImage, visible=visible, 
                         border_width=border)

    # input widget
    def GInput (self, InText="", font="Sans, 20", value=None, size=(None, None), focus=True, position="left", visible=True, PwChars=False, readonly=False, 
                xStretch=False, yStretch=False, EmptySpace=(None), tcolor=None, bcolor=None, border=None):
        return sg.Input(default_text=InText, font=font, key=value, size=size, focus=focus, justification=position,  pad=EmptySpace, expand_x=xStretch, expand_y=yStretch, 
                        password_char=PwChars, visible=visible, readonly=readonly,  background_color=bcolor, text_color=tcolor, border_width=border)

    # multiLine widget
    def GMultiline (self, InText="", font=None, value=None, size=(None, None), visible=True, position="left", 
                    xStretch=False, yStretch=False, focus=True, readonly=False, noScroolBar=True, EmptySpace=(None, None), tcolor=None, bcolor=None, border=None):
        return sg.Multiline(default_text=InText, font=font, key=value, size=size, focus=focus, justification=position, visible=visible, disabled=readonly, 
                            expand_x=xStretch, expand_y=yStretch, no_scrollbar=noScroolBar, text_color=tcolor, background_color=bcolor, pad=EmptySpace, border_width=border)


    # image
    def GImage(self, image=None, value=None, EmptySpace=(None, None), visible=True, size=[None, None]):
        return sg.Image(filename=image, key=value, pad=EmptySpace, visible=visible, size=size)
    # listbox widget
    def GListBox(self, list=[], font="Sans, 20", value=None, size=(None, None), ActiveEvent=True, visible=True, position="left", EmptySpace=(None, None), noScroolBar=False, 
                 xStretch=False, yStretch=False, tColor=None, bColor=None):
        return sg.Listbox(list, font=font, key=value, enable_events=ActiveEvent, visible=visible, justification=position, size=size, pad=EmptySpace,
                   no_scrollbar=noScroolBar, expand_x=xStretch, expand_y=yStretch, text_color=tColor, background_color=bColor)



    # cheack mark
    def GCheack(self, title=None, font="Sans, 20", value=None, EmptySpace=(None, None), tcolor=None, bcolor=None):
        return sg.Checkbox(text=title, font=font, key=value, pad=EmptySpace, text_color=tcolor, background_color=bcolor)
    def GRadio(self, title=None, font="Sans, 20", groupID=None, value=None, cEvent=True, EmptySpace=(None, None), tcolor=None, bcolor=None):
        return sg.Radio(text=title, font=font, group_id=groupID, key=value, enable_events=cEvent, pad=EmptySpace, text_color=tcolor, background_color=bcolor)
    """
    default.GRadio(title="uWu", value="uWu", groupID="b1")
    if event == "Finish":
            for color in ["ıWı", "oWo", "uWu"]:
                if GetValues[color]:
                    default.window['str'].update(color)
    """



    # selections
    def GSelection(self, font="Sans, 20", values=None, defaultValue=None, value=None, EmptySpace=(None, None), visible=True, tcolor=None, bcolor=None, xStretch=False, yStretch=False):
        return sg.Combo(values=values, key=value, default_value=defaultValue, font=font, pad=EmptySpace, visible=visible, text_color=tcolor, background_color=bcolor, expand_x=xStretch, expand_y=yStretch, readonly=True)
    """
    if event == 'Finish':
        selected_fruit = GetValues['-FRUIT-']
        sg.popup(f'Seçilen meyve: {selected_fruit}')
    """
    def GIncreaseSelection(self, rangeValue=None, startValue=None, value=None, font="Sans, 20", size=(None, None), EmptySpace=(None, None), tcolor=None, bcolor=None, xStretch=False, yStretch=False, Visible=True):
        return sg.Spin(values=rangeValue, initial_value=startValue, font=font, key=value, size=size, pad=EmptySpace, expand_x=xStretch, expand_y=yStretch, text_color=tcolor, background_color=bcolor, visible=Visible)
    """
    [default.Text(key="number"), default.Spin(values=[i for i in range(10)], initial_value=5, key="uWu", expand_x=True, font="Sans, 20")],
    [default.Button("Finish")],

    if event == "Finish":
        fStrimg = f"Number: {GetValues['uWu']}"
        default.window["number"].update(fStrimg)
    """
    def GSlider(self, range=None, value=None, defaultValue=None, font="Sans, 20", size=(None, None), direction="h", EmptySpace=(None, None), tcolor=None, bcolor=None, xStretch=False, yStretch=False, Visible=True):
        return sg.Slider(range=range, key=value, default_value=defaultValue, orientation=direction, font=font, size=size, pad=EmptySpace, text_color=tcolor, background_color=bcolor, expand_x=xStretch, expand_y=yStretch, visible=Visible)
    """
    [default.Slider(range=(0, 100), orientation='v', key="health", size=(20, 15), default_value=100)],
    if event == 'Finish':
        health = GetValues["health"]
    """
    # [sg.Output(size=(40, 10), key="-OUTPUT-")]



# Ekstra
    def GProgressBar(self, MaxValue=None, value=None, visible=True, direction="h"):
            return sg.ProgressBar(max_value=MaxValue, key=value, visible=visible, orientation=direction)
    """
        if healthFalse == True:
            if health <= 100:
                health -= 0.1
                window['progressbar'].update_bar(health)
            else:
                print("finish")
                healthFalse = False
        else:
            pass
    """
    def Push(self):
        return sg.Push()
    def hsep(self):
        return sg.HSeparator(color="purple")
    def vsep(self):
        return sg.VSeparator()
    def GMessage(self, message=None, wmTitle="default Window", font="Sans, 15", tcolor=None, bcolor=None):
        return sg.popup(message, title=wmTitle, font=font, text_color=tcolor, background_color=bcolor)
    def GMusic(self, SounFile=None, play=False):
        if os.path.isfile(SounFile):
            if play == True:
                if os.name == 'nt':  # Windows
                    os.system('start "" "{}"'.format(sound_file_path))
                elif os.name == 'posix':  # Linux
                    os.system('mpg123 "{}" &'.format(SounFile))
            else:
                if os.name == 'nt':  # Windows
                    os.system('taskkill /IM wmplayer.exe /F')
                elif os.name == 'posix':  # Linux
                    os.system('killall mpg123')
        else:
            print("Hata: {} dosyası bulunamadı!".format(SounFile))