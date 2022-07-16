import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

links = ["http://selenium1py.pythonanywhere.com"]


# Работа с кнопкой корзины на стартовой странице
@pytest.mark.guests_basket_from_main
class TestGuestsAddProductToBasket:
    # Наличие сообщения о пустоте корзины и отсутствие товаров в корзине при переходе со стартовой страницы
    @pytest.mark.parametrize('link', links)
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_text_basket_is_empty()
        basket_page.should_not_be_products_in_basket()


# Работа с кнопкой авторизации на стартовой странице
@pytest.mark.login_guest
class TestLoginFromMainPage:
    # Переход на страницу авторизации и проверка наличия полей авторизации и регистрации
    @pytest.mark.parametrize('link', links)
    def test_guest_can_go_to_login_page(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    # Проверка наличия кпонки авторизации
    @pytest.mark.parametrize('link', links)
    def test_guest_should_see_login_link(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
