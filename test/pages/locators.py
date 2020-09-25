from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    LOGIN_EMAIL = (By.CSS_SELECTOR, '.form-control#id_login-username')
    LOGIN_PASS = (By.CSS_SELECTOR, '.form-control#id_login-password')
    LOGIN_FORGOTTEN_LINK = (By.CSS_SELECTOR, '.col-sm-6.login_form p a[href]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.col-sm-6.login_form .btn.btn-lg.btn-primary ')

    REGISTER_EMAIL = (By.CSS_SELECTOR, '.form-control#id_registration-email')
    REGISTER_PASS = (By.CSS_SELECTOR, '.form-group #id_registration-password1')
    REGISTER_CONFIRM_PASS = (By.CSS_SELECTOR, '.form-control#id_registration-password2')
