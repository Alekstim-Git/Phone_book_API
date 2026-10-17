import requests

from config import TEST_USER_EMAIL, TEST_USER_PASSWORD, API_BASE_URL


def test_login_with_valid_credentials_return_token():
    payload = {
        "username": TEST_USER_EMAIL,
        "password": TEST_USER_PASSWORD
    }

    response = requests.post(f"{API_BASE_URL}/v1/user/login/usernamepassword", json=payload)
    assert response.status_code == 200

    body = response.json()
    assert "token" in body
    assert len(body["token"]) > 0
    assert "application/json" in response.headers["Content-Type"]


def test_registration_user_success():
    new_user = {
        "username": "Kykakyy@gmail.com",
        "password": "Password123!"
    }
    response = requests.post(f"{API_BASE_URL}/v1/user/registration/usernamepassword", json=new_user)
    assert response.status_code == 200

    body = response.json()
    assert "token" in body

    # Проверяем, что под новым пользователем действительно можно зайти
    login_response = requests.post(f"{API_BASE_URL}/v1/user/login/usernamepassword",json=new_user)
    assert login_response.status_code == 200
    assert "token" in login_response.json()
