from fastapi import FastAPI
from models import *
import repository


app = FastAPI()


@app.post("/create/")
async def create_user(user: User):
    return repository.create_user(user.name)


@app.post("/update/")
async def update_user(user: User):
    return repository.update_user(user)


@app.get("/user/{user_id}")
async def get_user(user_id: int):
    return {'name': repository.get_user(user_id)}


@app.post("/delete/")
async def delete_user(user: User):
    return repository.delete_user(user.id)