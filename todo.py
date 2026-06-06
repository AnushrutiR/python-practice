tasks=[]
def save_tasks():
    file = open("tasks.txt", "w")
    for task in tasks:
        file.write(task + "\n")
    file.close()

def load_tasks():
    try:
        file = open("tasks.txt", "r")
        for line in file:
            tasks.append(line.strip())
        file.close()
    except:
        pass

def add_tasks():
        task=input("Enter tasks:")
        tasks.append(task)
        save_tasks()
        print("Task added successfully!")
def view_tasks():
        if len(tasks)==0:
                print("No current tasks :D")
        else:
                for i,task in enumerate(tasks):
                    print(i+1,task)
def mark_done():
    view_tasks()
    if len(tasks) == 0:
        return
    choice = int(input("Enter task number to mark done: "))
    tasks.pop(choice - 1)
    save_tasks()
    print("Task marked as done!")
load_tasks()

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4.Quit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_tasks()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    else:
         break
