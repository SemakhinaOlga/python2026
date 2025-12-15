def add_task(tasks_list, title, priority=1, tags=None, completed=False):
    tasks_list=[]
    new_tasks={}
    
    if tags is None:
        tags=[]
    
        
        
    new_tasks ={'title': title, 'priority': priority, 'tags': tags, 'completed': completed}
    tasks.append(new_tasks)

    
    return(tasks_list)
    
    
    

tasks=[]
tasks = add_task(tasks, "Купить молоко")
print(tasks)



