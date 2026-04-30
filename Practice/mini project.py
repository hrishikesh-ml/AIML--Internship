tasks = []

def add_task():
    
    tasks.append({
        "name": input("Task: "), 
        "priority": input("Priority (High/Med/Low): "),
        "time": float(input("Hours: ")), 
        "status": "Pending"
    })

def view_tasks():
    
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t['name']} | {t['priority']} | {t['time']}h | {t['status']}")

def analyze_tasks():
    total_t = sum(t['time'] for t in tasks) 
    comp = sum(1 for t in tasks if t['status'] == "Completed")
    high_p = [t['name'] for t in tasks if t['priority'].lower() == 'high']
    
    print(f"Tasks: {len(tasks)} | Total Time: {total_t}h | High Priority: {high_p}")
    
    if total_t > 8:
        print(" Warning: Work > 8 hours!") 
    if comp > (len(tasks) - comp):
        print(" Positive progress!") 

while True: 
    c = input("\n1.Add 2.View 3.Complete 4.Analyze 5.Exit: ")
    if c == '1':
        add_task() 
    elif c == '2':
        view_tasks()
    elif c == '3':
        view_tasks()
        idx = int(input("Task # to complete: ")) - 1
        tasks[idx]['status'] = "Completed"
    elif c == '4':
        analyze_tasks()
    elif c == '5':
        print("good bye.")
        break