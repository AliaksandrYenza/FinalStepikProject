from .pages.login_page import LoginPage
from .pages.main_page import MainPage



def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=midsummer"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page() #1
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_link_login() #1


def test_login_page_elements_present(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()
    page.should_be_login_page()
    page.should_be_login_url()
    page.should_be_register_form()


