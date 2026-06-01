import pytest
from pageObjects.loginPage import LoginPage
from utilities.baseClass import BaseClass


class TestUIElements(BaseClass):
    """UI/Element visibility tests"""

    @pytest.mark.smoke
    def test_email_field_exists_and_visible(self, setup):
        """Verify email input field exists and is visible"""
        driver = setup
        login_page = LoginPage(driver)

        assert login_page.is_email_field_visible(), "Email field not visible on login page"
        self.take_screenshot(driver, "email_field_visible")
        print("✓ Email field is visible")

    @pytest.mark.smoke
    def test_password_field_exists_and_visible(self, setup):
        """Verify password input field exists and is visible"""
        driver = setup
        login_page = LoginPage(driver)

        assert login_page.is_password_field_visible(), "Password field not visible on login page"
        self.take_screenshot(driver, "password_field_visible")
        print("✓ Password field is visible")

    @pytest.mark.smoke
    def test_login_button_exists_and_visible(self, setup):
        """Verify login button exists and is visible"""
        driver = setup
        login_page = LoginPage(driver)

        assert login_page.is_login_button_visible(), "Login button not visible on login page"
        self.take_screenshot(driver, "login_button_visible")
        print("✓ Login button is visible")

    def test_all_login_elements_present(self, setup):
        """Verify all required login elements are present"""
        driver = setup
        login_page = LoginPage(driver)

        assert login_page.is_email_field_visible()
        assert login_page.is_password_field_visible()
        assert login_page.is_login_button_visible()

        self.take_screenshot(driver, "all_login_elements")
        print("✓ All login elements are present and visible")