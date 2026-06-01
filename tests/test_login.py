import pytest
import time
from pageObjects.loginPage import LoginPage
from utilities.baseClass import BaseClass
from testData.login_data import VALID_CREDENTIALS, INVALID_EMAILS, INVALID_PASSWORDS


class TestLoginFunctionality(BaseClass):
    """Comprehensive Login Test Suite"""

    @pytest.mark.smoke
    def test_login_with_valid_credentials(self, setup):
        """Test login with valid credentials"""
        driver = setup
        login_page = LoginPage(driver)

        # Login
        login_page.login(VALID_CREDENTIALS["email"], VALID_CREDENTIALS["password"])

        # Verify successful login
        assert "Let's Shop" in driver.page_source, "Failed to login - 'Let's Shop' text not found"
        self.take_screenshot(driver, "login_success")
        print("✓ Test passed: Valid login successful")

    @pytest.mark.regression
    def test_login_page_ui_elements(self, setup):
        """Test that all login UI elements are visible"""
        driver = setup
        login_page = LoginPage(driver)

        # Check all elements are visible
        assert login_page.is_email_field_visible(), "Email field not visible"
        assert login_page.is_password_field_visible(), "Password field not visible"
        assert login_page.is_login_button_visible(), "Login button not visible"

        self.take_screenshot(driver, "login_ui_elements_visible")
        print("✓ Test passed: All UI elements visible")

    @pytest.mark.regression
    @pytest.mark.parametrize("credentials", INVALID_EMAILS)
    def test_login_with_invalid_email(self, setup, credentials):
        """Test login with invalid email formats"""
        driver = setup
        login_page = LoginPage(driver)

        # Clear and login
        login_page.clear_email()
        login_page.clear_password()
        login_page.login(credentials["email"], credentials["password"])

        # Take screenshot
        self.take_screenshot(driver, f"invalid_email_{credentials['description'].replace(' ', '_')}")
        print(f"✓ Test passed: {credentials['description']}")

    @pytest.mark.regression
    @pytest.mark.parametrize("credentials", INVALID_PASSWORDS)
    def test_login_with_invalid_password(self, setup, credentials):
        """Test login with invalid passwords"""
        driver = setup
        login_page = LoginPage(driver)

        # Clear and login
        login_page.clear_email()
        login_page.clear_password()
        login_page.login(credentials["email"], credentials["password"])

        # Take screenshot
        self.take_screenshot(driver, f"invalid_password_{credentials['description'].replace(' ', '_')}")
        print(f"✓ Test passed: {credentials['description']}")

    def test_login_empty_email(self, setup):
        """Test login with empty email field"""
        driver = setup
        login_page = LoginPage(driver)

        login_page.login("", "Password123")
        time.sleep(1)

        self.take_screenshot(driver, "empty_email_error")
        print("✓ Test passed: Empty email test completed")

    def test_login_empty_password(self, setup):
        """Test login with empty password field"""
        driver = setup
        login_page = LoginPage(driver)

        login_page.login("test@test.com", "")
        time.sleep(1)

        self.take_screenshot(driver, "empty_password_error")
        print("✓ Test passed: Empty password test completed")

    def test_login_both_empty(self, setup):
        """Test login with both email and password empty"""
        driver = setup
        login_page = LoginPage(driver)

        login_page.login("", "")
        time.sleep(1)

        self.take_screenshot(driver, "both_fields_empty")
        print("✓ Test passed: Both fields empty test completed")

    def test_login_invalid_credentials(self, setup):
        """Test login with invalid credentials"""
        driver = setup
        login_page = LoginPage(driver)

        login_page.login("invalid@test.com", "WrongPassword")
        time.sleep(1)

        self.take_screenshot(driver, "invalid_credentials")
        print("✓ Test passed: Invalid credentials test completed")