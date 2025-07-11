# utils/config.py
import os

# Base URL of the application under test
BASE_URL = "http://demowebshop.tricentis.com"

# Browser type: "chrome", "firefox", etc.
BROWSER = os.getenv("BROWSER", "chrome")

# Headless mode: True or False
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"

# Default timeout for waits
TIMEOUT = int(os.getenv("TIMEOUT", "10"))

user_credentials = {
    "user": {
        "email": "Tosca.learning@qa.test",
        "password": "Tosca1234!"
    }

}

user_details = {
    "City": "Vienna",
    "Address1": "Demo address",
    "PostalCode": "77890",
    "Phone": "73383839900"

}

card_details = {
    "CardholderName": "Doe",
    "CardNumber": "4111111111111111",
    "CardCode": "1234"



}
