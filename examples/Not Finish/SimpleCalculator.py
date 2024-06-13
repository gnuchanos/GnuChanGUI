"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""


from GnuChanGUI import *
from threading import Thread





#Thread(target=DownloadVideo, args=[]).start()



if __name__ == "__main__":
    gc = GnuChanGUI(Title="", Size=(750, 700), resizable=False, finalize=True)
    gc.font = "Sans, 20"
    Themecolors().GnuChanOS
    clr = GnuChanOSColor()

    number1 = number2 = ""
    mathFinish = False
    number1Typing = True
    numbers = ["0","1","2","3","4","5","6","7","8","9","."]
    mathSymbol = ["+", "-", "*", "/"]
    mathStarter = ""
    mathEnd = 0


    window = [
        [ gc.GText(title="Let's Start Math", value="math", xStretch=True, position="center", bcolor=clr.colors0) ],
            [ 
                gc.GButton(title="1", xStretch=True, size=(2, None)), 
                gc.GButton(title="2", xStretch=True, size=(2, None)), 
                gc.GButton(title="3", xStretch=True, size=(2, None)), 
                gc.GButton(title="+", xStretch=True, size=(5, None))
            ],
            [ 
                gc.GButton(title="4", xStretch=True, size=(2, None)), 
                gc.GButton(title="5", xStretch=True, size=(2, None)), 
                gc.GButton(title="6", xStretch=True, size=(2, None)), 
                gc.GButton(title="-", xStretch=True, size=(5, None)) 
            ],
            [ 
                gc.GButton(title="7", xStretch=True, size=(2, None)), 
                gc.GButton(title="8", xStretch=True, size=(2, None)), 
                gc.GButton(title="9", xStretch=True, size=(2, None)), 
                gc.GButton(title="*", xStretch=True, size=(5, None))
            ],
            [ 
                gc.GButton(title="<", xStretch=True, size=(2, None)), 
                gc.GButton(title="0", xStretch=True, size=(2, None)), 
                gc.GButton(title=".", xStretch=True, size=(2, None)), 
                gc.GButton(title="/", xStretch=True, size=(5, None))
            ],
            [
                gc.GButton(title="CLEAN", xStretch=True),
                gc.GButton(title="GO", xStretch=True),
            ],
            [ gc.GButton(title="=", xStretch=True) ],
            [ gc.GText(bcolor=clr.colors0, xStretch=True) ],
            [ gc.GMultiline(value="console", xStretch=True, yStretch=True, readonly=True) ],
            [ gc.GText(bcolor=clr.colors0, xStretch=True) ],
    ]

    rightWindow = [
        [ gc.GText(title="Let's Start Math", value="mathInput", xStretch=True, position="center", bcolor=clr.colors0) ],
        [ gc.GInput(value="number", size=(25, None)) ],
            [ gc.GText(bcolor=clr.colors0, xStretch=True) ],
        [
            gc.GButton(title="+", value="Addition", xStretch=True, size=(2, None)), 
            gc.GButton(title="-", value="Subtraction", xStretch=True, size=(2, None)),
            gc.GButton(title="*", value="Multiplication", xStretch=True, size=(2, None)), 
            gc.GButton(title="/", value="Division", xStretch=True, size=(2, None)),
        ],
            [ gc.GText(bcolor=clr.colors0, xStretch=True) ],
        [
            gc.GButton(title="Remove", value="delete", xStretch=True),
            gc.GButton(title="Clean", value="clearMAN", xStretch=True),
        ],
            [ gc.GText(bcolor=clr.colors0, xStretch=True) ],
        [ gc.GListBox(value="math-multi", xStretch=True, yStretch=True, noScroolBar=True) ],
            [ gc.GText(bcolor=clr.colors0, xStretch=True) ],
    ]

    layout = [
        [ gc.GText(xStretch=True) ],
        [ 
            gc.GText(yStretch=True, xStretch=True),
            gc.GColumn(winColumn=window, xStretch=True, yStretch=True),
            gc.GText(yStretch=True, xStretch=True),
            gc.GColumn(winColumn=rightWindow, xStretch=True, yStretch=True),
            gc.GText(yStretch=True, xStretch=True),
        ],
        [ gc.GText(xStretch=True) ],
        [ gc.GText(title="Let's Start Math", value="onlyinput", xStretch=True, position="center", bcolor=clr.colors0) ],
        [ gc.GInput(value="only-input", xStretch=True)]
    ],

    gc.GWindow(mainWindow=layout)
    gc.GListBoxBorderSize(value="math-multi", border=0)

    def buttonMath():
        global number1, number2, mathFinish, number1Typing, numbers, mathSymbol, mathEnd, mathStarter

        if not mathFinish:
            # add numbers in number1 or number2
            if gc.event in numbers:
                if number1Typing:
                    number1 += gc.event
                    gc.window["math"].update(number1)
                else:
                    number2 += gc.event
                    gc.window["math"].update(number2)
            # remove number in number1 or number2
            if number1Typing:
                if gc.event == "<":
                    number1 = number1[:-1]
                    gc.window["math"].update(number1)
            else:
                if gc.event == "<":
                    number2 = number2[:-1]
                    gc.window["math"].update(number2)
                # finish math
                if gc.event == "=":
                    mathFinish = True

            # number1 -> number2
            if gc.event in mathSymbol:
                if number1Typing:
                    number1Typing = False
                    mathStarter = gc.event
        else:
            # end math
            if mathStarter == "+":
                mathEnd = float(number1) + float(number2)
                gc.window["math"].update(round(mathEnd, 5))
            elif mathStarter == "-":
                mathEnd = float(number1) - float(number2)
                gc.window["math"].update(round(mathEnd, 5))
            elif mathStarter == "*":
                mathEnd = float(number1) * float(number2)
                gc.window["math"].update(round(mathEnd, 5))
            elif mathStarter == "/":
                mathEnd = float(number1) / float(number2)
                gc.window["math"].update(round(mathEnd, 5))

            # clean everything
            if gc.event == "CLEAN":
                number1 = number2 = mathStarter = ""
                mathEnd = 0
                gc.window["math"].update("Let's Start Math")
                number1Typing = True; mathFinish = False

            # Assign The Math Result to Number1 and Keep Doing Math.
            if gc.event == "GO":
                number1 = str(mathEnd)
                number2 = ""
                mathStarter = ""
                gc.window["math"].update(number1)
                number1Typing = True; mathFinish = False


    mathNumberList = []
    mathMathEnd = 0
    mathEnd = False
    number = ""

    def inputMath():
        global mathNumberList, mathEnd, number, mathMathEnd
        if gc.event == "Return:36":
            try:
                number = float(gc.GetValues["number"])
                mathNumberList.append(number)
                gc.window["math-multi"].update(mathNumberList)
                gc.window["number"].update("")
            except ValueError:
                print("Only Numbers")
            gc.window["onlyinput"].update(round(eval(gc.GetValues["only-input"]), 5))

        if not mathEnd:
            if len(mathNumberList) > 2:
                if gc.event == "Addition":
                    print("works +")
                    for i in mathNumberList:
                        mathMathEnd += i
                        print(mathMathEnd, " | ")
                        mathEnd = True
                elif gc.event == "Subtraction":
                    print("works -")
                    for i in mathNumberList:
                        mathMathEnd -= i
                        print(mathMathEnd, " | ")
                        mathEnd = True
                elif gc.event == "Multiplication":
                    print("works *")
                    for i in mathNumberList:
                        mathMathEnd *= i
                        print(mathMathEnd, " | ")
                        mathEnd = True
                elif gc.event == "Division":
                    print("works /")
                    for i in mathNumberList:
                        mathMathEnd /= i
                        print(mathMathEnd, " | ")
                        mathEnd = True

        if gc.event == "delete":
            print("works")
            try:
                select = gc.GetValues["math-multi"][0]
                print(select)
                mathNumberList.remove(select)
                gc.window["math-multi"].update(mathNumberList)
            except IndexError:
                print("Empty Selection!")

        if gc.event == "clearMAN":
            mathNumberList = []
            gc.window["math-multi"].update(mathNumberList)
            gc.window["mathInput"].update("Let's Start Math")
            gc.window["number"].update("")
            mathEnd = False

    def update():
        Thread(target=buttonMath, args=[]).start()
        Thread(target=inputMath, args=[]).start()


    gc.update(GUpdate=update)