import random
import string

import requests


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def generate_json_body_new_courier():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    return payload


def login_courier(login, password):
    payload = {
        "login": login,
        "password": password
    }
    r = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier/login", data=payload)

    return r.json()["id"]


def delete_courier_by_log_pass(login, password):
    id_courier = login_courier(login, password)
    requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{id_courier}')


def register_new_courier_and_return_login_password():
    payload = generate_json_body_new_courier()
    login_pass = []

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    if response.status_code == 201:
        login_pass.append(payload['login'])
        login_pass.append(payload['password'])
        login_pass.append(payload['firstName'])

    return login_pass
