from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains



class BasePage:
    def __init__(self, driver):
        self.locator = None
        self.driver = driver
        self.timeout = 10

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator):
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        ).click()


    def type(self, locator, text):
        element = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        ).text

    def is_visible(self, locator):
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False

    def wait_for_title(self, title_fragment):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.title_contains(title_fragment)
        )

    def wait_for_url_contains(self, url_fragment):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.url_contains(url_fragment)
        )

    def scroll_into_view(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def safe_dismiss_alert(self):
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            print(f"Alert detected: {alert.text}")
            alert.accept()
        except:
            print("No alert appeared.")

    def wait_for_element_to_disappear(self, locator):
        WebDriverWait(self.driver, self.timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def dismiss_tricentis_popup(self, locator):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(locator)
            ).click()
            print("Tricentis popup dismissed.")
        except:
            print("No Tricentis popup appeared.")

    def blur_active_element(self):
            try:
                self.driver.execute_script("document.activeElement.blur();")
            except:
                pass

    def capture_dom_snapshot(self, name="debug"):
            self.driver.save_screenshot(f"screenshots/{name}.png")
            with open(f"screenshots/{name}.html", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)

    def dismiss_popup_if_present(self, locator):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(locator)
            ).click()
            print("Popup dismissed.")
        except:
            print("No popup appeared.")

    def blur_search_field(self):
        try:
            search_input = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "small-searchterms"))
            )
            self.driver.execute_script("arguments[0].blur();", search_input)
            print("Search field blurred.")
        except Exception as e:
            print(f"Could not blur search field: {e}")

    def get_input_value(self, locator):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element.get_attribute("value")
        except Exception as e:
            print(f"Could not get input value: {e}")
            return False

    def disable_search_field(self):
        try:
            self.driver.execute_script("""
                const search = document.getElementById('small-searchterms');
                if (search) search.setAttribute('disabled', 'true');
            """)
            print("Search field disabled.")
        except Exception as e:
            print(f"Could not disable search field: {e}")

    def submit_login_form_js(self):
        try:
            self.driver.execute_script("""
                document.querySelector('form[action="/login"]').submit();
            """)
            print("Login form submitted via JavaScript.")
        except Exception as e:
            print(f"Failed to submit login form via JS: {e}")

    def dismiss_and_detect_alert(self):
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            print(f"Alert detected: {alert.text}")
            alert.accept()
            return True
        except:
            print("No alert appeared.")
            return False

    def submit_login_form_directly(self):
        try:
            self.driver.execute_script("""
                const form = document.querySelector('form[action="/login"]');
                if (form) form.submit();
            """)
            print("Login form submitted via JS.")
        except Exception as e:
            print(f"Failed to submit login form via JS: {e}")

    def click_login_button_js(self):
        try:
            self.driver.execute_script("""
                const btn = document.querySelector('input.button-1.login-button');
                if (btn) btn.click();
            """)
            print("Login button clicked via JS.")
        except Exception as e:
            print(f"Failed to click login button via JS: {e}")

    def select_dropdown_and_wait(self, dropdown_locator, value, wait_for_locator):
        try:
            dropdown = Select(self.driver.find_element(*dropdown_locator))
            dropdown.select_by_value(value)
            print(f"Selected value '{value}' from dropdown.")

            print(f"Waiting for element: {wait_for_locator}")
            WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(wait_for_locator)
            )
            print(f"Element {wait_for_locator} is now present.")
        except Exception as e:
            print(f"Dropdown selection or wait failed: {e}")
            print("Page source snapshot:")
            print(self.driver.page_source)
            raise

    def select_dropdown_by_text(self, locator, visible_text):

        element = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(locator))
        Select(element).select_by_visible_text(visible_text)

    def get_confirmation(self, locator, expected_text=None):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
            text = element.text
            if expected_text and expected_text not in text:
                raise ValueError(f"Expected '{expected_text}', but got '{text}'")
            return text
        except TimeoutException:
            print(f"Timeout: Element {locator} not visible after {self.timeout} seconds.")
            return None

    def hover_and_get_text(self, target_locator, text_locator=None, timeout=10):

        element_to_hover = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(target_locator)
        )
        ActionChains(self.driver).move_to_element(element_to_hover).pause(1).perform()

        if text_locator:
            tooltip_element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(text_locator)
            )
            return tooltip_element.text
        else:
            # fallback to native title attribute
            return element_to_hover.get_attribute("title")

    def wait_for_confirmation_text(self, locator, expected_text=None):
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
            text = self.driver.find_element(*locator).text
            if expected_text and expected_text not in text:
                print(f"[WARN] Expected '{expected_text}', but got '{text}'")
            return text
        except TimeoutException:
            print(f"[ERROR] Confirmation element not found: {locator}")
            print(f"[DEBUG] Current URL: {self.driver.current_url}")
            print(f"[DEBUG] Page Snapshot:\n{self.driver.page_source[:1000]}...")
            return None

    

    def wait_for_confirmation_page(self):
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.url_contains(self.CONFIRM_URL_FRAGMENT)
            )
            return True
        except TimeoutException:
            print("[ERROR] Confirmation page URL not loaded.")
            print("[DEBUG] Current URL:", self.driver.current_url)
            return False

    def get_confirmation_text(self):
        try:
            confirmation_element = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(self.locator)
            )
            return confirmation_element.text
        except TimeoutException:
            print("[ERROR] Confirmation message not visible.")
            self.driver.save_screenshot("confirmation_fail.png")
            print("[DEBUG] Snapshot saved.")
            return None
