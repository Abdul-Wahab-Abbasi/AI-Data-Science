from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def greet():
    return "Hello, World!"

users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com"},
    {"id": 2, "name": "Jane Doe", "email": "jane@example.com"},
    {"id": 3, "name": "Alice Smith", "email": "alice@example.com"},
    {"id": 4, "name": "Bob Johnson", "email": "bob@example.com"},
]
@app.get("/users")
def get_users():
    return users

@app.get("/users/{id}")
def get_user_by_id(id: int):
    for user in users:
        if user['id'] == id:
            return user
    return "Not found"
    
