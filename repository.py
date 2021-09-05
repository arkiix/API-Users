import config
import json_storage
import DB


if config.DB:
    storage = DB
else:
    storage = json_storage


def create_user(name):
    return storage.create_user(name)


def update_user(user):
    return storage.update_user(user)


def delete_user(id):
    return storage.delete_user(id)


def get_user(id):
    return storage.get_user(id)