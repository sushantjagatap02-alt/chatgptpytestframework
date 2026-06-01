from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    email = (By.ID, "userEmail")
    password = (By.ID, "userPassword")
    login_button = (By.ID, "login")

    def login(self, username, pwd):
        """Perform login with username and password"""
        self.driver.find_element(*self.email).send_keys(username)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.login_button).click()
        time.sleep(2)

    def get_error_message(self):
        """Get error message if login fails"""
        try:
            # Try different possible error selectors
            error_selectors = [
                (By.XPATH, "//div[contains(@class, 'alert')]"),
                (By.CSS_SELECTOR, ".alertError"),
                (By.XPATH, "//span[contains(text(), 'Incorrect')]"),
            ]

            for selector in error_selectors:
                try:
                    wait = WebDriverWait(self.driver, 3)
                    error = wait.until(EC.presence_of_element_located(selector))
                    return error.text
                except:
                    continue
            return None
        except:
            return None

    def is_email_field_visible(self):
        """Check if email field is visible"""
        try:
            return self.driver.find_element(*self.email).is_displayed()
        except:
            return False

    def is_password_field_visible(self):
        """Check if password field is visible"""
        try:
            return self.driver.find_element(*self.password).is_displayed()
        except:
            return False

    def is_login_button_visible(self):
        """Check if login button is visible"""
        try:
            return self.driver.find_element(*self.login_button).is_displayed()
        except:
            return False


    def clear_email(self):
        """Clear email field"""
        self.driver.find_element(*self.email).clear()

    def clear_password(self):
        """Clear password field"""
        self.driver.find_element(*self.password).clear()