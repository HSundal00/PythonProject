
while True:
    request = input("Type add, show, edit, complete or exit: ")
    request = request.strip()

    match request:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            #This creates a list within a txt file, 'r' is to read the file
            with open('todo.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            #Calls the same file and write within it, 'w' to write in the file
            with open('todo.txt', 'w') as file:
                file.writelines(todos)

        case 'show':
            with open('todo.txt', 'r') as file:
                todos = file.readlines()


            # Removes extra new lines
            new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(new_todos):
                row = f"{index+1}-{item}"
                print(row)

        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            
            with open('todo.txt', 'r') as file:
                todos = file.readlines()

            new_todos = input("Enter a new item: ")
            todos[number] = new_todos + "\n"

            with open('todo.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("Number of the todo to complete: "))
            with open('todo.txt', 'r') as file:
                todos = file.readlines()

            todos.pop(number - 1)

            with open('todo.txt', 'w') as file:
                file.writelines(todos)

        case 'exit':
            break

print("bye")


    