from selenium.webdriver.common.by import By

class MainPageLocators():
    login_link = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    login_form = (By.CSS_SELECTOR, "#login_form")
    reg_form = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    basket = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    item_name_message = (By.CSS_SELECTOR, "#messages > .alert.alert-safe.alert-noicon.alert-success:nth-child(1) .alertinner strong")
    item_price_message = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in .alertinner p strong")
    item_name = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    item_price = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
       
       