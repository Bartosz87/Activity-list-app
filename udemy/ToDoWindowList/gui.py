import FreeSimpleGUI as sg
import functions

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key='activity')
add_button = sg.Button("Add")
remove_button = sg.Button("Remove")

list_box = sg.Listbox(get_todos_list(),
                      size=(30, 5),
                      key='listbox')

window = sg.Window("To-do-App", layout=[[label], [input_box, add_button], [list_box, edit_button, remove_button]])

while True:
    event, values = window.read()
    activities_list = get_todos_list()
    print(event, values)

    match event:
        case "Add":

            activities_list.append(values['activity'])
            activities_list[-1] = activities_list[-1] + "\n"
            functions.write_todos(activities_list)
            window['listbox'].update(values=activities_list)

            print('wpisywana wartość: ', values['activity'])

        case "Remove":
            activities_list = functions.get_todos_list()
            activities_list.remove(values['listbox'][0])
            functions.write_todos(activities_list)
            window['listbox'].update(values=activities_list)

            print("removed: ", values['listbox'][0])

        case sg.WIN_CLOSED:
            break

window.close()


