tasks=[]
while True:
    print("\n--- TO-DO List ---")
    print('1.Add Task')
    print('2.View Task')
    print('3.Delete Task')
    print('4.Exit')

    Choice=input("Enter choice: ")
    if Choice =='1':
        task=input("Enter Task: ")
        tasks.append(task)
        print(" Task added")

    elif Choice == "2":
        if not tasks:
            print("No tasks available")
        else:
            print('\nYour Tasks:')
            for i,task in enumerate(tasks,start=1):
                print(f"{i}.{task}")

    elif Choice == "3":
        if not tasks:
            print("No task to delete")
        else:
            for i,task in enumerate(tasks,start=1):
                print(f"{i}.{task}")
            num = int(input("Enter task number to delete: "))
            if 1<=num <= len(tasks):
                tasks.pop(num-1)
                print("Task deleted")
            else:
                print("Invalid number")
    elif Choice == '4':
        print("Exiting...!!!")
        break
    else:
        print("Invalid choice")
        
        

    