tasks=[]
def add_tasks (task):
    tasks.append(task)
def show_tasks () :
    if not tasks :
        print ("there is no tasks yet")
        return
    for index , task in enumerate(tasks , start=1):
        print(f"{index}. {task}")
add_tasks("learn git")
add_tasks("publish a priject on github")
add_tasks("learn sql")
show_tasks()