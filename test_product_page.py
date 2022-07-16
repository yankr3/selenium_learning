import pytest
from .pages.product_page import PageObject
from .pages.basket_page import BasketPage

links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
         pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                      marks=pytest.mark.xfail),
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]

# links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"]


@pytest.mark.parametrize('link', links)
def test_guest_can_add_to_basket(browser, link):
    page = PageObject(browser, link)
    page.open()
    # Добавляем товар в корзину
    page.add_to_basket()
    # Считаем во всплывающем окне значение и заполняем его в окно
    page.solve_quiz_and_get_code()
    # Сравниваем значения цен и наименований книги из корзины и со страницы товара
    page.check_price_and_name_product()
    # Проверка ссылки
    add_basket_page = PageObject(browser, browser.current_url)
    add_basket_page.should_be_add_to_basket_link()


# Тест на то, что не должно быть сообщения об успешном добавлении товара в корзину (оно есть, тест падает)
@pytest.mark.xfail
@pytest.mark.parametrize('link', links)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = PageObject(browser, link)
    page.open()
    # Добавляем товар в корзину
    page.add_to_basket()
    add_basket_page = PageObject(browser, browser.current_url)
    add_basket_page.should_not_be_success_message()


# Тест на то, что не должно быть сообщения об успешном добавлении товара в корзину (его нет, тест проходит)
@pytest.mark.xfail
@pytest.mark.parametrize('link', links)
def test_guest_cant_see_success_message(browser, link):
    page = PageObject(browser, link)
    page.open()
    page.should_not_be_success_message()


# Тест на то, что сообщение об успешном добавлении товара в корзину должно пропасть (этого не происходит, тест падает)
@pytest.mark.xfail
@pytest.mark.parametrize('link', links)
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = PageObject(browser, link)
    page.open()
    # Добавляем товар в корзину
    page.add_to_basket()
    add_basket_page = PageObject(browser, browser.current_url)
    add_basket_page.success_message_is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PageObject(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PageObject(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PageObject(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_text_basket_is_empty()
    basket_page.should_not_be_products_in_basket()

