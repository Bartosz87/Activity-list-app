FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):

    with open(filepath, "r") as file:
        todos_list = file.read()
    return todos_list

def write_todos(activities, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(activities)


def get_todos_list(filepath=FILEPATH):
    with open(filepath, "r") as file:
        todos_list = file.readlines()
    return todos_list


