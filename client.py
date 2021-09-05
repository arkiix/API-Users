import requests


URL = 'http://127.0.0.1:8000/'


def create_user(name):
    cur_url = URL + 'create/'
    resp = requests.post(cur_url, json={'name': name})
    print(resp.text)


def delete_user(id: int):
    cur_url = URL + 'delete/'
    resp = requests.post(cur_url, json={'id': id})
    print(resp.text)


def update_user(id: int, name: str):
    cur_url = URL + 'update/'
    resp = requests.post(cur_url, json={'id': id, 'name': name})
    print(resp.text)


def get_user(id: int):
    cur_url = URL + f'user/{id}'
    resp = requests.get(cur_url)
    print(resp.text)