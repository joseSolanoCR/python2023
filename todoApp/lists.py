todos = []

while True:
    user_action = input("type add, edit or show: ")

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            print(todos)
        case 'edit':
            for index, x in enumerate(todos):
                print(index,x)
            item = todos.index(input("What todo do you want to edit?"))
            n_item = input("New todo: ")
            todos[item] = n_item
            #todos.append(n_item)
            print(todos)
        case 'exit':
            break

print('Bye')

