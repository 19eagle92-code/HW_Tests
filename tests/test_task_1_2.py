import pytest
from task_1_2 import check_auth


def test_check_auth():
    assert check_auth("admin", "password") is True


params = (("user", "123"), ("Kirill@mail.ru", "password"), ("", ""))


@pytest.mark.parametrize("login, password", params)
def test_check_auth_params(login, password):
    assert check_auth(login, password) == False


def test_check_auth_return_type():
    result = check_auth("admin", "password")
    assert isinstance(result, bool)


@pytest.fixture
def valid_data():
    return {"login": "admin", "password": "password"}


def test_check_auth_with_fixture(valid_data):
    assert check_auth(valid_data["login"], valid_data["password"]) == True
