import pytest
from selenium import webdriver
from hudl.page.login import LoginPage


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver


# @pytest.mark.skip
def test_connect(driver):
    page = LoginPage(driver)
    page.load()
    assert page.driver.title == 'Log In'
