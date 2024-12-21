import FreeSimpleGUI as sg
import functions

label = sg.Text("Type in a to-do")
input_box=sg.InputText(tooltip="Enter todo", key='activity')
add_button = sg.Button("Add")

window = sg.Window("To-do-App", layout=[[label], [input_box,add_button]])


while True:
    event, values = window.read()
    activities_list =  functions.get_todos_list()
    activities_list.append(values['activity'])
    activities_list[-1]= activities_list[-1] +"\n"
    functions.write_todos(activities_list)

    print(functions.get_todos_list())
    print(functions.get_todos())
    break


window.close()