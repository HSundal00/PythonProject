import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")


while True:
    request = input("Type add, show, edit, complete or exit: ")
    request = request.strip()

    if request.startswith('add'):
        todo = request[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif request.startswith('show'):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)

    elif request.startswith('edit'):
        try:
            number = int(request[5:])
            number = number - 1
            
            todos = functions.get_todos()

            new_todos = input("Enter a new item: ")
            todos[number] = new_todos + "\n"

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif request.startswith('complete'):
        try:
            number = int(request[9:])
            
            todos = functions.get_todos()

            todos.pop(number - 1)

            functions.write_todos(todos)

        except IndexError:
            print("Wrong number")
            continue


    elif request.startswith('exit'):
            break

print("bye")


#Testing