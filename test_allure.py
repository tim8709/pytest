import pytest
import allure


@allure.feature("登录模块")
class TestLogin:
    @allure.story("登录成功")
    def test_login_success(self):
        print("登录成功")

    @allure.story("登录失败")
    def test_login_fail(self):
        print("登录失败")

    @allure.story("密码缺失")
    def test_input_pwd(self):
        with allure.step("输入用户名"):
            print("输入用户名")
        with allure.step("点击登录按钮"):
            print("点击登录按钮")

    def test_attach_text(self):
        allure.attach("我是文本", attachment_type=allure.attachment_type.TEXT)

    def test_attach_html(self):
        allure.attach("<body>我是htmlbody内容</body>", "html", attachment_type=allure.attachment_type.TEXT)

    def test_attach_image(self):
        allure.attach.file("./image/DCIM(3).jpg", name="image", attachment_type=allure.attachment_type.JPG)


# TRIVIAL：不重要，必填项无提示，或提示不规范
@allure.severity(allure.severity_level.TRIVIAL)
def test_trivial():
    print("trivial")


# MINOR：不太重要，界面错误或UI需求不符
@allure.severity(allure.severity_level.MINOR)
def test_minor():
    print("minor")


# NORMAL：普通，数值计算错误
@allure.severity(allure.severity_level.NORMAL)
def test_normal():
    print("normal")


# CRITICAL：严重，功能点缺失
@allure.severity(allure.severity_level.CRITICAL)
def test_critical():
    print("critical")


# BLOCKER：阻塞，中断缺陷，程序无响应，无法执行下一步操作
@allure.severity(allure.severity_level.BLOCKER)
def test_blocker():
    print("blocker")
