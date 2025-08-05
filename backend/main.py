# backend/main.py
from fastapi import FastAPI
from agents.manager_agent import assign_task

app = FastAPI()

@app.get("/")
def root():
    return {"message": "E-commerce AI Agent API running"}

@app.post("/run-task/")
def run_task(task_type: str, inputs: dict):
    result = assign_task(task_type, inputs)
    return {"task_type": task_type, "result": result}
