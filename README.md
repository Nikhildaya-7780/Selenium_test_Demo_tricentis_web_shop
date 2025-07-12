# 🧪 Selenium Automation Framework – Demo Web Shop

A robust and scalable automation framework built using Python and Selenium WebDriver to test the end-to-end flow of the Tricentis Demo Web Shop.

## 🚀 Features

- Login automation with credential validation
- Product selection and cart interaction
- Checkout flow with billing, shipping, and payment steps
- JavaScript-based form submission and alert handling
- Dynamic dropdown selection and hover-based tooltip extraction
- Page Object Model (POM) architecture with reusable BasePage methods

## 📦 Tech Stack

- Python 3.x
- Selenium WebDriver
- PyTest
- Page Object Model (POM)
- JavaScript injection for browser interactions

## 🛠 Installation

```bash
git clone https://github.com/your-username/selenium-project.git
cd selenium-project
pip install -r requirements.txt

🧪 Running Tests

pytest tests/login_test.py::test_web_page_end_to_end


Project structure:

SeleniumProject/
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── product_page.py
│   ├── checkout_page.py
│   ├── billing_address.py
│   └── confirm_screen.py
├── tests/
│   └── login_test.py
├── README.md
└── requirements.txt
