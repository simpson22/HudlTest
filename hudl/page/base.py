from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from selenium.common.exceptions import (
    ElementNotVisibleException,
    ElementNotSelectableException,
)


class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(
            driver,
            timeout=3,
            poll_frequency=1,
            ignored_exceptions=[
                ElementNotVisibleException,
                ElementNotSelectableException,
            ],
        )

    def close(self):
        try:
            self.driver.quit()
        except Exception as e:
            print(f"Couldn't close the web driver: {e}")
