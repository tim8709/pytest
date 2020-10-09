import pytest
import yaml


# @pytest.fixture()
# def login():
#     return "登录"
#
#
# class TestLogin:
#     def test_case1(self, login):
#         print(login)
#         print("需要登录")
#
#     def test_case2(self):
#         print("不需要登录")
#
#     @pytest.mark.usefixtures("login")
#     def test_case3(self):
#         print("需要登录")
#
#######################################
#
# @pytest.fixture(autouse=True)
# def login():
#     return "登录"
#
#
# class TestLogin:
#     def test_case(self):
#         print(login)
#         print("需要登录")
#
#######################################
#
# @pytest.fixture()
# def login1():
#     return "登录1"
#
#
# @pytest.fixture()
# def login2():
#     return "登录2"
#
#
# class TestLogin:
#     def test_case1(self, login1, login2):
#         print(login1, login2)

########################################

# @pytest.fixture(scope="class")
# def login():
#     return "登录"
#
#
# class TestLogin:
#     def test_case1(self, login):
#         print("case1")
#
#     def test_case2(self):
#         print("case2")
#
#     def test_case3(self):
#         print("case3")
#
#
# class TestLogin2:
#     def test_case4(self):
#         print("case4")
#
#     def test_case5(self):
#         print("case5")
#
#     def test_case6(self):
#         print("case6")

########################################

# 调用conftest.py文件中的公共方法login
# class TestLogin:
#     def test_case1(self, login):
#         print("case1")
#
#     def test_case2(self):
#         print("case2")
#
#     def test_case3(self):
#         print("case3")

########################################
# 参数化
@pytest.fixture(params=[1, 2, 3])
def login(request):
    return request.param


class TestLogin:
    def test_case(self, login):
        print(f"{login}")
