import os
import pytest
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Tests.helper_functions import login, validate_successful_login

fake = Faker()


# Function to test the Login page with invalid credentials and checking for appropriate message
@pytest.mark.parametrize("email, password", [
    (fake.email(), fake.password()),

])
def test_login_with_invalid_credentials(setup_and_teardown, email, password):
    """
        Test the Login page with invalid credentials and check for appropriate message.

        Args:
            setup_and_teardown: Fixture for setting up and tearing down the WebDriver.
            email (str): Invalid email address.
            password (str): Invalid password.

        Returns:
            None
        """
    driver = setup_and_teardown
    login(driver, email, password)
    invalid_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//li[text()='Invalid username or password']")))
    assert invalid_message.text == "Invalid username or password"


# Function to test the Login page by leaving email and password field empty and checking for validation message
@pytest.mark.parametrize("email, password", [
    ("", fake.password()),
    (fake.email(), ""),
    ("", "")
])
def test_login_with_empty_credentials(setup_and_teardown, email, password):
    """
        Test the Login page by leaving email and password field empty and check for validation message.

        Args:
            setup_and_teardown: Fixture for setting up and tearing down the WebDriver.
            email (str): Empty string or an email.
            password (str): Empty string or password.

        Returns:
            None
        """
    driver = setup_and_teardown
    login(driver, email, password)
    assert (driver.find_element(By.ID, "email").get_attribute("validationMessage") == "Please fill out this field." or
            driver.find_element(By.ID, "password").get_attribute("validationMessage") == "Please fill out this field.")


# Function to test the Login page with valid credentials and validating the login attempt
@pytest.mark.parametrize("email, password",
                         [(os.environ.get('VALID_EMAIL'), os.environ.get('VALID_PASSWORD'))])
def test_login_with_valid_credentials(setup_and_teardown, email, password):
    """
        Test the Login page with valid credentials and validate the login attempt.

        Args:
            setup_and_teardown: Fixture for setting up and tearing down the WebDriver.
            email (str): Valid email address.
            password (str): Valid password.

        Returns:
            None
        """
    driver = setup_and_teardown
    result = validate_successful_login(driver, email, password)
    assert result == 1
