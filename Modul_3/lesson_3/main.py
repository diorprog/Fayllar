
import json


def decorator(func):
    def wrapper(user: dict):
        if 5 <= user['id'] <=10:
            return func(user)

    return wrapper


@decorator
def print_user(user: dict):
    return user['id'] , user['name']


with open("users.json" , 'r') as f:
    for user in json.load(f):
        response = print_user(user)
        if response:
            print(response)
