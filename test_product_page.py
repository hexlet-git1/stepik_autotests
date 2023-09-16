from .pages.product_page import ProductPage
from .pages.main_page import BasePage
import time
import pytest

# Берем  код, использующий цикл для прогона номеров промо дописываем маркировку XFail - @pytest.mark.xfail(reason="Bug in this promo-link") Затем запускаем тест с параметрами -v (подробно пишет Xpass/Xfail) и -rx (выдает в конце оповещение - не прошедшую тест ссылку и сообщение, указанное в reason). Код позволяет быстро настроить автотесты хоть на тысячу номерных акций (всего лишь поменять число в цикле), а также автоматически будет выводить Xpass/Xfail для тестов с параметрами -v -rx (поскольку сегодня может не работать что-то по одной ссылке, а завтра заработает и перестанет работать по другой ссылке).

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]
@pytest.mark.parametrize('link', urls)

@pytest.mark.xfail(reason="Bug in this promo-link")
def test_guest_can_add_product_to_basket(browser, link):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    base_page = BasePage(browser, link)
    base_page.solve_quiz_and_get_code()
    page.name_product_in_basket_correct()
    page.price_product_in_basket_correct()
    # time.sleep(1)
    
