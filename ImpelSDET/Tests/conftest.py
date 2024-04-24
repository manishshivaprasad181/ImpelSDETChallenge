import os
import pytest
from selenium import webdriver
from Tests.helper_functions import login, navigate_to_add_customer_page


# setup and teardown fixture
@pytest.fixture(scope="module")
def setup_and_teardown():
    """
        Fixture to set up and teardown the WebDriver instance for each test module.

        Returns:
            WebDriver: WebDriver instance for testing.
        """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://test-engineer-assignment-manager.testenv.impel.io/login?next=%2F")
    yield driver
    driver.quit()


# Fixture to set up test environment for adding customer and add customer form validation
@pytest.fixture(scope="module")
def add_customer_page_setup(setup_and_teardown):
    """
       Fixture to set up test environment for adding a customer and validating the add customer form.

       Args:
           setup_and_teardown: setup_and_teardown fixture.

       Returns:
           WebDriver: WebDriver instance for testing.
       """
    driver = setup_and_teardown
    login(driver, os.environ.get('VALID_EMAIL'), os.environ.get('VALID_PASSWORD'))
    navigate_to_add_customer_page(driver)
    yield driver
    driver.quit()
