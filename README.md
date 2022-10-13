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
python -m venv .
```
### Drivers

The Chrome Webdriver has been chosen for initial testing.

Get Chrome if not already installed from: https://www.google.com/chrome/

Then please ensure you have downloaded chromedriver from: https://chromedriver.chromium.org/downloads, selecting a version that matches the installed Chrome Browser.

And then ensure the ```PATH``` environment variable has been set to the filepath of the driver.

e.g. On MacOS:

```
export PATH=$PATH:/path/to/driver
```

You may also need to bypass MacOS Gatekeeper in order for the Chromedriver to launch.

```
sudo xattr -r -d com.apple.quarantine /path/to/driver/filename
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

Set ```HUDL_EMAIL``` and ```HUDL_PASSWORD``` environment variables with valid login credentials:

```
export HUDL_EMAIL=*****************
export HUDL_PASSWORD=*****************
```

Then run the tests with the optional parameters to improve verbosity and summary report:

From the HudlTest project directory

```
python -m pytest -v -rA
```

## TODO:

Functional

* Remember Me Tests (Looks a bit broken?)
* Maintain a Login state with ChromeOptions
* Need Help?
* Login from Landing Page
* Email Hint on Org Login Page

Cross-Functional

* Different Browsers
* Adaptability (Window Resizing)
* Security
* Responsiveness
* Accessibility
* Visual Regression

Quality of Life

* Reporting
* Test Artifacts
* Fluent Interface
* Page Factory
* Abstract Classes
* BDD
