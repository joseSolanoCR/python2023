with open('todos.txt', 'r') as file :
    todos = file.readlines()

while True:
    user_action = input("type add, edit, complete or show: ")

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + '\n'
            todos.append(todo)
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        case 'show':
            n_todos = [item.strip('\n') for item in todos]
            for index, x in enumerate(n_todos):
                print(f"{index}. {x}")
        case 'edit':
            for index, x in enumerate(todos):
                print(f"{index}. {x}")
            todos = [item.strip('\n') for item in todos]
            item = todos.index((input("What todo do you want to edit?")))
            n_item = input("New todo: ")
            todos[item] = n_item + "\n"
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
            #todos.append(n_item)
            print(todos)
        case 'exit':
            break
        case 'complete':
            for index, x in enumerate(todos):
                print(f"{index}. {x}")
            cTodo = input("What todo do you want to complete?")
            todos.remove(cTodo)
            # todos.append(n_item)
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
            print(todos)

print('Bye')

