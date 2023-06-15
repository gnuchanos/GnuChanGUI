from GnuChanGUI import *
import random

def main():
    gc = GnuChanGUI(Title="GnuChan Program Timer", Size=(1024,600), resizable=True)
    gc.Theme()

    randomWords = []
    randomWord = []
    randomButtonList = ["q1", "q2", "q3", "q4"]
    questionFalse = False
    newlog = ""

    gMenu = [
        ["Info", ["GnuChanOS", "Youtube Channel", "Github Page"]],
        ["System", ["Exit"]]
    ]

    layout = [
        [gc.GMenuForTheme(winMenu=gMenu, font=gc.font)],
        [gc.GListBox(value="questionLog", font=gc.font, xStretch=True, yStretch=True, position="center", noScroolBar=True)],
        [gc.GText(value="Words", font="Sans, 25", xStretch=True, position="center")],
        [gc.GButton("1", value=randomButtonList[0], font=gc.font, xStretch=True)],
        [gc.GButton("2", value=randomButtonList[1], font=gc.font, xStretch=True)],
        [gc.GButton("3", value=randomButtonList[2], font=gc.font, xStretch=True)],
        [gc.GButton("4", value=randomButtonList[3], font=gc.font, xStretch=True)],
        [gc.GButton("Random English Words Question", font=gc.font, xStretch=True)],
        [gc.GText("", xStretch=True)],
        [gc.GMultiline(value="answerLog", font=gc.font, xStretch=True, yStretch=True, readonly=True)],



    ]

    gc.GWindow(mainWindow=layout)


    gc.GListBoxFixer(value="questionLog", border=0)
    with open("modified_words.txt", "r") as words:
        GWords = words.read().splitlines()
        gc.window["questionLog"].update(GWords)


    while True:
        event, GetValues = gc.window.read(timeout=24)
        if event == WIN_CLOSED or event == "Exit":
            break

        if event == "Random English Words Question":
            questionFalse = True

        if questionFalse == True:
            with open("modified_words.txt", "r") as words:
                #split all lines
                randomWords = words.read().splitlines()
                # split 2 words question and answer
                randomWord = random.choice(randomWords).split("-")  # correct answer
                randomAnswers = random.sample(randomWords, 3)  # wrong answers
                # randomword is correck but randomAnwers wrong
                randomAnswerList = [randomWord[1]] + [answer.split("-")[1] for answer in randomAnswers]
                # take random answer
                random.shuffle(randomAnswerList)
                q1, q2, q3, q4 = randomAnswerList  # random shuffle answers

                # answer buttons
                gc.window[randomButtonList[0]].update(q1)
                gc.window[randomButtonList[1]].update(q2)
                gc.window[randomButtonList[2]].update(q3)
                gc.window[randomButtonList[3]].update(q4)


                questionWindow = f"answer this question ->| {randomWord[0]} |"
                gc.window["Words"].update(questionWindow)
                questionFalse = False

        if event in randomButtonList:
            try:
                selectedAnswer = gc.window[event].GetText()
                if selectedAnswer == randomWord[1]:
                    log = "Correct! The answer is: " + randomWord[1] + "\n"
                    newlog += log
                    gc.window["answerLog"].update(newlog)
                else:
                    log = "Incorrect! The correct answer is: " + randomWord[1] + "\n"
                    newlog += log
                    gc.window["answerLog"].update(newlog)
            except IndexError:
                pass

    gc.window.close()


if __name__ == "__main__":
    main()
