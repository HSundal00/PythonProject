while True:
    request = input("Type add, show, edit, complete or exit: ")
    request = request.strip()

    if request.startswith('add'):
        todo = request[4:]

        with open('todo.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo + '\n')

        with open('todo.txt', 'w') as file:
            file.writelines(todos)

    elif request.startswith('show'):

        with open('todo.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)

    elif request.startswith('edit'):
        try:
            number = int(request[5:])
            number = number - 1
            
            with open('todo.txt', 'r') as file:
                todos = file.readlines()

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
            
            with open('todo.txt', 'r') as file:
                todos = file.readlines()

            todos.pop(number - 1)

            with open('todo.txt', 'w') as file:
                file.writelines(todos)
        except IndexError:
            print("Wrong number")
            continue


    elif request.startswith('exit'):
            break

print("bye")



    