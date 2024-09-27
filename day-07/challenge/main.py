from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

class Task(BaseModel):
    title: str
    description: str

tasks: Dict[int, Task] = {}
task_id_counter = 1

@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}

@app.post("/tasks")
def create_task(task: Task):
    global task_id_counter
    tasks[task_id_counter] = task
    task_id_counter += 1
    return {"task_id": task_id_counter - 1, "task": task}

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"task_id": task_id, "task": tasks[task_id]}

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[task_id] = updated_task
    return {"task_id": task_id, "task": updated_task}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]
    return {"message": "Task deleted successfully"}