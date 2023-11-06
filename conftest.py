import pytest
import requests


@pytest.fixture
def create_order():
    payload = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2023-11-10",
        "comment": "Saske, come back to Konoha"
    }

    response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/orders", data=payload)
    track = response.json()["track"]

    yield track

    requests.post("https://qa-scooter.praktikum-services.ru/api/v1/orders/cancel", data=response)
