# utils/browser_factory.py
from selenium import webdriver

def create_browser(browser_name="chrome", headless=True):
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--start-maximized")
        return webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        return webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")