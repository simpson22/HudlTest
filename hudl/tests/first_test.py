import os
import pytest
from selenium import webdriver
from hudl.page.login import LoginPage

email = os.environ.get("HUDL_EMAIL")
password = os.environ.get("HUDL_PASSWORD")


@pytest.fixture(scope="module")
def page():
    driver = webdriver.Chrome()
    page = LoginPage(driver)
    yield page
    page.close()


# @pytest.mark.skip
def test_connect(page):
    login_page = page
    login_page.load()
    assert login_page.driver.title == "Log In"


def test_login(page):
    login_page = page
    login_page.load()
    home_page = login_page.login(email, password)
    assert home_page.driver.title == "Home - Hudl"
