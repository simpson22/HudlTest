from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from selenium.common.exceptions import (
    ElementNotVisibleException,
    ElementNotSelectableException,
)


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(
            driver,
            timeout=5,
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

    # Too flakey
    def has_loaded(self, driver):
        print("Checking if {} page is loaded.".format(driver.current_url))
        page_state = driver.execute_script('return document.readyState;')
        return page_state == 'complete'
