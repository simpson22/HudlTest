from hudl.page.base import BasePage
from hudl.page.home import HomePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    email_input = "//input[@data-qa-id='email-input']"
    password_input = "//input[@data-qa-id='password-input']"
    login_button = "//button[@data-qa-id='login-btn']"

    def load(self):
        self.driver.get("https://www.hudl.com/login")

    def login(self, email, password):
        self.driver.find_element(By.XPATH, self.email_input).send_keys(email)
        self.driver.find_element(By.XPATH, self.password_input).send_keys(password)
        self.driver.find_element(By.XPATH, self.login_button).click()
        return HomePage(self.driver)

    def badLogin(self, email, password):
        self.driver.find_element(By.XPATH, self.email_input).send_keys(email)
        self.driver.find_element(By.XPATH, self.password_input).send_keys(password)
        self.driver.find_element(By.XPATH, self.login_button).click()
