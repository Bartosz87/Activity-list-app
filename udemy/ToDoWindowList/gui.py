import FreeSimpleGUI as sg
from functions import *

label1 = sg.Text("Enter your activity:")
label2 = sg.Text("Your activities list:")
input_box = sg.InputText(key='activity')
add_button = sg.Button("Add")
remove_button = sg.Button("Remove")

list_box = sg.Listbox(get_todos_list(),
                      size=(30, 5),
                      key='listbox')

window = sg.Window("To-do-App", layout=[[label1], [input_box, add_button], [label2], [list_box, remove_button]])

while True:
    event, values = window.read()
    activities_list = get_todos_list()
    print(event, values)


    if event == "Add":
        activities_list.append(values['activity'])
        activities_list[-1] = activities_list[-1] + "\n"
        write_todos(activities_list)
        window['listbox'].update(values=activities_list)
        window['activity'].update(value='')


    if event == "Remove":
        activities_list = get_todos_list()
        activities_list.remove(values['listbox'][0])
        write_todos(activities_list)
        window['listbox'].update(values=activities_list)

    if event == sg.WIN_CLOSED:
        break

window.close()


