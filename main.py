def get_todos():
    with open('todo.txt', 'r') as file:
        todos_local = file.readlines()    
    return todos_local


while True:
    request = input("Type add, show, edit, complete or exit: ")
    request = request.strip()

    if request.startswith('add'):
        todo = request[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        with open('todo.txt', 'w') as file:
            file.writelines(todos)

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

            with open('todo.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif request.startswith('complete'):
        try:
            number = int(request[9:])
            
            todos = get_todos()

            todos.pop(number - 1)

            with open('todo.txt', 'w') as file:
                file.writelines(todos)
        except IndexError:
            print("Wrong number")
            continue


    elif request.startswith('exit'):
            break

print("bye")


#Testing