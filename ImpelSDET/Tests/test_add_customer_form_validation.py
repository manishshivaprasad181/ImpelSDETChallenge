import pytest
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Tests.helper_functions import fill_out_customer_form, click_save_customer_button, validate_validation_message

fake = Faker()


# Function to test the add customer page by leaving required fields empty or having spaces and checking for
# validation messages
@pytest.mark.parametrize("name, s3_folder",
                         [("", ""),
                          (fake.company(), ""),
                          ("", fake.name()),
                          (fake.company(), fake.name())])
def test_empty_inputs_validation(add_customer_page_setup, name, s3_folder):
    """
    Test the add customer page by leaving required fields empty or having spaces and checking for validation messages.

        Args: add_customer_page_setup: Fixture to set up test environment for adding a customer and validating the
        add customer form. name (str): Name of the customer. s3_folder (str): S3 folder name.

        Returns:
            None
        """
    driver = add_customer_page_setup
    fill_out_customer_form(driver, name, s3_folder)
    click_save_customer_button(driver)
    if name == "":
        validate_validation_message(driver, "Name is required.")
    if s3_folder == "":
        validate_validation_message(driver, "S3 folder is required.")
    if ' ' in s3_folder:
        validate_validation_message(driver, "S3 folder cannot have spaces")


# Function to test the add customer page by entering required details which already existed in the database
# and checking for validation messages
@pytest.mark.parametrize("name, s3_folder",
                         [("ABC Hyundai", "abchyundai")])
def test_customer_already_exists(add_customer_page_setup, name, s3_folder):
    """
        Test the add customer page by entering required details which already existed in the database and checking for validation messages.

        Args:
            add_customer_page_setup: Fixture to set up test environment for adding a customer and validating the add customer form.
            name (str): Name of the customer.
            s3_folder (str): S3 folder name.

        Returns:
            None
        """
    driver = add_customer_page_setup
    fill_out_customer_form(driver, name, s3_folder)
    click_save_customer_button(driver)
    validation_message_element1 = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, ".//td[contains(normalize-space(), 'Name is already in use.')]"))
    )
    validation_message_element2 = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, ".//td[contains(normalize-space(), 'S3 folder is already in "
                                                    "use.')]"))
    )
    validation_message_element3 = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, ".//td[contains(normalize-space(), 'Email is already in use.')]")))

    assert validation_message_element1 or validation_message_element2 or validation_message_element3
