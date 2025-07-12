import time

from pages.billing_address import BillingAddress
from pages.login_page import LoginPage
from pages.product import ProductPage
from utils.config import user_credentials, user_details, card_details
from pages.checkout_page import CheckoutPage
from pages.confirm_screen import OrderConfirmationPage

def test_web_page_end_to_end(driver, base_url):
    login_page = LoginPage(driver)
    login_page.go_to_login_page(base_url)

    creds = user_credentials["user"]
    account_text =login_page.login(email=creds["email"], password=creds["password"], remember_me=True)
#    actual_email = login_page.is_logged_in()
#    assert actual_email == creds["email"]
#    assert "tosca.learning@qa.test" in account_text
    product_page = ProductPage(driver)
    message = product_page.go_to_apparel_and_add_jeans()
    assert "The product has been added to your" in message
    checkout = CheckoutPage(driver)
    checkout = checkout.checkout_process()
    billing_address = BillingAddress(driver)
    billing_address = billing_address.billing_address()
    billing_process = BillingAddress(driver)
    billing_process = billing_process.select_country("Austria")
    billing_process = billing_process.enter_details_and_continue(user_details, card_details)
    confirmation_page = OrderConfirmationPage(driver)
    confirmation_text = confirmation_page.get_confirmation_text()
    time.sleep(10)









