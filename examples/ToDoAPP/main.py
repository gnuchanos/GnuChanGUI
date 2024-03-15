from GnuChanGUI import *
from todo import *


"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""


if __name__ == "__main__":
    gc = GnuChanGUI(Title="", Size=(700, 600), resizable=True, finalize=True)
    gc.font = "Sans, 20"
    Themecolors().GnuChanOS

    tabMenu = [
        ["Todo File", ["Save", "Clear"]]
    ]

    todoApp0 = [
        [gc.hsep],
        [gc.GInput(value="todot0", xStretch=True, size=(10, None))],
        [gc.hsep],
        [gc.GText(title=todo0_title, value="todot_title_0", xStretch=True, position="center")],
        [gc.GListBox(list=todo0, value="todot0_box", xStretch=True, yStretch=True, noScroolBar=True)] ]

    todoApp1 = [
        [gc.hsep],
        [gc.GInput(value="todot1", xStretch=True, size=(10, None))],
        [gc.hsep],
        [gc.GText(title=todo1_title, value="todot_title_1", xStretch=True, position="center")],
        [gc.GListBox(list=todo1, value="todot1_box", xStretch=True, yStretch=True, noScroolBar=True)] ]

    todoApp2 = [
        [gc.hsep],
        [gc.GInput(value="todot2", xStretch=True, size=(10, None))],
        [gc.hsep],
        [gc.GText(title=todo2_title, value="todot_title_2", xStretch=True, position="center")],
        [gc.GListBox(list=todo2, value="todot2_box", xStretch=True, yStretch=True, noScroolBar=True)] ]

    todoApp3 = [
        [gc.hsep],
        [gc.GInput(value="todot3", xStretch=True, size=(10, None))],
        [gc.hsep],
        [gc.GText(title=todo3_title, value="todot_title_3", xStretch=True, position="center")],
        [gc.GListBox(list=todo3, value="todot3_box", xStretch=True, yStretch=True, noScroolBar=True)] ]

    layout = [
        [gc.GMenuForTheme(winMenu=tabMenu)],
        [gc.hsep],
        [   gc.vsep,
            gc.GFrame(title="Todo 0", winLayout=todoApp0, xStretch=True, yStretch=True, border=0),
            gc.vsep,
            gc.GFrame(title="Todo 1", winLayout=todoApp1, xStretch=True, yStretch=True, border=0),
            gc.vsep,
            gc.GFrame(title="Todo 2", winLayout=todoApp2, xStretch=True, yStretch=True, border=0),
            gc.vsep,
            gc.GFrame(title="Todo 3", winLayout=todoApp3, xStretch=True, yStretch=True, border=0),
            gc.vsep ],
        [gc.hsep]
    ]

    # ekstra variable
    focus = 0
    press = []
    time = 0.3

    gc.GWindow(mainWindow=layout)

    for i in range(0, 4):
        gc.GListBoxBorderSize(value=f"todot{i}_box", border=0)
    
    gc.window["todot0"].SetFocus()

    def update():
        global focus, todo0, todo1, todo2, todo3, focus, time 
        global todo0_title, todo1_title, todo2_title, todo3_title

        # change title ile  press enter
        if gc.event == "Return:36":

            #todo 1
            if focus == 0:
                try:
                    select_item = gc.GetValues["todot0_box"][0]
                    for i in todo0:
                        if i == select_item:
                            todo0.remove(i)
                            break
                    gc.window["todot0_box"].update(todo0)
                except Exception as err:
                    print(f"Err{err}")

                if gc.GetValues["todot0"] != "":
                    if str(gc.GetValues["todot0"]).startswith("h:"):
                        todo0_title = gc.GetValues["todot0"][2:]
                        gc.window["todot_title_0"].update(todo0_title)
                    else:
                        todo0.append(gc.GetValues["todot0"])
                        gc.window["todot0_box"].update(todo0)
                    gc.window["todot0"].update("")
            
            # todo 2
            if focus == 1:
                # remove item in list
                try:
                    select_item = gc.GetValues["todot1_box"][0]
                    for i in todo1:
                        if i == select_item:
                            todo1.remove(i)
                            break
                    gc.window["todot1_box"].update(todo1)
                except Exception as err:
                    print(f"Err{err}")

                if gc.GetValues["todot1"] != "":
                    if str(gc.GetValues["todot1"]).startswith("h:"):
                        todo1_title = gc.GetValues["todot1"][2:]
                        gc.window["todot_title_1"].update(todo1_title)
                    else:
                        todo1.append(gc.GetValues["todot1"])
                        gc.window["todot1_box"].update(todo1)
                    gc.window["todot1"].update("")

            # todo 3
            if focus == 2:
                # remove item in list
                try:
                    select_item = gc.GetValues["todot2_box"][0]
                    for i in todo2:
                        if i == select_item:
                            todo2.remove(i)
                            break
                    gc.window["todot2_box"].update(todo2)
                except Exception as err:
                    print(f"Err{err}")

                if gc.GetValues["todot2"] != "":
                    if str(gc.GetValues["todot2"]).startswith("h:"):
                        todo2_title = gc.GetValues["todot2"][2:]
                        gc.window["todot_title_2"].update(todo2_title)
                    else:
                        todo2.append(gc.GetValues["todot2"])
                        gc.window["todot2_box"].update(todo2)
                    gc.window["todot2"].update("")

            # todo 4
            if focus == 3:
                # remove item in list
                try:
                    select_item = gc.GetValues["todot3_box"][0]
                    for i in todo3:
                        if i == select_item:
                            todo3.remove(i)
                            break
                    gc.window["todot3_box"].update(todo3)
                except Exception as err:
                    print(f"Err{err}")

                if gc.GetValues["todot3"] != "":
                    if str(gc.GetValues["todot3"]).startswith("h:"):
                        todo3_title = gc.GetValues["todot3"][2:]
                        gc.window["todot_title_3"].update(todo3_title)
                    else:
                        todo3.append(gc.GetValues["todot3"])
                        gc.window["todot3_box"].update(todo3)
                    gc.window["todot3"].update("")

        # change focus press tab
        if gc.event == "Tab:23":
            if focus != 3:
                if focus >= 0 and focus < 4:
                    focus += 1
            else:
                focus = 0

        # change focus press shift tab
        if gc.event == "ISO_Left_Tab:23":
            if focus != 0:
                if focus >= 0 and focus < 4:
                    focus -= 1
            else:
                focus = 3

        # change focus
        if focus == 0:
            gc.window["todot0"].set_focus()
        if focus == 1:
            gc.window["todot1"].set_focus()
        if focus == 2:
            gc.window["todot2"].set_focus()
        if focus == 3:
            gc.window["todot3"].set_focus()

        # save todo list
        if gc.event == "Save":
            if not todo0 == [] and not todo1 == [] and not todo2 == [] and not todo3 == []:
                file = open('/home/archkubi/Github/gnuchangui/examples/ToDoAPP/todo.py', 'w')
                save = f"todo0={todo0}\ntodo1={todo1}\ntodo2={todo2}\ntodo3={todo3}\ntodo0_title=\"{todo0_title}\"\ntodo1_title=\"{todo1_title}\"\ntodo2_title=\"{todo2_title}\"\ntodo3_title=\"{todo3_title}\"  "
                file.write(save)
                file.close()

        # clear listbox ALL
        if gc.event == "Clear":
            file = open('/home/archkubi/Github/gnuchangui/examples/ToDoAPP/todo.py', 'w')
            save = f"todo0=[]\ntodo1=[]\ntodo2=[]\ntodo3=[]\ntodo0_title=\"\"\ntodo1_title=\"\"\ntodo2_title=\"\"\ntodo3_title=\"\""

            # this is not in video i add new
            gc.window["todot0_box"].update("")
            gc.window["todot1_box"].update("")
            gc.window["todot2_box"].update("")
            gc.window["todot3_box"].update("")

            gc.window["todot_title_0"].update("")
            gc.window["todot_title_1"].update("")
            gc.window["todot_title_2"].update("")
            gc.window["todot_title_3"].update("")

            file.write(save)
            file.close()


    # while update
    gc.update(GUpdate=update)