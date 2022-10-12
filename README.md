README

Prerequisites

Python 3.10.7

venv

pip-tools

drivers in PATH

python -m pytest

NOTES:

Different Browsers?
Cross Functional Requirements?
Visual Regression?
BDD it?

lint
venv
requirements
readme
reporting
artifacts - screenshots?

Exploratiory Test
Selenium Test Practices: https://www.selenium.dev/documentation/test_practices/
	Fluent Interface
	Page object Model
	
	
Test negatives and edge cases too
Add a Readme and ensure execution on MacOS


Journeys

https://www.hudl.com/en_gb/ > Log in

https://www.hudl.com/login > Log in

	Happy Path

	Bad Password
		No Password
		Mistyped
		All Caps
		All lowercase
	Bad Email
		No Email
		Mistyped
		Case Sensitive? (Shouldn't be)

	Login Retry
		Can't submit twice without change
		Can submit on change and Succeed

	Log In with an Organization?
		Try non org login and Fail
		Fail Redirect + Log in
		Navigate Straight back with Link
		Email Hint?

	Remember Me True/False (Needs to keep state) (Seems to be a bug always remembers)


	Need help? (From wrong password, and from page itself)
	Sign Up?
	Navigate back arrow?
	Changing Password?


https://www.hudl.com/home


Visual Regression?
CFRs?
	Reponsiveness
	Adaptability (Window size)
	Tab selecting
	Verify Text?
	Security (HTTP / HTTPS)

