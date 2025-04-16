from fastapi import APIRouter,HTTPException
from models.TaskModel import Task
from datetime import datetime

router=APIRouter()

tasks_db=[]

@router.post("/assign")
def assign_task(task: Task):
    task.assigned_at = datetime.now()
    tasks_db.append(task)
    return {"message": "Task assigned successfully", "task": task}

@router.get("/tasks/{intern_email}")
def get_intern_tasks(intern_email: str):
    intern_tasks = [task for task in tasks_db if task.intern_email == intern_email]
    return intern_tasks

@router.put("/complete/{intern_email}/{title}")
def mark_task_complete(intern_email: str, title: str):
    for task in tasks_db:
        if task.intern_email == intern_email and task.title == title:
            task.completed = True
            return {"message": "Task marked as completed"}
    raise HTTPException(status_code=404, detail="Task not found")

# hi my name is Harsh Shrivastava