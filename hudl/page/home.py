from hudl.page.base import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    locators = {
        "user_dropdown": "//div[@class='hui-globaluseritem__display-name']",
        "logged_in_email": "//div[@class='hui-globaluseritem__email']",
    }

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self.wait.until(lambda driver: driver.title == "Home - Hudl")
        except Exception as e:
            print(f"Did not load Homepage: {e}")

    def load(self):
        self.driver.get("https://www.hudl.com/home")

    def verifyLoginEmail(self, login_email):
        try:
            self.login_email = login_email
            self.driver.find_element(By.XPATH, self.locators["user_dropdown"]).click()
            self.wait.until(self._checkLoginEmail)
            self.logged_in_email = self.driver.find_element(By.XPATH, self.locators["logged_in_email"]).text
        except Exception as e:
            print(f"Login not successful: {e}")

    def _checkLoginEmail(self, driver):
        email = self.login_email
        return driver.find_element(By.XPATH, self.locators["logged_in_email"]).text == email
