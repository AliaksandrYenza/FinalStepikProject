import pytest

from test.page.product_page import ProductPage

#
# xfile = 7
# mask = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
# links = [mask+str(i) for i in range(10) if i != xfile]
# xlink = pytest.param(mask+str(xfile), marks=pytest.mark.xfail(reason="mistake on page"))
# links.insert(xfile, xlink)

links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"]

@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):

    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_page()


