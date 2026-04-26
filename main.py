def get_todos(filepath):
    with open(filepath, 'r') as file:
        todos_local = file.readlines()    
    return todos_local

def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


while True:
    request = input("Type add, show, edit, complete or exit: ")
    request = request.strip()

    if request.startswith('add'):
        todo = request[4:]

        todos = get_todos("todo.txt")

        todos.append(todo + '\n')

        write_todos("todo.txt", todos)

    elif request.startswith('show'):

        todos = get_todos("todo.txt")

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)

    elif request.startswith('edit'):
        try:
            number = int(request[5:])
            number = number - 1
            
            todos = get_todos("todo.txt")

            new_todos = input("Enter a new item: ")
            todos[number] = new_todos + "\n"

            write_todos("todo.txt", todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif request.startswith('complete'):
        try:
            number = int(request[9:])
            
            todos = get_todos("todo.txt")

            todos.pop(number - 1)

            write_todos("todo.txt", todos)

        except IndexError:
            print("Wrong number")
            continue


    elif request.startswith('exit'):
            break

print("bye")


#Testing