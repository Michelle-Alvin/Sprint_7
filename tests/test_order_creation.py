#import allure
import pytest
import requests


class TestOrderCreation:
    #@allure.title("Проверка выбора цвета")
    @pytest.mark.parametrize("color", [
        ["BLACK", "GREY"],
        ["BLACK", ""],
        ["", ""]
    ])
    def test_create_order_color_variation(self, color):
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [color]
        }

        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/orders", data=payload)

        assert response.status_code == 201
        assert response.json()["track"] is not None
