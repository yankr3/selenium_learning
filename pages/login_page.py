from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators

# Класс тестирования стрицы авторизации
class LoginPage(BasePage):

    # Проверяем наличие страцы авторизации, форм регистрации и авторизации
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOG_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Registration form is not presented"