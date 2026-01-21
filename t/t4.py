import json

try:
    with open("data.json", "r") as f:
        tasks = json.load(f)
except FileNotFoundError:
    tasks = []

def add_task():
    while True:
        task = input("Enter the new Task:")
        task = " ".join([word.lower() for word in task.split()])
    
        if task not in tasks:
            tasks.append(task)
            print("Task has been added.")
            break
        else:
            print("The task has already been added.Try again.")
        
        
    
    with open("data.json", "w") as f:
        json.dump(tasks, f, indent = 4)

def remove_task():
    for task in tasks:
        print(f"*{task}")
    task = input("Enter the task to be removed from the above list:")
    task = " ".join([word.lower() for word in task.split()])
    if task in tasks:
        tasks.remove(task)
        with open("data.json", "w") as f:  # Save the change!
            json.dump(tasks, f, indent=4)
    else:
        print("This task doesnt exist.")
        

print("WELCOME TO MY TO-DO-LIST CREATOR.")
continue_choice = input("Enter 'c' to continue or any other key to quit:")
while continue_choice.lower() == "c":
    choice = input('Enter "a" to add task / "r" to remove tasks / "v" to view tasks :').lower().strip()
    while choice not in "arv":
        print("invalid Option!!!")
        choice = input('Enter "a" to add task / "r" to remove tasks / "v" to view tasks :').lower().strip()
    match (choice):
        case "a":
            add_task()
        case "r":
            remove_task()
        case "v":
            for task in tasks:
                print(task)
        case _:
            print("invalid option")
    continue_choice = input("Enter 'c' to continue or any other key to quit:")


print("Your Remaining Tasks:")
for task in tasks:
    print(f"*{task}")

    
