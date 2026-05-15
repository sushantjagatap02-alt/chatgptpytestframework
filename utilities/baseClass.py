class BaseClass:

    def take_screenshot(self, driver, name):

        driver.save_screenshot(f"screenshots/{name}.png")