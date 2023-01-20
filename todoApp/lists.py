file = open('todos.txt', 'r')
todos = file.readlines()
file.close()
for l in todos:
    print(l)
while True:
    user_action = input("type add, edit, complete or show: ")

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + '\n'
            todos.append(todo)
            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            for index, x in enumerate(todos):
                print(f"{index}. {x}")
        case 'edit':
            for index, x in enumerate(todos):
                print(f"{index}. {x}")
            item = todos.index(input("What todo do you want to edit?"))
            n_item = input("New todo: ")
            todos[item] = n_item
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
            print(todos)

print('Bye')

