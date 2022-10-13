from hudl.page.base import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    locators = {
        "user_dropdown": "//div[@class='hui-globaluseritem__display-name']",
        "logged_in_email": "//div[@class='hui-globaluseritem__email']",
    }

    def __init__(self, driver, login_email):
        super().__init__(driver)
        try:
            self.login_email = login_email
            self.wait.until(lambda driver: driver.title == "Home - Hudl")
            self.driver.find_element(By.XPATH, self.locators["user_dropdown"]).click()
            self.wait.until(self.isLoggedInAs)
            self.logged_in_email = self.driver.find_element(By.XPATH, self.locators["logged_in_email"])
            if login_email == self.logged_in_email:
                print('Successfully logged in')
            else:
                print('Logged in as someone else!')
        except Exception as e:
            print(f"Login not successful: {e}")

    def load(self):
        self.driver.get("https://www.hudl.com/home")

    def isLoggedInAs(self, driver):
        email = self.login_email
        return driver.find_element(By.XPATH, self.locators["logged_in_email"]).text == email
