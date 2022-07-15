from selenium.webdriver.common.by import By


# Селектор для перехода на страницу авторизации
class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


# Селекторы поиска форм авторизации и регистрации
class LoginPageLocators:
    LOG_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")


class PageProductLocators:
    # Кнопка добавления в корзину
    BTN_ADD_BSKT = (By.CSS_SELECTOR, ".btn-add-to-basket")
    # Наименование товара на странице товара
    NAME_PROD = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    # Цена товара на странице товара
    PRICE_PROD = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    # Наименование товара в корзине
    NAME_BSKT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    # Цена товара в корзине
    PRICE_BSKT = (
        By.CSS_SELECTOR,
        "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
