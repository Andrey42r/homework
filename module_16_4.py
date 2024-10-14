from fastapi import FastAPI, status, Body, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

users = []

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get("/users")
def get_all_user() -> List[User]:
    return users


@app.post("/user/{username}/{age}")
def create_user(username: str, age: int):
    user_id = max(users, key=lambda x: int(x.id)).id + 1 if users else 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return users

@app.put("/user/{user_id}/{username}/{age}")
def create1_user(user_id: int, username: str, age: int) -> str:
    try:
        if user_id in users:
            user_id = f"Имя: {username}, возраст: {age}"
        return f"The user {user_id} is updated"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")

@app.delete("/user/{user_id}")
def delete_user(user_id: int) -> str:
    for i, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(i)
            return f"User {deleted_user} was deleted"
        raise HTTPException(status_code=404, detail="User was not found")
