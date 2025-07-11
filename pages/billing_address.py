import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from utils import config
from pages.base_page import BasePage



class BillingAddress(BasePage):

    BILLING_ADDRESS = (By.ID, "billing-address-select")
    NEW_ADDRESS = (By.XPATH, "//select[@id='billing-address-select']")
    SELECT_COUNTRY = (By.XPATH, "//select[@id='BillingNewAddress_CountryId']")
    ENTER_CITY = (By.ID, "BillingNewAddress_City")
    ENTER_ADDRESS = (By.ID, "BillingNewAddress_Address1")
    ENTER_POSTAL_CODE = (By.ID, "BillingNewAddress_ZipPostalCode")
    ENTER_PHONE = (By.ID, "BillingNewAddress_PhoneNumber")
    CLICK_CONTINUE = (By.XPATH, '//input[@onclick="Billing.save()"]')
    CONTINUE_SHIPPING = (By.XPATH, "//input[@onclick='Shipping.save()']")
    SHIPPING_METHOD = (By.XPATH, "//input[@class='button-1 shipping-method-next-step-button']")
    PAYMENT_METHOD = (By.ID, "paymentmethod_2")
    CONTINUE_FROM_PAYMENT = (By.XPATH, "//input[@class='button-1 payment-method-next-step-button']")
    CARD_HOLDER_NAME = (By.XPATH, "//input[@id='CardholderName']")
    CARD_NUMBER = (By.XPATH, "//input[@id='CardNumber']")
    CARD_CODE = (By.XPATH, "//input[@id='CardCode']")
    PAYMENT_CONFIRM = (By.XPATH, "//input[@class='button-1 payment-info-next-step-button']")
    TOTAL_VALUE = (By.XPATH, "//input[@value='Confirm']")
    TEXT = (By.XPATH, "//strong[normalize-space()='Your order has been successfully processed!']")
    FINAL_CONTINUE = (By.XPATH, "//input[@value='Continue']")
    CART_TEXT = (By.CLASS_NAME, "cart-label")
    TOOL_TIP_TEXT = (By.XPATH, "//div[@class='count']")




    def billing_address(self):
        self.select_dropdown_and_wait(
            dropdown_locator=self.BILLING_ADDRESS,
            value="",
            wait_for_locator=self.NEW_ADDRESS
        )
        return self


    def select_country(self, country):
        self.select_dropdown_by_text(self.SELECT_COUNTRY, country )
        return self

    def enter_details_and_continue (self, user_details, card_details):
        self.type(self.ENTER_CITY, user_details['City'])
        self.type(self.ENTER_ADDRESS, user_details['Address1'])
        self.type(self.ENTER_POSTAL_CODE, user_details['PostalCode'])
        self.type(self.ENTER_PHONE, user_details['Phone'])
        self.click(self.CLICK_CONTINUE)
        self.click(self.CONTINUE_SHIPPING)
        self.click(self.SHIPPING_METHOD)
        self.click(self.PAYMENT_METHOD)
        self.click(self.CONTINUE_FROM_PAYMENT)
        self.type(self.CARD_HOLDER_NAME, card_details['CardholderName'])
        self.type(self.CARD_NUMBER, card_details['CardNumber'])
        self.type(self.CARD_CODE, card_details['CardCode'])
        self.click(self.PAYMENT_CONFIRM)
        self.click(self.TOTAL_VALUE)
    #    self.get_text(self.TEXT)
        time.sleep(5)
       # self.click(self.FINAL_CONTINUE)

      #  self.hover_and_get_text(self.CART_TEXT, self.TOOL_TIP_TEXT)
        return self












