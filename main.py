while True:
    request = input("Type add, show, edit, complete or exit: ")
    request = request.strip()

    if 'add' in request:
        todo = request[4:]

        with open('todo.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo + '\n')

        with open('todo.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in request:
        with open('todo.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)

    elif 'edit' in request:
        number = int(request[5:])
        number = number - 1
        
        with open('todo.txt', 'r') as file:
            todos = file.readlines()

        new_todos = input("Enter a new item: ")
        todos[number] = new_todos + "\n"

        with open('todo.txt', 'w') as file:
            file.writelines(todos)

    elif 'complete' in request:
        number = int(request[9:])
        
        with open('todo.txt', 'r') as file:
            todos = file.readlines()

        todos.pop(number - 1)

        with open('todo.txt', 'w') as file:
            file.writelines(todos)

    elif 'exit' in request:
            break

print("bye")

#just testing to see if this works


    