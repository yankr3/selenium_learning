import pytest
from .pages.product_page import PageObject
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time

# links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#          pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                       marks=pytest.mark.xfail),
#          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]

links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"]


# Добавление Гостем товара со страницы карточки товара
@pytest.mark.add_products_from_guest
class TestGuestsAddToBasketFromProductPage:
    # Возможность добавления товара в корзину и неизменность цены/названия товара после добавления
    @pytest.mark.need_review
    @pytest.mark.parametrize('link', links)
    def test_guest_can_add_to_basket(self, browser, link):
        page = PageObject(browser, link)
        page.open()
        page.add_to_basket()
        # Подсчет прверочного значения
        # page.solve_quiz_and_get_code()
        page.check_price_and_name_product()
        page.should_be_add_to_basket_link()

    # Отсутсвие сообщения об успешном добавлении товара в корзину до его добавления (его нет, тест проходит)
    @pytest.mark.xfail
    @pytest.mark.parametrize('link', links)
    def test_guest_cant_see_success_message(self, browser, link):
        page = PageObject(browser, link)
        page.open()
        page.should_not_be_success_message()


# Работа Гостя с кнопкой авторизации
@pytest.mark.guest_login_page_from_PP
class TestGuestsLoginFromProductPage:
    # Наличие кнопки переход на страницу авторизации со страницы продукта
    @pytest.mark.parametrize('link', links)
    def test_guest_should_see_login_link_on_product_page(self, browser, link):
        page = PageObject(browser, link)
        page.open()
        page.should_be_login_link()

    # Переход на страницу авторизации со страницы продукта
    @pytest.mark.need_review
    @pytest.mark.parametrize('link', links)
    def test_guest_can_go_to_login_page_from_product_page(self, browser, link):
        page = PageObject(browser, link)
        page.open()
        page.go_to_login_page()


# Работа Гостя с товарами и корзиной
@pytest.mark.work_with_guests_basket
class TestGuestsWorkWithBasket:
    # Отсутствие на странице товара сообщения об успешном добавлении товара в корзину после его добавления (оно есть, тест падает)
    @pytest.mark.xfail
    @pytest.mark.parametrize('link', links)
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser, link):
        page = PageObject(browser, link)
        page.open()
        # Добавляем товар в корзину
        page.add_to_basket()
        page.should_not_be_success_message()

    # Исчезновение на странице товара сообщения об успешном добавлении товара после добавления (этого не происходит, тест падает)
    @pytest.mark.xfail
    @pytest.mark.parametrize('link', links)
    def test_message_disappeared_after_adding_product_to_basket(self, browser, link):
        page = PageObject(browser, link)
        page.open()
        # Добавляем товар в корзину
        page.add_to_basket()
        page.success_message_is_disappeared()

    # Наличие сообщения о пустоте корзины и отсутствие товаров в корзине при переходе со стартовой товара
    @pytest.mark.need_review
    @pytest.mark.parametrize('link', links)
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser, link):
        page = PageObject(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_text_basket_is_empty()
        basket_page.should_not_be_products_in_basket()


# Добавление Гостем товара со страницы карточки товара с последующей регистрацией
@pytest.mark.add_products_from_user
class TestUsersAddToBasketFromProductPage:
    # Возможность добавления товара в корзину и неизменность цены/названия товара после добавления, регистрация после добавления
    @pytest.mark.need_review
    @pytest.mark.parametrize('link', links)
    def test_user_can_add_to_basket(self, browser, link):
        mail = str(time.time()) + "@fakemail.org"
        page = PageObject(browser, link)
        page.open()
        page.add_to_basket()
        # page.solve_quiz_and_get_code()
        page.should_be_add_to_basket_link()
        page.check_price_and_name_product()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(mail, '12345dcdvd5')
        login_page.should_be_authorized_user()

    # Отсутсвие сообщения об успешном добавлении товара в корзину до его добавления (его нет, тест проходит), регистрация после проверки
    @pytest.mark.parametrize('link', links)
    def test_user_cant_see_success_message(self, browser, link):
        mail = str(time.time()) + "@fakemail.org"
        page = PageObject(browser, link)
        page.open()
        page.should_not_be_success_message()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(mail, '12345dcdvd5')
        login_page.should_be_authorized_user()
