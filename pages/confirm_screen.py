from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class OrderConfirmationPage(BasePage):
    CONFIRMATION_MSG = (By.XPATH, "//strong[normalize-space()='Your order has been successfully processed!']")
    FINAL_CONTINUE = (By.XPATH, "//input[@value='Continue']")
    CART_TEXT = (By.CLASS_NAME, "cart-label")
    TOOL_TIP_TEXT = (By.XPATH, "//div[@class='count']")

    def get_confirmation_text(self):
        self.click(self.FINAL_CONTINUE)
    #    return self.get_text(self.CONFIRMATION_MSG)
