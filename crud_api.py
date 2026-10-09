from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
from fastapi.middleware.cors import CORSMiddleware
 
app = FastAPI(title="CRUD API")
pp = FastAPI(title="CRUDAPI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

connection = sqlite3.connect("database.db",check_same_thread=False)


class User(BaseModel):
    name:str


@app.post("/users")
def create_user(user: User):
    connection.execute(
        "INSERT INTO users (name) VALUES (?)",
        (user.name,)
    )

    connection.commit()

    return {
        "message": "User created successfully",
        "name": user.name
    }


@app.get("/")
def home():
    return {
        "message": "CRUD API is running"
    }


@app.get("/users")
def get_users():
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users")

    users = cursor.fetchall()

    return users


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "id": user_id,
        "message": "User found"
    }
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    connection.execute(
        "DELETE FROM users WHERE id = ?",
        (user_id,)
    )

    connection.commit()

    return {
        "message": "User deleted successfully",
        "id": user_id
    }
@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    connection.execute(
        "UPDATE users SET name = ? WHERE id = ?",
        (user.name, user_id)
    )

    connection.commit()

    return {
        "message": "User updated successfully",
        "id": user_id,
        "name": user.name
    }