TODO:
Cleanup Readme
Comment Code
Finish Test Cases
Test on MacOS
Cleanup the DSL, Improve Readability
Improve Reporting?

# HudlTest

A demonstration test framework which tests the login functionality of https://www.hudl.com/

## Prerequisites

### Python 3.10.7

This framework has been built and tested with Python 3.10.7

It is likely compatible with more version of Python, but these have not been tested.

### venv

You may want to set up a virtual environment.

From the current directory 
```
python -m venv
```
### Drivers

The Chrome driver has been chosen for initial testing, please ensure you have downloaded chromedriver from: https://chromedriver.chromium.org/downloads

And then ensure the ```PATH``` environment variable has been set to the filepath of the driver.

e.g. On MacOS:

```
export PATH=$PATH:/path/to/driver
```



### pip-tools

pip-tools has been used to help manage packages in the environment. requirements.in has been used to specify the direct dependencies of the HudlTest framework.

The requirements.txt is then compiled from the requirements.in

*example only, do not need to run:*
```
pip install pip-tools
pip-compile requirements.in
```

So to install all dependencies required:

*Do run this before executing tests:*
```
pip install -r requirements.txt
```

## Executing the tests

Set ```HUDL_EMAIL``` and ```HUDL_PASSWORD``` environment variables with valid login credentials.

```
python -m pytest
```

## NOTES:

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

