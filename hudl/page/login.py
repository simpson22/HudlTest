from hudl.page.base import BasePage
from hudl.page.home import HomePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    locators = {
        "email_input": "//input[@data-qa-id='email-input']",
        "password_input": "//input[@data-qa-id='password-input']",
        "login_button": "//button[@data-qa-id='login-btn']",
        "login_organisation_button": "//button[@data-qa-id='log-in-with-organization-btn']",
        "error_display": "//p[@data-qa-id='error-display']",
    }

    def load(self):
        self.driver.get("https://www.hudl.com/login")
        self.wait.until(lambda driver: driver.title == "Log In")
        self.email_input = self.driver.find_element(By.XPATH, self.locators["email_input"])
        self.password_input = self.driver.find_element(By.XPATH, self.locators["password_input"])
        self.login_button = self.driver.find_element(By.XPATH, self.locators["login_button"])
        self.login_organisation_button = self.driver.find_element(By.XPATH, self.locators["login_organisation_button"])

    def input_email(self, email):
        self.email_input.send_keys(email)

    def input_password(self, password):
        self.password_input.send_keys(password)

    def click_login(self):
        self.login_button.click()
        return HomePage(self.driver)

    def click_login_organisation(self):
        self.login_organisation_button.click()
        return OrgLoginPage(self.driver)

    def login(self, email, password):
        self.input_email(email)
        self.input_password(password)
        home_page = self.click_login()
        return home_page

    def is_error_displayed(self):
        self.error_display = self.driver.find_element(By.XPATH, self.locators["error_display"])
        return self.error_display.is_displayed()


class OrgLoginPage(BasePage):
    locators = {
        "email_input": "//input[@class='uni-input']",
        "login_button": "//button[@data-qa-id='log-in-with-sso']",
    }

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self.wait.until(lambda driver: driver.title == "Log In with Organization - Hudl")
            self.email_input = self.driver.find_element(By.XPATH, self.locators["email_input"])
            self.login_button = self.driver.find_element(By.XPATH, self.locators["login_button"])
        except Exception as e:
            print(f"Did not load Organisation Log In Page: {e}")

    def input_email(self, email):
        self.email_input.send_keys(email)

    def click_login(self):
        self.login_button.click()

    def fail_login(self, email):
        self.input_email(email)
        self.click_login()
        self.wait.until(
            lambda driver: driver.title != "Log In with Organization - Hudl"
        )
