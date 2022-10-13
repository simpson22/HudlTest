import os
import pytest
from selenium import webdriver
from hudl.page.login import LoginPage

email = os.environ.get("HUDL_EMAIL")
password = os.environ.get("HUDL_PASSWORD")


@pytest.fixture(
    # scope="module"
    # Enable or disable sharing the driver instance.
    # Better to not share state unless making some local changes.
)
def page():
    driver = webdriver.Chrome()
    page = LoginPage(driver)
    page.load()
    yield page
    page.close()


# @pytest.mark.skip
def test_connect(page):
    assert page.driver.title == "Log In"


# @pytest.mark.skip
def test_login(page):
    home_page = page.login(email, password)
    assert home_page.driver.title == "Home - Hudl"


@pytest.mark.parametrize(
    "email,password",
    [
        (email, ""),
        ("", password),
        (email, password.upper()),
        (email, password.lower()),
        pytest.param(email.upper(), password, marks=pytest.mark.xfail),
    ],
)
# @pytest.mark.skip
def test_bad_login_combinations(page, email, password):
    page.login(email, password)
    assert page.driver.title != "Home - Hudl"


# @pytest.mark.skip
def test_retry_login_journey(page):
    page.login(email, 'bad_password')
    assert not page.login_button.is_enabled()
    page.password_input.clear()
    page.input_password(password)
    assert page.login_button.is_enabled()
    page.click_login()
    assert page.driver.title == "Home - Hudl"
