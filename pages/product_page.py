# Работа с корзиной и товарами
import pytest
from .base_page import BasePage
from .locators import PageProductLocators


class PageObject(BasePage):
    # Добавляем товар в корзину
    def add_to_basket(self):
        link = self.browser.find_element(*PageProductLocators.BTN_ADD_BSKT)
        link.click()

    @pytest.mark.xfail
    # Получаем со страницы товара наименование и цену, понадобится для проверки
    def check_price_and_name_product(self):
        name = self.browser.find_element(*PageProductLocators.NAME_PROD).text
        price = self.browser.find_element(*PageProductLocators.PRICE_PROD).text
        name_bskt = self.browser.find_element(*PageProductLocators.NAME_BSKT).text
        price_bskt = self.browser.find_element(*PageProductLocators.PRICE_BSKT).text
        assert (name == name_bskt and price == price_bskt), "A product information from a basket is'n a product information from a page product"

    # Проверка поиска элемента на странице
    def should_be_add_to_basket_link(self):
        assert self.is_element_present(*PageProductLocators.BTN_ADD_BSKT), "Add to basket link is not presented"
