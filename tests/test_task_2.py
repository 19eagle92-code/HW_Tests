from uuid import uuid4
import os
import pytest
import requests
from dotenv import load_dotenv


BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources"


# @pytest.fixture
# def session(headers):
#     sess = requests.Session()
#     sess.headers.update(headers)
#     return sess


@pytest.fixture
def token():
    load_dotenv()
    token = os.getenv("token_yandex")
    if not token:
        pytest.fail("YANDEX_TOKEN не установлен в переменных окружения")
    return token


@pytest.fixture
def headers(token):
    return {"Authorization": f"OAuth {token}"}


@pytest.fixture
def temp_folder():
    """Генерирует уникальное имя папки"""
    return f"test-folder-{uuid4()}"


@pytest.fixture
def create_and_cleanup_folder(headers, temp_folder):
    """Создаёт папку и удаляет её после теста"""
    folder_path = f"disk:/{temp_folder}"
    # Создание
    response = requests.put(BASE_URL, headers=headers, params={"path": folder_path})
    assert response.status_code in [201, 409], f"Ошибка при создании: {response.text}"

    yield temp_folder  # передаём управление в тест

    # Удаление после теста
    requests.delete(
        BASE_URL, headers=headers, params={"path": folder_path, "permanently": "true"}
    )


def test_create_folder_success(headers, temp_folder):
    response = requests.put(
        BASE_URL, headers=headers, params={"path": f"disk:/{temp_folder}"}
    )
    assert response.status_code in [201, 409]

    check_response = requests.get(
        BASE_URL, headers=headers, params={"path": f"disk:/{temp_folder}"}
    )

    assert check_response.status_code == 200
    assert check_response.json()["name"] == temp_folder


def test_create_existing_folder(headers, create_and_cleanup_folder):
    folder = create_and_cleanup_folder
    response = requests.put(
        BASE_URL, headers=headers, params={"path": f"disk:/{folder}"}
    )
    assert response.status_code == 409


def test_create_folder_invalid_path(headers):
    response = requests.put(BASE_URL, headers=headers, params={"path": "disk://///"})
    assert response.status_code == 404


def test_create_folder_no_token(temp_folder):
    response = requests.put(BASE_URL, params={"path": f"disk:/{temp_folder}"})

    assert response.status_code == 401


def test_create_folder_with_wrong_token(temp_folder):
    headers = {"Authorization": "OAuth wrong_{token}"}

    response = requests.put(
        BASE_URL, headers=headers, params={"path": f"disk:/{temp_folder}"}
    )

    assert response.status_code == 401
