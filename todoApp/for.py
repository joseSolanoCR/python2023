todos = []

while True:
    user_action = input("type add or show: ").strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for x in todos:
                print(x.capitalize())
        case 'exit':
            break
        case _:
            print("Unknown command!!")

print('Bye')

