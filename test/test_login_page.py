from .pages.login_page import LoginPage

def test_login_page_elements_present(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    page = LoginPage(link, browser)
