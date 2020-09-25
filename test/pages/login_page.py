from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self):
        assert self.cur_url in LoginPageLocators.LOGIN_URL, "LOGIN_URL is not presented"

        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "LOGIN_EMAIL is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASS), "LOGIN_PASS is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORGOTTEN_LINK), "LOGIN_FORGOTTEN_LINK is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "LOGIN_BUTTON is not presented"
        #тут должна быть одна проверка на общий цсс селектор всей формы, но я затупил

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), "REGISTER_EMAIL is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASS), "REGISTER_PASS is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_CONFIRM_PASS), "REGISTER_CONFIRM_PASS is not presented"
        #аналогично как и выше