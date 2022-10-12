from hudl.page.base import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    homepage_banner = "//div[@class='hui-globalusermenu']"

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self.wait.until(lambda driver: driver.title == "Home - Hudl")
            self.wait.until(lambda driver: driver.find_element(By.XPATH, self.homepage_banner))
            print("Successfully logged in")
        except Exception as e:
            print("Login not successful")

    def load(self):
        self.driver.get("https://www.hudl.com/home")
