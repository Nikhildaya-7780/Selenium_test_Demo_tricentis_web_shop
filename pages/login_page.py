from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage

class LoginPage(BasePage):
    # Locators
    LOGIN_LINK = (By.CLASS_NAME, "ico-login")
    EMAIL_INPUT = (By.ID, "Email")
    PASSWORD_INPUT = (By.ID, "Password")
    REMEMBER_ME_CHECKBOX = (By.ID, "RememberMe")
    SUBMIT_BUTTON = (By.XPATH, "//input[@type='submit']")
    APPAREL_SHOES = (By.CLASS_NAME, "Apparel & Shoes")
    BLUE_JEANS_ADD_TO_CART = (By.XPATH, "//div[@class='product-grid']//div[3]//div[1]//div[2]//div[3]//div[2]//input[1]")
    PRODUCT_ADDED_TO_CART_TEXT = (By.XPATH, "//p[@class='content']")
    ACCOUNT_NAME = (By.CLASS_NAME, "account")
    POPUP_OK_BUTTON = (By.XPATH, "//input[@value='OK' or @type='button' or @class='button-1']")

    def go_to_login_page(self, base_url):
        self.open(base_url)
        self.safe_dismiss_alert()
        self.click(self.LOGIN_LINK)

    def login(self, email, password, remember_me=False):
        self.dismiss_and_detect_alert()
        self.disable_search_field()

        self.type(self.EMAIL_INPUT, email)
        self.type(self.PASSWORD_INPUT, password)
        if remember_me:
            self.click(self.REMEMBER_ME_CHECKBOX)

        # ✅ Click login button via JS
        self.click_login_button_js()

    #   alert_triggered = self.dismiss_and_detect_alert()

    #    if alert_triggered:
    #        print("Retrying login after alert...")
    #        self.disable_search_field()
    #        self.type(self.EMAIL_INPUT, email)
    #        self.type(self.PASSWORD_INPUT, password)
    #        if remember_me:
    #        self.click(self.REMEMBER_ME_CHECKBOX)
    #        self.click_login_button_js()
    #        self.dismiss_and_detect_alert()

    #   self.click(self.ACCOUNT_NAME)
    #   print("Current URL:", self.driver.current_url)
    #   return self.get_input_value((By.ID, "Email"))



    def go_to_Apparel_shoes(self):
        self.click(self.APPAREL_SHOES)
        self.click(self.BLUE_JEANS_ADD_TO_CART)
        self.get_text(self.PRODUCT_ADDED_TO_CART_TEXT)

    #def is_logged_in(self):
    #    try:
    #       return WebDriverWait(self.driver, 5).until(
    #            EC.presence_of_element_located(self.ACCOUNT_NAME)
    #        ).is_displayed()
    #    except:
    #        return False






