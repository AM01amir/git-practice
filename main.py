tasks=[]
def add_tasks (task):
    tasks.append({"title":task,"completed":False})
def show_tasks () :
    if not tasks :
        print ("there is no tasks yet")
        return
    for index , task in enumerate(tasks , start=1):
        status = "done" if task["completed"] else "pending"
        print(f"{index}. {task["title"]}-{status}")
def complete_task (task_number):
    if 1<=task_number<=len(tasks) :
        tasks[task_number-1]["completed"]=True
        print("task completed")
    else:
        print("invalid task number")
add_tasks("learn git")
add_tasks("publish a project on github")
add_tasks("learn sql")
print("befor complation : ")
show_tasks()
complete_task(2)
print("\nafter complation")
show_tasks()
def add(a,b):
	return a+b