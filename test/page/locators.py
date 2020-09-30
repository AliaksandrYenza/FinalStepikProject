from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_URL = 'login'


class BasketLocators():
    BASKET_PART_URL = '?promo=newYear'
    BASKET_BUTTON_ADD = (By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary.btn-add-to-basket')
    BASKET_PRICE = (By.CSS_SELECTOR, '.col-sm-6.product_main .price_color')
    BASKET_NAME = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')

    BASKET_BENEFIT = 'Deferred benefit offer'



class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")