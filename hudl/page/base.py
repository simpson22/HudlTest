from selenium.webdriver.remote.webdriver import WebDriver


class BasePage():
    def __init__(self, driver: WebDriver) -> None:
        self.driver: WebDriver = driver

    def close(self):
        try:
            self.driver.close()
            self.driver.quit()
        except Exception as e:
            print(f"Couldn't close the web driver: {e}")
