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
        [ gc.GText(SetText="Let's Start Math", TextValue="math", xStretch=True, TPosition="center", BColor=clr.colors0) ],
            [ 
                gc.GButton(Text="1", xStretch=True, Size=(2, None)), 
                gc.GButton(Text="2", xStretch=True, Size=(2, None)), 
                gc.GButton(Text="3", xStretch=True, Size=(2, None)), 
                gc.GButton(Text="+", xStretch=True, Size=(5, None))
            ],
            [ 
                gc.GButton(Text="4", xStretch=True, Size=(2, None)), 
                gc.GButton(Text="5", xStretch=True, Size=(2, None)), 
                gc.GButton(Text="6", xStretch=True, Size=(2, None)), 
                gc.GButton(Text="-", xStretch=True, Size=(5, None)) 
            ],
            [ 
                gc.GButton(Text="7", xStretch=True, Size=(2, None)), 
                gc.GButton(Text="8", xStretch=True, Size=(2, None)), 
                gc.GButton(Text="9", xStretch=True, Size=(2, None)), 
                gc.GButton(Text="*", xStretch=True, Size=(5, None))
            ],
            [ 
                gc.GButton(Text="<", xStretch=True, Size=(2, None)), 
                gc.GButton(Text="0", xStretch=True, Size=(2, None)), 
                gc.GButton(Text=".", xStretch=True, Size=(2, None)), 
                gc.GButton(Text="/", xStretch=True, Size=(5, None))
            ],
            [
                gc.GButton(Text="CLEAN", xStretch=True),
                gc.GButton(Text="GO", xStretch=True),
            ],
            [ gc.GButton(Text="=", xStretch=True) ],
            [ gc.GText(BColor=clr.colors0, xStretch=True) ],
    ]

    layout = [
        [ gc.GText(xStretch=True) ],
        [ 
            gc.GText(yStretch=True, xStretch=True),
            gc.GColumn(winColumnLayout_List=window, xStretch=True, yStretch=True),
            gc.GText(yStretch=True, xStretch=True),
        ],
        [ gc.GText(xStretch=True) ],
    ],

    gc.GWindow(SetMainWindowLayout_List=layout)

    def buttonMath():
        global number1, number2, mathFinish, number1Typing, numbers, mathSymbol, mathEnd, mathStarter, log

        if not mathFinish:
            # add numbers in number1 or number2
            if gc.GetEvent in numbers:
                if number1Typing:
                    number1 += gc.GetEvent
                    gc.GetWindow["math"].update(number1)
                else:
                    number2 += gc.GetEvent
                    gc.GetWindow["math"].update(number2)
            # remove number in number1 or number2
            if number1Typing:
                if gc.GetEvent == "<":
                    number1 = number1[:-1]
                    gc.GetWindow["math"].update(number1)
            else:
                if gc.GetEvent == "<":
                    number2 = number2[:-1]
                    gc.GetWindow["math"].update(number2)
                # finish math
                if gc.GetEvent == "=":
                    mathFinish = True

            # number1 -> number2
            if gc.GetEvent in mathSymbol:
                if number1Typing:
                    number1Typing = False
                    mathStarter = gc.GetEvent
        else:
            # end math
            if mathStarter == "+":
                mathEnd = float(number1) + float(number2)
                gc.GetWindow["math"].update(round(mathEnd, 5))
            elif mathStarter == "-":
                mathEnd = float(number1) - float(number2)
                gc.GetWindow["math"].update(round(mathEnd, 5))
            elif mathStarter == "*":
                mathEnd = float(number1) * float(number2)
                gc.GetWindow["math"].update(round(mathEnd, 5))
            elif mathStarter == "/":
                mathEnd = float(number1) / float(number2)
                gc.GetWindow["math"].update(round(mathEnd, 5))


            # Assign The Math Result to Number1 and Keep Doing Math.
            if gc.GetEvent == "GO":
                number1Typing = True
                mathFinish = False
                number1 = str(mathEnd)
                number2 = mathStarter = ""
                gc.GetWindow["math"].update(number1)


        # clean everything
        if gc.GetEvent == "CLEAN":
            mathFinish = False
            number1Typing = True
            number1 = number2 = mathStarter = ""
            mathEnd = 0
            print(f"{number1} | {number2} | {mathEnd}")
            gc.GetWindow["math"].update("Let's Start Math")


    mathNumberList = []
    mathMathEnd = 0
    mathEnd = False
    number = ""

    def update():
        buttonMath()

    def BeforeExit():
        pass

    gc.SetUpdate(Update=update, exitBEFORE=BeforeExit, TimeOUT=0)

