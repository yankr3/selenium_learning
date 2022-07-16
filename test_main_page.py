from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time


# Открыть страницу авторизации и проверить есть ли поля авторизации и регистрации
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    # создаем экземляр браузера с переданной ссылкой (MainPage -> BasePage -> init)
    page = MainPage(browser, link)
    # Открываем браузер по переданной ссылке (MainPage -> BasePage -> open)
    page.open()
    # Переходим на страницу авторизации (MainPage -> метод go_to_login_page)
    time.sleep(6)
    page.go_to_login_page()
    # создаем экземляр браузера с текущей ссылкой (LoginPage -> BasePage -> init)
    login_page = LoginPage(browser, browser.current_url)
    # Тестируем страницу авторизации на наличие форм регистрации и авторизации методом should_be_login_page из класса LoginPage
    login_page.should_be_login_page()


# Проверяем есть ли вообще стрица авторизации, возвращаем исключение, если нет
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_text_basket_is_empty()
    basket_page.should_not_be_products_in_basket()

