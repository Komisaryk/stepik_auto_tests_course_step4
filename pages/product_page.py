from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
        add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_to_cart.click()

    def should_be_alert_that_the_product_added_to_the_basket(self):
        self.should_be_alert()
        self.should_be_product_name_in_alert()

    def should_be_alert(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_PRODUCT_ADDED), "Product added alert is not presented"

    def should_be_product_name_in_alert(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        alert_txt = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_ADDED_INNER_TXT).text
        assert product_name == alert_txt, "Alert message don't contains product name"

    def should_be_alert_with_basket_cost(self):
        self.should_be_alert_price()
        self.should_be_price_in_alert()

    def should_be_alert_price(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_CART_PRICE), "Cart price alert is not presented"

    def should_be_price_in_alert(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        alert_txt = self.browser.find_element(*ProductPageLocators.ALERT_CART_PRICE_TXT).text
        assert product_price == alert_txt, "Alert don't contains product price"