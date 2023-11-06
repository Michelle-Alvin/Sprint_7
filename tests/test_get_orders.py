#import allure
import requests


class TestGetOrders:
    #@allure.title("Проверка запроса списка заказов")
    def test_list_of_orders(self, create_order):
        response = requests.get("https://qa-scooter.praktikum-services.ru/api/v1/orders")

        assert response.json()['orders']
