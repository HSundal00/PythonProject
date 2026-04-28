def get_todos(filepath="todo.txt"):
    """ Read a text file and return the list of to-do items. """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()    
    return todos_local


def write_todos(todos_arg,filepath="todo.txt"):
    """ Write the to-do items list in the text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


while True:
    request = input("Type add, show, edit, complete or exit: ")
    request = request.strip()

    if request.startswith('add'):
        todo = request[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    elif request.startswith('show'):

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)

    elif request.startswith('edit'):
        try:
            number = int(request[5:])
            number = number - 1
            
            todos = get_todos()

            new_todos = input("Enter a new item: ")
            todos[number] = new_todos + "\n"

            write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif request.startswith('complete'):
        try:
            number = int(request[9:])
            
            todos = get_todos()

            todos.pop(number - 1)

            write_todos(todos)

        except IndexError:
            print("Wrong number")
            continue


    elif request.startswith('exit'):
            break

print("bye")


#Testing