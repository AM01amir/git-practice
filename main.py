tasks=[]
def add_tasks (task):
    tasks.append(task)
def show_tasks () :
    if not tasks :
        print ("there is no tasks yet")
        return
    for index , task in enumerate(tasks , start=1):
        print(f"{index}. {task}")
def remove_task (number_of_task):
    if 1<=number_of_task<=len(tasks) :
        removed_task=tasks.pop(number_of_task-1)
        print(f"deleted {removed_task}")
    else:
        print("invalid task number")
add_tasks("learn git")
add_tasks("publish a project on github")
add_tasks("learn sql")
show_tasks()
remove_task(2)
print("\ntask after removation")
show_tasks()