from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_google():

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    driver.maximize_window()

    driver.get("https://www.google.com")

    print(driver.title)

    assert "Ggogle" in driver.title

    time.sleep(3)

    driver.quit()