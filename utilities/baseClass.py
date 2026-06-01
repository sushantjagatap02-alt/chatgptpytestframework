from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseClass:

    def take_screenshot(self, driver, name):
        """Take and save screenshot"""
        driver.save_screenshot(f"screenshots/{name}.png")
        print(f"Screenshot saved: screenshots/{name}.png")

    def wait_for_element(self, driver, locator, timeout=10):
        """Wait for element to be present"""
        wait = WebDriverWait(driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))

    def wait_for_element_visible(self, driver, locator, timeout=10):
        """Wait for element to be visible"""
        wait = WebDriverWait(driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, driver, locator, timeout=10):
        """Wait for element to be clickable"""
        wait = WebDriverWait(driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))