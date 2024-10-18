"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""


from GnuChanGUI import *


if __name__ == "__main__":
    gc = GnuChanGUI(Title="Simple Calculator", Size=(350, 470), resizable=False, finalize=True)
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
    ]

    layout = [
        [ gc.GText(xStretch=True) ],
        [ 
            gc.GText(yStretch=True, xStretch=True),
            gc.GColumn(winColumn=window, xStretch=True, yStretch=True),
            gc.GText(yStretch=True, xStretch=True),
        ],
        [ gc.GText(xStretch=True) ],
    ],

    gc.GWindow(mainWindow=layout)

    def buttonMath():
        global number1, number2, mathFinish, number1Typing, numbers, mathSymbol, mathEnd, mathStarter, log

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


            # Assign The Math Result to Number1 and Keep Doing Math.
            if gc.event == "GO":
                number1Typing = True
                mathFinish = False
                number1 = str(mathEnd)
                number2 = mathStarter = ""
                gc.window["math"].update(number1)


        # clean everything
        if gc.event == "CLEAN":
            mathFinish = False
            number1Typing = True
            number1 = number2 = mathStarter = ""
            mathEnd = 0
            print(f"{number1} | {number2} | {mathEnd}")
            gc.window["math"].update("Let's Start Math")


    mathNumberList = []
    mathMathEnd = 0
    mathEnd = False
    number = ""

    def update():
        buttonMath()

    def BeforeExit():
        pass

    gc.update(GUpdate=update, exitBEFORE=BeforeExit, timeout=0)

