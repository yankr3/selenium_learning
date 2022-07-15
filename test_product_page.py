import pytest
from .pages.product_page import PageObject

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
