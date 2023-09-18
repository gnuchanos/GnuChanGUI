from GnuChanGUI import *

gc = GnuChanGUI(Title="GnuChan Program Timer", Size=(1024, 600), resizable=True)
gc.Theme()

gMenu = [
    ["Info", ["GnuChanOS", "Youtube Channel", "Github Page"]],
    ["System", ["Exit"]] ]

gLeftColumn = [[gc.GText(title="Left", xStretch=True, position="center", bColor="red")]]
gRightColumn = [[gc.GText(title="Right", xStretch=True, position="center", bColor="green")]]
gBottomColumn = [[gc.GText(title="Bottom", xStretch=True, position="center", bColor="yellow")]]

gNormalWinLayout = [
    [gc.GColumn(winColumn=gLeftColumn, xStretch=True, bcolor="red"), gc.GColumn(winColumn=gRightColumn, xStretch=True, bcolor="green")],
    [gc.GColumn(winColumn=gBottomColumn, xStretch=True, bcolor="yellow")],
    [gc.GText(title="This is Tab2 Text")]
]

# this is all be tab
gFrameTab1 = [
    [gc.GText(title="This is Tab1 Text", value="TextChangerValue"),
     gc.GButton(title="Click This Show Message", value="ButtonDontNeedValue")],
    
    [gc.GText(title="Input: ", EmptySpace=(None, 0)), gc.GInput(value="UserInput", EmptySpace=(None, 0))],
    
    [gc.GImage(image="img/ram.png"), gc.Push, gc.GImage(image="img/rem.png")],
    
    [gc.GListBox(list=["half Life 3", "Left 4 Dead 3", "Portal 3", "gabe newell Fear 3"], size=(None, 2), xStretch=True)],
    
    [gc.GText(title="MultiLine: ", EmptySpace=(None, 0)),
     gc.GMultiline(value="MultiLıneValue", size=(None, 2), xStretch=True)],
    
    [gc.GCheack(title="Half Life 3 ??", value="TrueFalseValue"), gc.GRadio(title="Earth is Flat?", value="TrueFalseValue2")],
    
    [gc.GSelection(values=(1,2,3,4,5), defaultValue=1, value="SelectVale")],
    
    [gc.GIncreaseSelection(rangeValue=(1,2,3,4,5), startValue=1, value="ChangeValue")],
    
    [gc.GSlider(direction="h", defaultValue=1, range=(1,10), value="SliderChangeValue")],
    
    [gc.hsep],
    
    [gc.GProgressBar(direction="h", value="BarValue", MaxValue=10), gc.vsep, gc.GButton(title="Slider Change ProgressBar")]

]
gFrameTab2 = [
    [gc.GFrame(winLayout=gNormalWinLayout, bColor="black", xStretch=True)]
]

# this is all tab
gTabGroup = [
    [gc.GTab(TabLayout=gFrameTab1, title="Frame Tab1")],
    [gc.GTab(TabLayout=gFrameTab2, title="Frame Tab2")]
]

layout = [
    [gc.GMenuForTheme(winMenu=gMenu, font=gc.font)],
    [gc.GTabGroup(TabGroupLayout=gTabGroup)],
    ]

gc.GWindow(mainWindow=layout)
# all change use ( window[] ) settings
gc.GSelectionFixer(value="SelectVale")

def update():
    if gc.event == "GnuChanOS":
        webbrowser.open("https://gnuchanos.itch.io/")
    if gc.event == "Youtube Channel":
        webbrowser.open("https://www.youtube.com/@GnuChanOS")
    if gc.event == "Github Page":
        webbrowser.open("https://github.com/gnuchanos")
    if gc.event == "Slider Change ProgressBar":
        number = gc.GetValues["SliderChangeValue"]
        gc.window["BarValue"].update(number)
    if gc.event == "ButtonDontNeedValue":
        gc.GMessage(message="Nice Work :)", wmTitle="nice Mesagge")

gc.update(GUpdate=update)