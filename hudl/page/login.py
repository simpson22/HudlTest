from hudl.page.base import BasePage
from hudl.page.home import HomePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    locators = {
        "email_input": "//input[@data-qa-id='email-input']",
        "password_input":  "//input[@data-qa-id='password-input']",
        "login_button": "//button[@data-qa-id='login-btn']"
    }

    def load(self):
        self.driver.get("https://www.hudl.com/login")
        self.wait.until(lambda driver: driver.find_element(By.XPATH, self.locators["email_input"]))
        self.email_input = self.driver.find_element(By.XPATH, self.locators["email_input"])
        self.password_input = self.driver.find_element(By.XPATH, self.locators["password_input"])
        self.login_button = self.driver.find_element(By.XPATH, self.locators["login_button"])

    def input_email(self, email):
        self.email_input.send_keys(email)

    def input_password(self, password):
        self.password_input.send_keys(password)

    def click_login(self):
        self.login_button.click()

    def login(self, email, password):
        self.input_email(email)
        self.input_password(password)
        self.click_login()
        return HomePage(self.driver)

    def badLogin(self, email, password):
        self.input_email(email)
        self.input_password(password)
        self.click_login()
