from pageObjects.loginPage import LoginPage

def test_login(setup):

    driver = setup

    login_page = LoginPage(driver)

    login_page.login("test@test.com", "Password123")

    assert "Let's Shop" in driver.page_source