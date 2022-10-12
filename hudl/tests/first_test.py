import os
import pytest
from selenium import webdriver
from hudl.page.login import LoginPage

email = os.environ.get('HUDL_EMAIL')
password = os.environ.get('HUDL_PASSWORD')


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver


# @pytest.mark.skip
def test_connect(driver):
    page = LoginPage(driver)
    page.load()
    assert page.driver.title == 'Log In'


def test_login(driver):
    page = LoginPage(driver)
    page.load()
    page.login(email, password)
    assert page.driver.title == 'Home'
