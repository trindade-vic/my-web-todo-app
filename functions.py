FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return a list of todos """
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write a new todo in a text file """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print(get_todos())