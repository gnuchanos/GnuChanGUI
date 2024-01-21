from GnuChanGUI import *
from save import *

gc = GnuChanGUI(Title="GnuChan Program Timer", Size=(1024, 600), resizable=True)
Themecolors().GnuChanOS

gMenu = [ ["Info", ["GnuChanOS", "Youtube Channel", "Github Page"]], 
          ["TodoList", ["Save", "Clean"]],
          
          ["Story", ["Open File", "Save", "Save As", 
                                                "Font Size", ["20", "19", "18", "17", "16", "15","14", "13", "12", "11", "10"],
                                                "Font Color", ["Black", "White", "Red", "Green", "Blue", "Yellow"],
                                                "Font BackGround Color", ["Black", "White", "Red", "Green", "Blue", "Yellow"],
                    ]],
          ["System", ["Exit"]] ]


todolist0 = saveDic["todolist0"]
todolist1 = saveDic["todolist1"]
todolist2 = saveDic["todolist2"]


todo0 = [
    [ gc.GText(title="Assets Work", font="Sans, 20", xStretch=True, position="center")],
    [ gc.GButton(title="remove", value="remove_todo0", font="Sans, 20", size=(None, 10), xStretch=True), 
      gc.GButton(title="ADD", value="button_add_todo0", font="Sans, 20", size=(None, 10), xStretch=True)],

    [ gc.GInput(value="add_todo0", font="Sans, 20", size=(None, 10), xStretch=True) ],
    [ gc.GText(title=""), 
     gc.GListBox(list=todolist0, font="Sans, 12", value="todo0", xStretch=True, yStretch=True, size=(None, 15), noScroolBar=True, position="center"), 
     gc.GText(title="") ] ]

todo1 = [
    [ gc.GText(title="Script/Scene", font="Sans, 20", xStretch=True, position="center")],
    [ gc.GButton(title="remove", value="remove_todo1", font="Sans, 20", size=(None, 10), xStretch=True), 
      gc.GButton(title="ADD", value="button_add_todo1", font="Sans, 20", size=(None, 10), xStretch=True)],

    [ gc.GInput(value="add_todo1", font="Sans, 20", size=(None, 10), xStretch=True) ],
    [ gc.GText(title=""), 
      gc.GListBox(list=todolist1, font="Sans, 12", value="todo1", xStretch=True, yStretch=True, size=(None, 15), noScroolBar=True, position="center"), 
      gc.GText(title="") ] ]

todo2 = [
    [ gc.GText(title="Finish Work", font="Sans, 20", xStretch=True, position="center")],
    [ gc.GButton(title="remove", value="remove_todo2", font="Sans, 20", size=(None, 10), xStretch=True), 
      gc.GButton(title="ADD", value="button_add_todo2", font="Sans, 20", size=(None, 10), xStretch=True)],

    [ gc.GInput(value="add_todo2", font="Sans, 20", size=(None, 10), xStretch=True) ],
    [ gc.GText(title=""), 
      gc.GListBox(list=todolist2, font="Sans, 12", value="todo2", xStretch=True, yStretch=True, size=(None, 15), noScroolBar=True, position="center"), 
      gc.GText(title="") ] ]

todo_Window = [ [
        gc.vsep,
        gc.GColumn(winColumn=todo0, xStretch=True, yStretch=True),
        gc.vsep,
        gc.GColumn(winColumn=todo1, xStretch=True, yStretch=True),
        gc.vsep,
        gc.GColumn(winColumn=todo2, xStretch=True, yStretch=True),
        gc.vsep,
    ] ]

Story_Text = [
    [gc.GText(title="Story Dialogs", font="Sans, 20", position="center", xStretch=True)],
    [gc.GMultiline(value="story", font="Sans, 20", xStretch=True, yStretch=Tree, wrapLines=True)]
]

layout = [
    [gc.GMenuForTheme(winMenu=gMenu, font=gc.font)],
    [gc.GTabGroup(TabGroupLayout=[
        [gc.GTab(title="Todot List", TabLayout=todo_Window)],
        [gc.GTab(title="Story", TabLayout=Story_Text)],
    ])],
    [gc.GText(title="Version 0.0.1 Beta", font="Sans, 20", xStretch=True)]

    ]

gc.GWindow(mainWindow=layout)

# settings
gc.GListBoxBorderSize(value="todo0", border=0)
gc.GListBoxBorderSize(value="todo1", border=0)
gc.GListBoxBorderSize(value="todo2", border=0)
gc.GMultilineTabSpace(gMultilineFont="Sans, 15", gMultilineValue="story")

def removeThing(todolist, value):
    try:
        remove = str(gc.GetValues[value]).lstrip("['").rstrip("']")
        todolist.remove(remove)
        gc.window[value].update(todolist)
    except ValueError:
        gc.GMessage(wmTitle="Warning", message="Choose Something to delete")

def addThings(todolist, value, inputValue):
    if gc.GetValues[inputValue] != "":
        todolist.append(gc.GetValues[inputValue])
        gc.window[value].update(todolist)
        gc.window[inputValue].update("")

textOpen = FileSave(value="story", window=gc.window)

def Open_Text():
    # multiline text
    global textOpen
    if gc.event == "Open File":
        textOpen.Open
    elif gc.event == "Save As":
        textOpen.SaveAs
    elif gc.event == "Save":
        textOpen.Save

def todoList():
    global todolist0, todolist1, todolist2
    # remove todo list item
    if gc.event == "remove_todo0":
        removeThing(todolist=todolist0, value="todo0")
    if gc.event == "remove_todo1":
        removeThing(todolist=todolist1, value="todo1")
    if gc.event == "remove_todo2":
        removeThing(todolist=todolist2, value="todo2")

    # add new todo list item
    if gc.event == "button_add_todo0":
        addThings(todolist=todolist0, value="todo0", inputValue="add_todo0")
    if gc.event == "button_add_todo1":
        addThings(todolist=todolist1, value="todo1", inputValue="add_todo1")
    if gc.event == "button_add_todo2":
        addThings(todolist=todolist2, value="todo2", inputValue="add_todo2")

    # save todo list
    if gc.event == "Save":
        saveDic["todolist0"] = todolist0
        saveDic["todolist1"] = todolist1
        saveDic["todolist2"] = todolist2       
        with open("save.py", 'w') as file:
                file.write(f"saveDic={saveDic}")

    # clean todo list
    if gc.event == "Clean":
        # clean in save.py dictionary
        saveDic["todolist0"] = []
        saveDic["todolist1"] = []
        saveDic["todolist2"] = []      
        with open("save.py", 'w') as file:
                file.write(f"saveDic={saveDic}")

        # take empty variable
        todolist0 = saveDic["todolist0"]
        todolist1 = saveDic["todolist1"]
        todolist2 = saveDic["todolist2"]

        # update window
        gc.window["todo0"].update(todolist0)
        gc.window["todo1"].update(todolist1)
        gc.window["todo2"].update(todolist2)

def update():
    # gnuchanos pages
    if gc.event == "GnuChanOS":
        webbrowser.open("https://gnuchanos.github.io") 
    elif gc.event == "Youtube Channel":
        webbrowser.open("https://www.youtube.com/channel/ucmjtfic152myx7mbxmghfea")    
    elif gc.event == "Github Page":
        webbrowser.open("https://github.com/gnuchanos")

    Open_Text()
    todoList()



gc.update(GUpdate=update)
