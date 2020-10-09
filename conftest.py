import pytest


@pytest.fixture(scope="session")
def login():
    return "登录"
