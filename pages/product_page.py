from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.basket)
        basket.click()
       
    def name_product_in_basket_correct(self):
        item_name_message_text = self.browser.find_element(*ProductPageLocators.item_name_message).text
        item_name_text = self.browser.find_element(*ProductPageLocators.item_name).text
        assert item_name_message_text == item_name_text, "Name product  in cart not correct" 
        
    def price_product_in_basket_correct(self):
        item_price_message_text = self.browser.find_element(*ProductPageLocators.item_price_message).text
        item_price_text = self.browser.find_element(*ProductPageLocators.item_price).text
        assert item_price_message_text == item_price_text, f"Price f{item_price_message_text} product in cart not correct {item_price_text}"
        