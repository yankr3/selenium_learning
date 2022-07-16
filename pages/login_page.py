# Страница авторизации и регистрации


from .base_page import BasePage
from .locators import BasePageLocators
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    # Наличие кнопки авторизации
    def should_be_login_url(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    # Наличие формы авторизации на странице регистрации
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOG_FORM), "Login form is not presented"

    # Наличие формы регистрации на странице регистрации
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Registration form is not presented"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # Регистрация пользователя
    def register_new_user(self, email, password):
        login = self.browser.find_element(*LoginPageLocators.REG_FORM_LOGIN)
        login.send_keys(email)
        passwd1 = self.browser.find_element(*LoginPageLocators.REG_FORM_PASSW1)
        passwd1.send_keys(password)
        passwd2 = self.browser.find_element(*LoginPageLocators.REG_FORM_PASSW2)
        passwd2.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REG_FORM_BTN)
        time.sleep(2)
        button.click()
