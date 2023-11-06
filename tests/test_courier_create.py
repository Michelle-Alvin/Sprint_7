import requests
# import allure

from courier_genarate import generate_json_body_new_courier
from courier_genarate import generate_random_string
from courier_genarate import register_new_courier_and_return_login_password


#@allure.title("Тесты метода создания курьера")
class TestCourierCreate:
    #@allure.title("Проверка успешного создание курьера")
    def test_create_courier_success(self):
        login_pass = register_new_courier_and_return_login_password()

        assert login_pass, "Курьер не создан, код статус отличается от 201"

    #@allure.title("Проверка дубликата данных")
    def test_courier_duplicate_prevention(self):
        login_pass = register_new_courier_and_return_login_password()

        payload = {
            "login": login_pass[0],
            "password": login_pass[1],
            "firstName": login_pass[2]
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        assert response.status_code == 409, "Ошибка дубликата не получена (409)"

    #@allure.title("Проверка создания с неполным набором обязательных полей")
    def test_error_response_for_missing_fields(self):
        payload = {
            "login": "blabla",
            "firstName": "test"
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        assert response.status_code == 400

    #@allure.title("Проверка корректного код статуса при успешном создании")
    def test_response_code_for_courier_creation(self):
        payload = generate_json_body_new_courier()

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        assert response.status_code == 201

    #@allure.title("Проверка корректного тела ответа в создании курьера")
    def test_successful_courier_creation_response(self):
        payload = generate_json_body_new_courier()

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        expect_response = {"ok": True}

        assert response.json() == expect_response

    #@allure.title("Проверка создания без необязательных полей")
    def test_required_fields_for_courier_creation(self):
        login = generate_random_string(10)
        password = generate_random_string(10)

        payload = {
            "login": login,
            "password": password
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        assert response.status_code == 201

    #@allure.title("Проверка создания курьера с существующим логином")
    def test_error_response_for_duplicate_courier(self):
        resp = register_new_courier_and_return_login_password()
        login = resp[0]
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        assert response.json()['message'] == "Этот логин уже используется. Попробуйте другой."
