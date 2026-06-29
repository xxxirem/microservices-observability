from fastapi import FastAPI, HTTPException
import os

app = FastAPI(title="User Service")

USERS = {
    1: {"id": 1, "name": "Samir Khavari", "role": "DevOps Trainee"},
    2: {"id": 2, "name": "Vovchik", "role": "QA Engineer"}
}

@app.get("/api/v1/users/{user_id}")
async def get_user(user_id: int):
    if user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")
    return USERS[user_id]

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "user-service"}