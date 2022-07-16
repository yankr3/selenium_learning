# Страница карточки товара


import pytest
from .base_page import BasePage
from .locators import PageProductLocators


class PageObject(BasePage):
    # Добавление товара в корзину
    def add_to_basket(self):
        link = self.browser.find_element(*PageProductLocators.BTN_ADD_BSKT)
        link.click()

    # Проверка совпадения наименования и цены со страницы товара до добавления и после
    @pytest.mark.xfail
    def check_price_and_name_product(self):
        name = self.browser.find_element(*PageProductLocators.NAME_PROD).text
        price = self.browser.find_element(*PageProductLocators.PRICE_PROD).text
        name_bskt = self.browser.find_element(*PageProductLocators.NAME_BSKT).text
        price_bskt = self.browser.find_element(*PageProductLocators.PRICE_BSKT).text
        assert (name == name_bskt and price == price_bskt), "A product information from a basket is'n a product information from a page product"

    # Наличие кнопки добавления в корзину
    def should_be_add_to_basket_link(self):
        assert self.is_element_present(*PageProductLocators.BTN_ADD_BSKT), "Add to basket link is not presented"

    # Сообщение об успешном добавлении товара не появляется в течение заданного времени
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*PageProductLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    # Сообщение об успешном добавлении товара исчезает в течение заданного времени
    def success_message_is_disappeared(self):
        assert self.is_disappeared(*PageProductLocators.SUCCESS_MESSAGE), \
            "Element is disappeared before"


