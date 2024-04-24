import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# Function to perform login action on a Login page
def login(driver, email, password):
    """
        Perform login action on a Login page.

        Args:
            driver: WebDriver instance.
            email (str): Email address for login.
            password (str): Password for login.

        Returns:
            None
        """
    email_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "email"))
    )
    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    email_field.clear()
    password_field.clear()
    email_field.send_keys(email)
    password_field.send_keys(password)
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit"))
    )
    submit_button.click()


# Function to validate a successful login by checking whether Log Out option is present in the page.
def validate_successful_login(driver, email, password):
    """
        Validate a successful login by checking whether Log Out option is present in the page.

        Args:
            driver: WebDriver instance.
            email (str): Email address for login.
            password (str): Password for login.

        Returns:
            int: 1 if login is successful, 0 otherwise.
        """
    login(driver, email, password)
    time.sleep(1)
    dropdown_menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "navbar-login-menu"))
    )
    ActionChains(driver).move_to_element(dropdown_menu).click().perform()
    logout_link = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//ul[@class='dropdown-menu']//a[text()='Log out']"))
    )
    if logout_link.is_displayed():
        return 1
    else:
        return 0


# Function to fill the required details in add customer page
def fill_out_customer_form(driver, name, s3_folder):
    """
       Fill the required details in add customer page.

       Args:
           driver: WebDriver instance.
           name (str): Name of the customer.
           s3_folder (str): S3 folder name.

       Returns:
           None
       """
    driver.execute_script("window.scrollTo(0, 0);")
    name_field = driver.find_element(By.ID, "name")
    s3_folder_field = driver.find_element(By.NAME, "s3_folder")
    name_field.clear()
    s3_folder_field.clear()
    name_field.send_keys(name)
    s3_folder_field.send_keys(s3_folder)


# Function to click save after entering customer details
def click_save_customer_button(driver):
    """
        Click save after entering customer details.

        Args:
            driver: WebDriver instance.

        Returns:
            None
        """
    driver.find_element(By.ID, "save-customer").click()


# Function to check whether a validation message is present or popped up on the page
def validate_validation_message(driver, message):
    """
        Check whether a validation message is present or popped up on the page.

        Args:
            driver: WebDriver instance.
            message (str): Validation message to be checked.

        Returns:
            None
        """
    validation_message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, f".//td[contains(normalize-space(), '{message}')]"))
    )
    assert validation_message_element is not None


# Function to Navigate to the add customer page
def navigate_to_add_customer_page(driver):
    """
        Navigate to the add customer page.

        Args:
            driver: WebDriver instance.

        Returns:
            None
        """
    customers_dropdown = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Customers')]")))
    customers_dropdown.click()
    list_option = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'List')]")))
    list_option_link = list_option.get_attribute('href')
    driver.get(list_option_link)
    WebDriverWait(driver, 10).until(EC.url_contains("/my-customer/"))
    add_customer_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Add Customer')]")))
    add_customer_page = add_customer_button.get_attribute('href')
    driver.get(add_customer_page)
