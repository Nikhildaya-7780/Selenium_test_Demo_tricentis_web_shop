from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    APPAREL_SHOES = (By.XPATH, "//a[contains(@href, 'apparel-shoes')]")
    BLUE_JEANS_ADD_TO_CART = (By.CSS_SELECTOR, "body > div:nth-child(4) > div:nth-child(1) > div:nth-child(5) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(2) > input:nth-child(1)")
    PRODUCT_ADDED_TO_CART_TEXT = (By.CLASS_NAME, "content")
    CLOSE_HEADER_BUTTON = (By.CLASS_NAME, "close")
    SELECT_SHOPPING_CART = (By.CLASS_NAME, "ico-cart")


    def go_to_apparel_and_add_jeans(self):
        self.scroll_into_view(self.APPAREL_SHOES)
        self.click(self.APPAREL_SHOES)
        self.scroll_into_view(self.BLUE_JEANS_ADD_TO_CART)
        self.click(self.BLUE_JEANS_ADD_TO_CART)
        message = self.get_text(self.PRODUCT_ADDED_TO_CART_TEXT)
        self.click(self.CLOSE_HEADER_BUTTON)
        self.wait_for_element_to_disappear(self.CLOSE_HEADER_BUTTON)
        self.click(self.SELECT_SHOPPING_CART)
        return message



