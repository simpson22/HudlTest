from hudl.page.base import BasePage
from hudl.page.home import HomePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def load(self):
        self.driver.get("https://www.hudl.com/login")

    def selectEmail(self):
        self.driver.find_element(By.XPATH, "//input[@data-qa-id='email-input']").click()

    def login(self, email, password):
        self.driver.find_element(
            By.XPATH, "//input[@data-qa-id='email-input']"
        ).send_keys(email)
        self.driver.find_element(
            By.XPATH, "//input[@data-qa-id='password-input']"
        ).send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@data-qa-id='login-btn']").click()
        return HomePage(self.driver)
