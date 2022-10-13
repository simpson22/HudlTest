import os
import pytest
from selenium import webdriver
from hudl.page.login import LoginPage

valid_email = os.environ.get("HUDL_EMAIL")
valid_password = os.environ.get("HUDL_PASSWORD")


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
def test_valid_login(page: LoginPage):
    home_page = page.login(valid_email, valid_password)
    assert page.driver.title == "Home - Hudl"
    home_page.verify_login_email(valid_email)
    assert home_page.logged_in_email == valid_email


@pytest.mark.parametrize(
    "email,password",
    [
        (valid_email, ""),
        ("", valid_password),
        (valid_email, valid_password.upper()),
        (valid_email, valid_password.lower()),
        pytest.param(valid_email.upper(), valid_password, marks=pytest.mark.xfail),
    ],
)
# @pytest.mark.skip
def test_invalid_login_combinations(page: LoginPage, email, password):
    page.login(email, password)
    assert page.driver.title != "Home - Hudl"
    assert page.is_error_displayed()
    assert (
        page.error_display.text
        == "We didn't recognize that email and/or password.Need help?"
    )


# @pytest.mark.skip
def test_retry_login_journey(page: LoginPage):
    page.login(valid_email, "bad_password")
    assert not page.login_button.is_enabled()
    page.password_input.clear()
    page.input_password(valid_password)
    assert page.login_button.is_enabled()
    home_page = page.click_login()
    home_page.verify_login_email(valid_email)
    assert page.driver.title == "Home - Hudl"
    assert home_page.logged_in_email == valid_email


# @pytest.mark.skip
def test_cannot_login_as_org(page: LoginPage):
    org_page = page.click_login_organisation()
    org_page.fail_login(valid_email)
    assert page.driver.title == "Log In"
    assert page.is_error_displayed()
    assert (
        page.error_display.text
        == "This account can't log in with an organization yet. Please log in using your email and password."
    )
