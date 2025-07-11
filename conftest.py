# conftest.py
import pytest
from utils import config
from utils.browser_factory import create_browser

@pytest.fixture(scope="session")
def driver():
    browser = create_browser(browser_name=config.BROWSER, headless=config.HEADLESS)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()

@pytest.fixture(scope="session")
def base_url():
    return config.BASE_URL


