import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Tests.helper_functions import fill_out_customer_form, click_save_customer_button, validate_successful_login
from faker import Faker

fake = Faker()


# Function to test the add customer functionality and retrieving email and password
# and validating login with same credentials
@pytest.mark.parametrize("name, s3_folder",
                         [(fake.company(), fake.name().replace(' ', ''))])
def test_add_customer(add_customer_page_setup, name, s3_folder):
    """
        Test the add customer functionality, retrieve email and password, and validate login with the same credentials.

        Args:
            add_customer_page_setup: Fixture to set up test environment for adding a customer and validating the add customer form.
            name (str): Name of the customer.
            s3_folder (str): S3 folder name.

        Returns:
            None
        """
    driver = add_customer_page_setup
    print(driver.current_url)
    fill_out_customer_form(driver, name, s3_folder)
    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.NAME, "password")
    email = email_input.get_attribute("value")
    password = password_input.get_attribute("value")
    click_save_customer_button(driver)
    WebDriverWait(driver, 20).until(EC.url_changes(driver.current_url))
    dropdown_menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "navbar-login-menu"))
    )
    ActionChains(driver).move_to_element(dropdown_menu).click().perform()
    logout_link = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[text()='Log out']"))
    )
    logout_link.click()
    result = validate_successful_login(driver, email, password)
    assert result == 1
