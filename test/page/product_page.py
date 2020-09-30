from selenium.webdriver.common.by import By

from test.page.base_page import BasePage
from test.page.locators import BasketLocators


class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_be_basket_url()
        self.should_be_new_message_of_name_adding()
        self.should_be_new_message_of_benefit_adding()
        self.should_be_same_price()


    def add_to_basket(self):
        button_add_item_to_basket = self.browser.find_element(*BasketLocators.BASKET_BUTTON_ADD)
        button_add_item_to_basket.click()


    def should_be_basket_url(self):
        assert (BasketLocators.BASKET_PART_URL in self.url)


    def should_be_new_message_of_name_adding(self):
        alert_name = self.browser.find_element(By.CSS_SELECTOR, '.alert-success:nth-child(1)').text
        BASKET_NAME = self.browser.find_element(*BasketLocators.BASKET_NAME).text
        assert (BASKET_NAME in str(alert_name)), '\n\n\nNAME ERROR\n\n\n'


    def should_be_new_message_of_benefit_adding(self):
        alert_benefits = self.browser.find_element(By.CSS_SELECTOR, '.alert-success:nth-child(2)').text
        assert (BasketLocators.BASKET_BENEFIT in alert_benefits), '\n\n\nBENEFITS ERROR\n\n\n'


    def should_be_same_price(self):
        alert_price = self.browser.find_element(By.CSS_SELECTOR, '.alert.alert-safe.alert-noicon.alert-info.fade.in strong').text
        assert self.browser.find_element(*BasketLocators.BASKET_PRICE).text == alert_price, '\n\n\nPRICE ERROR\n\n\n'


