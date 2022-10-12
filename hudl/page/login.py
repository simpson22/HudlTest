from hudl.page.base import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get("https://www.hudl.com/login")

    def selectEmail(self):
        self.driver.find_element(By.XPATH, "//input[@data-qa-id='email-input']").click()
