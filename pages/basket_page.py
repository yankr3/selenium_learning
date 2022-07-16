import pytest
from .base_page import BasePage
from .locators import BasketLocators


class BasketPage(BasePage):

    def should_be_text_basket_is_empty(self):
        assert self.is_element_present(*BasketLocators.BASKET_EMPTY), 'Basket is not empty'

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketLocators.ELEM_IN_BASKET), 'There is products in the basket'


