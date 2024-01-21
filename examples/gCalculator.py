from GnuChanGUI import *

gc = GnuChanGUI(Title="GnuChan Program Timer", Size=(230, 455), resizable=False)
Themecolors().GnuChanOS
font = "Sans, 20"

gMenu = [ ["Info", ["GnuChanOS", "Youtube Channel", "Github Page"]], ["System", ["Exit"]] ]

screen = ""
number1 = number2 = ""
mathEnd = 0
mathSymbol = ""
number1Typing = True
manthFinish = False

numbers = ["1","2","3","4","5","6","7","8","9","0","."]
math = ["+","*","-","/","="]

layout = [
    [gc.GMenuForTheme(winMenu=gMenu, font=gc.font)],
    [gc.GText(value="screen", font=font, bcolor=GColors().purple8, xStretch=True)],

    [gc.Push, gc.GButton(title="1", font=font, xStretch=True), gc.GButton(title="2", font=font, xStretch=True), gc.GButton(title="3", font=font, xStretch=True), gc.Push ],
    [gc.Push, gc.GButton(title="4", font=font, xStretch=True), gc.GButton(title="5", font=font, xStretch=True), gc.GButton(title="6", font=font, xStretch=True), gc.Push ],
    [gc.Push, gc.GButton(title="7", font=font, xStretch=True), gc.GButton(title="8", font=font, xStretch=True), gc.GButton(title="9", font=font, xStretch=True), gc.Push ],

    [gc.Push, gc.GButton(title=".", font=font, xStretch=True), gc.GButton(title="0", font=font, xStretch=True), gc.GButton(title="<", font=font, xStretch=True), gc.Push ],

    [gc.Push, gc.GButton(title="=", font=font, xStretch=True),  gc.GButton(title="+", font=font, xStretch=True), gc.GButton(title="-", font=font, xStretch=True), gc.Push ],
    [gc.Push, gc.GButton(title="*", font=font, xStretch=True),  gc.GButton(title="/", font=font, xStretch=True), gc.Push ],

    [gc.Push, gc.GButton(title="GO", font=font, xStretch=True), gc.GButton(title="CLEAR", font=font, xStretch=True), gc.Push ],


    ]

gc.GWindow(mainWindow=layout)

def numberstTyping():
    global number1, number2, numbers, number1Typing
    if number1Typing:
        if gc.event in numbers:
            number1 += gc.event
            gc.window["screen"].update(number1)
    else:
        if gc.event in numbers:
            number2 += gc.event
            gc.window["screen"].update(number2)

def mathFunc():
    global number1, number2, number1Typing, mathEnd, math, manthFinish, mathSymbol
    if number1Typing:
        if gc.event in math:
            mathSymbol = gc.event
            number1Typing = False

    if gc.event == "=":
        if mathSymbol == "+":
            mathEnd = float(number1) + float(number2)
            gc.window["screen"].update(round(mathEnd, 6))
            manthFinish = True                
        if mathSymbol == "-":
            mathEnd = float(number1) - float(number2)
            gc.window["screen"].update(round(mathEnd, 6))
            manthFinish = True                
        if mathSymbol == "*":
            mathEnd = float(number1) * float(number2)
            gc.window["screen"].update(round(mathEnd, 6))
            manthFinish = True                
        if mathSymbol == "/":
            mathEnd = float(number1) / float(number2)
            gc.window["screen"].update(round(mathEnd, 6))
            manthFinish = True

    if gc.event == "<":
        if number1Typing:
            number1 = number1[:-1]
            gc.window["screen"].update(number1)
        else:
            number2 = number2[:-1]
            gc.window["screen"].update(number2)


def clear():
    global number1, number2, number1Typing, manthFinish, mathEnd
    number1 = number2 = ""
    mathEnd = 0
    manthFinish = False
    number1Typing = True
    gc.window["screen"].update("")

def GO():
    global number1, number2, number1Typing, manthFinish, mathEnd
    number1 = str(round(mathEnd, 6))
    number1Typing = True
    number2 = ""
    mathEnd = 0
    manthFinish = False
    gc.window["screen"].update(number1)

def update():
    # gnuchanos pages
    if gc.event == "GnuChanOS":
        webbrowser.open("https://gnuchanos.github.io") 
    elif gc.event == "Youtube Channel":
        webbrowser.open("https://www.youtube.com/channel/ucmjtfic152myx7mbxmghfea")    
    elif gc.event == "Github Page":
        webbrowser.open("https://github.com/gnuchanos")

    global manthFinish
    if not manthFinish:
        numberstTyping()
        mathFunc()
    else:
        if gc.event == "GO":
            GO()

    if gc.event == "CLEAR":
        clear()
        print("test")


gc.update(GUpdate=update)
