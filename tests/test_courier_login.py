import allure
import requests

from courier_genarate import generate_random_string


class TestCourierLogin:
    @allure.title("Проверка успешной авторизации")
    def test_courier_success_authenticate(self):
        payload = {
            "login": "ninja123ninja",
            "password": "1234"
        }

        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier/login", data=payload)

        assert response.status_code == 200
        assert response.json()["id"] is not None

    @allure.title("Проверка необходимости обязательных полей для авторизации")
    def test_auth_requires_all_required_fields(self):
        payload = {
            "password": "1234"
        }

        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier/login", data=payload)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Проверка возвращаемой ошибки при неправильном пароле")
    def test_auth_with_incorrect_password_error(self):
        payload = {
            "login": "ninja123ninja",
            "password": "12345"
        }

        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier/login", data=payload)

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Проверка получения ошибки при пустом обязательном поле")
    def test_auth_with_missing_fields_error(self):
        payload = {
            "login": "",
            "password": "1234"
        }

        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier/login", data=payload)

        assert response.status_code == 400

    @allure.title("Проверка авторизации несуществующего пользователя")
    def test_auth_nonexistent_user_error(self):
        login = generate_random_string(10)

        payload = {
            "login": login,
            "password": "1234"
        }

        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier/login", data=payload)

        assert response.json()['message'] == "Учетная запись не найдена"

    @allure.title("Проверка возвращаемого id в ответе авторизации")
    def test_successful_auth_returns_id(self):
        payload = {
            "login": "ninja123ninja",
            "password": "1234"
        }

        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier/login", data=payload)

        assert response.json()['id'] is not None, 'Поля "id" нет в ответе'
