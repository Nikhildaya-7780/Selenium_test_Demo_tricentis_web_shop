from selenium.webdriver.common.by import By

from pages import base_page


class CheckoutPage(base_page.BasePage):

    TERMS_OF_SERVICE = (By.ID, "termsofservice")
    CHECKOUT_BUTTON = (By.XPATH, "//button[@class='button-1 checkout-button']")

    def checkout_process(self):
        self.click(self.TERMS_OF_SERVICE)
        self.click(self.CHECKOUT_BUTTON)