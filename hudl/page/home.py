from hudl.page.base import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait.until(lambda driver: driver.title == 'Home - Hudl')
        self.wait.until(lambda driver: driver.find_element(By.XPATH, "//div[@class='hui-globalusermenu']"))
        print('Successfully logged in')

    def load(self):
        self.driver.get("https://www.hudl.com/home")
