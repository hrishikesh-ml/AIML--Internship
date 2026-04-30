tasks=[]
def add_tasks():
    name=input("enter the task name:")
    priority=input("enter priority")
    time=int(input("enter the time required:"))
    
    task = {
        'Names' : name,'priorities':priority,'time':time
       
    }
    tasks.append(task)
    print("task succesfully updated!!!")

def display_tasks():
    if not tasks:
        print("empty task!!")
        return 
    print("---TASK LIST---")
    for i,task in enumerate(tasks,1):
        print({task})
display_tasks()


