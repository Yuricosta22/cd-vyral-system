from __future__ import annotations

from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr


class LeadCreate(BaseModel):
    full_name: str
    email: EmailStr
    status: Literal["new", "contacted", "qualified", "won", "lost"] = "new"
    source: str = "manual"


class Lead(LeadCreate):
    id: int


class TaskCreate(BaseModel):
    title: str
    assigned_to: str
    status: Literal["pending", "in_progress", "done"] = "pending"


class Task(TaskCreate):
    id: int


app = FastAPI(title="cd-vyral-system")

leads: list[Lead] = []
tasks: list[Task] = []


@app.get("/")
def read_root():
    return {"name": "cd-vyral-system", "status": "running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/dashboard")
def dashboard_summary():
    total_leads = len(leads)
    active_tasks = sum(1 for item in tasks if item.status != "done")
    won_leads = sum(1 for lead in leads if lead.status == "won")
    conversion_rate = round((won_leads / total_leads) * 100, 2) if total_leads else 0.0

    return {
        "total_leads": total_leads,
        "active_tasks": active_tasks,
        "conversion_rate": conversion_rate,
        "won_leads": won_leads,
    }


@app.get("/leads", response_model=list[Lead])
def list_leads():
    return leads


@app.post("/leads", response_model=Lead, status_code=201)
def create_lead(payload: LeadCreate):
    new_lead = Lead(id=len(leads) + 1, **payload.model_dump())
    leads.append(new_lead)
    return new_lead


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    return tasks


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(payload: TaskCreate):
    new_task = Task(id=len(tasks) + 1, **payload.model_dump())
    tasks.append(new_task)
    return new_task
