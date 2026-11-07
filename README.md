# Sprint 9: Web Automation Testing for Urban Routes

**QA Engineer Project — TripleTen**

## Description

This project implements automated user interface tests for Urban Routes using Python, Selenium WebDriver, and pytest.

The goal is to verify the main functionalities of the taxi booking process, from route configuration to the display of driver information.

The tests are organized into independent scenarios and use the Page Object Model (POM) pattern to separate interactions with the interface from the test cases.

## Objectives

- Automate functional scenarios for taxi booking.
- Verify the data entered by the user.
- Validate the fare selection, phone number, payment method, and trip options.
- Test the car search modal and driver information.
- Improve the maintainability and reliability of the automated tests.


## Technologies

- **Python:** programming language.
- **Selenium WebDriver:** automation of browser interactions.
- **pytest:** test execution and organization.
- **Chrome:** browser used to run the test scenarios.

## File Structure

- `main.py`: contains the nine test scenarios and browser configuration.
- `pages.py`: contains the `UrbanRoutesPage` class, locators, and interaction methods.
- `data.py`: centralizes the URL and test data.
- `helpers.py`: contains the function provided by TripleTen to retrieve the phone verification code.
- `README.md`: project documentation.
- `.gitignore`: excludes temporary files and local settings.

## Test Scenarios

1. Configuring the origin and destination addresses.
2. Selecting and validating the Comfort fare.
3. Registering and confirming the phone number.
4. Adding a payment method.
5. Entering and validating the message for the driver.
6. Selecting a blanket and tissues.
7. Selecting two ice creams.
8. Displaying the car search modal.
9. Verifying the driver’s information.

## Automation Strategies

- Element locators using ID, XPath, CSS selector, and class name.
- Explicit waits for dynamic elements.
- Validations using assertions.
- Independent setup of test scenarios.
- Closing the browser after each test.

## Installation

It is recommended to use a Python virtual environment.

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Before running the tests, update `urban_routes_url` in `data.py` with the active URL provided by TripleTen.

Also verify that Chrome, Selenium, and the browser driver are compatible with the runtime environment.

## Running the Tests

Run all scenarios:

```bash
pytest main.py -v
```

Run a specific scenario:

```bash
pytest main.py::TestUrbanRoutes::test_set_route -v
```

## Expected Result

pytest displays the individual results for each scenario, allowing you to identify which tests passed and which need review.

The actual result must be confirmed by running the suite against the live Urban Routes server.

## Author

Camilo Tiuzo
Quality Assurance Engineer


