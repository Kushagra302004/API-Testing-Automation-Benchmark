from typing import Optional
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="API Testing Demo Service")

users = {1: {"id": 1, "name": "Rahul", "email": "rahul@example.com", "age": 22}}
next_id = 2

class UserCreate(BaseModel):
    name: str = Field(min_length=1)
    email: str = Field(min_length=5)
    age: int = Field(ge=18, le=60)

class UserUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1)
    email: Optional[str] = Field(default=None, min_length=5)
    age: Optional[int] = Field(default=None, ge=18, le=60)

@app.get("/health")
def health(): return {"status": "ok"}

@app.get("/users")
def list_users(): return list(users.values())

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users: raise HTTPException(404, "User not found")
    return users[user_id]

@app.post("/users", status_code=201)
def create_user(payload: UserCreate):
    global next_id
    user = {"id": next_id, **payload.model_dump()}
    users[next_id] = user
    next_id += 1
    return user

@app.put("/users/{user_id}")
def replace_user(user_id: int, payload: UserCreate):
    if user_id not in users: raise HTTPException(404, "User not found")
    users[user_id] = {"id": user_id, **payload.model_dump()}
    return users[user_id]

@app.patch("/users/{user_id}")
def patch_user(user_id: int, payload: UserUpdate):
    if user_id not in users: raise HTTPException(404, "User not found")
    users[user_id].update(payload.model_dump(exclude_none=True))
    return users[user_id]

@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int):
    if user_id not in users: raise HTTPException(404, "User not found")
    del users[user_id]

@app.get("/protected")
def protected(authorization: Optional[str] = Header(None)):
    if authorization != "Bearer demo-token":
        raise HTTPException(401, "Invalid or missing token")
    return {"message": "Protected resource"}
