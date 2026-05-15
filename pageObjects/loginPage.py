from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    email = (By.ID, "userEmail")
    password = (By.ID, "userPassword")
    login_button = (By.ID, "login")

    def login(self, username, pwd):

        self.driver.find_element(*self.email).send_keys(username)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.login_button).click()