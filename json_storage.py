import json


def read_json():
    with open('users.json', 'r') as f:
        users_json = json.load(f)
    return users_json


def write_json(data):
    with open('users.json', 'w') as f:
        json.dump(data, f, indent=4)


def create_user(name):
    users_json = read_json()

    id = 0
    list_id = list(users_json['users'])[::-1]
    if len(list_id) > 0:
        id = int(list_id[0][4:]) + 1

    users_json['users'][f'user{id}'] = {'id': id, 'name': name}
    write_json(users_json)
    return f'Done! Your id: {id}'


def delete_user(id):
    users_json = read_json()
    users_json['users'][f'user{id}'] = {}
    write_json(users_json)
    return 'Done!'


def update_user(user):
    users_json = read_json()
    users_json['users'][f'user{user.id}'] = {'id': user.id, 'name': user.name}
    write_json(users_json)
    return 'Done!'


def get_user(id):
    users_json = read_json()
    try:
        name = users_json['users'][f'user{id}']['name']
    except:
        name = 'User not found'
    return name