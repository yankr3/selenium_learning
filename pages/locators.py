from selenium.webdriver.common.by import By


class BasePageLocators:
    # Кнопка для перехода на станицу авторизации
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # Ложная кнопка для перехода на станицу авторизации
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    # Пользователь авторизован
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


# Корзина пользователя
class BasketLocators:
    # Кнопка перехода в корзину
    BASKET_LINK = (
    By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    # Поле с сообщением о том, что корзина пуста
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
    # Форма с продуктами в корзине
    ELEM_IN_BASKET = (By.CSS_SELECTOR, "#basket_formset > div > div")


# Страница авторизации
class LoginPageLocators:
    # Форма авторизации
    LOG_FORM = (By.CSS_SELECTOR, "#login_form")
    # Форма регистрации
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    # Поле имейла регистрации
    REG_FORM_LOGIN = (By.CSS_SELECTOR, '#id_registration-email')
    # Поле пароля регистрации
    REG_FORM_PASSW1 = (By.CSS_SELECTOR, '#id_registration-password1')
    # Поле повтора пароля регистрации
    REG_FORM_PASSW2 = (By.CSS_SELECTOR, '#id_registration-password2')
    # Кнопка регистрации
    REG_FORM_BTN = (By.CSS_SELECTOR, '#register_form > button')


# Карточка товара
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
    # Сообщение об успешном добавлении товара
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)")
