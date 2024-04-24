# Impel SDET Challenge

### **Requirements and Dependencies**

    Run the following command in the root directory of the project
    pip install -r requirements.txt

### **Set the environment variables for storing ADMIN Email and Password**

       For security purpose ADMIN Email and Password is stored in os environment variables
        Run this command in terminal 
            echo $SHELL, This command will output the path to your 
            default shell executable (e.g., /bin/bash, /bin/zsh, etc.).
        Depending on your default shell, you'll edit the corresponding configuration file:
            For Bash: ~/.bash_profile or ~/.bashrc
            For Zsh: ~/.zshrc
        In Terminal, use a text editor like nano, vim, or TextEdit to open the configuration file
            nano ~/.zshrc
        Add the Environment Variable:
            export VALID_EMAIL=manish@impel.io
            export VALID_PASSWORD=WGZbeRGL
        Save and exit the editor

### **Steps to Run**

    Open Terminal and go to project directory and run following commands in terminal
        cd Tests
        pytest

_Test Report can be found in report.html file_

#### Test case 1:Login using Invalid credentials
    
    objective: To verify that the login page properly handles invalid credentials.
    Test Steps:
        1.     Open the Chrome browser.
        2.     Navigate to the login page.
        3.     Enter invalid credentials (e.g., incorrect username or password).
        4.     Click on the login button.
        5.     Verify that the appropriate error message is displayed.
    Expected Result: Display a message such as "invalid username and password"
    Actual Result: Invalid username or password

#### Test Case 2:Login using empty credentials

    objective:To verify that the login page properly handles empty credentials.
    Test Steps:
      1.     Open the Chrome browser.
      2.     Navigate to the login page.
      3.     Leave the username and password fields empty.
      4.     Click on the login button.
      5.     Verify that the appropriate error message is displayed.
   Expected Result: The system should display an error message indicating that the credentials cannot be empty.
   Actual Result:Please fill out this field.

#### Test case 3:Login with valid credentials
   
       objective:To verify that the login page allows access with valid credentials.
       Test Steps:
          1.     Open the Chrome browser.
          2.     Navigate to the login page.
          3.     Enter valid credentials.
          4.     Click on the login button.
          5.     Verify that the user is successfully logged in and directed to the expected page and verify if logout button is displayed
       Expected Result: The system should allow access and redirect the user to the intended page after successful login and was able to logout
       Actual Result: The login was successfully done and redirected to the user dashboard and logout button was found 

#### Test case 4:Validate Empty Inputs on Add Customer Page

    Objective:To ensure that the add customer page correctly validates and displays error messages when required fields are left empty or contain spaces.
    Test Steps:
    1.     Open the Chrome browser.
       2.     Navigate to the add customer page.
       3.     Leave the name and S3 folder fields empty.
       4.     Click on the save customer button.
       5.     Verify that the "Name is required,S3 Folder is required" validation message is displayed.
       6.     Provide a company name and leave the S3 folder field empty.
       7.     Click on the save customer button.
       8.     Verify that the "S3 folder is required." validation message is displayed.
       9.     Provide a valid company name and a name with spaces in the S3 folder field.
       10.     Click on the save customer button.
       11.     Verify that the "S3 folder cannot have spaces" validation message is displayed.
    Expected Result:The system should display appropriate error messages when required fields are left empty or contain spaces on the add customer page.
    Actual Result:Error messages displayed when name and S3 Folder left empty and "S3 folder cannot have spaces" message displayed when s3 folder had spaces.
    Bug Encountered: The system should not accept names with special characters such as $#%^& but the system accepted such names example:MarutiSuzuki,$#%^&

#### Test case 5:Validate Customer Already Exists on Add Customer Page

    Objective: To verify that the add customer page correctly handles adding a customer with details that already exist in the database.
    Test Steps:
    1.     Open the Chrome browser.
       2.     Navigate to the add customer page.
       3.     Enter the name "ABC Hyundai" and S3 folder "abchyundai", which already exist in the database.
       4.     Click on the save customer button.
       5.     Verify that either of the following validation messages is displayed:
       6.     "Name is already in use."
       7.     "S3 folder is already in use."
       8.     "Email is already in use."
    Expected Result:The system should display a validation message indicating that the customer details already exist in the 
    database on the add customer page.
    Actual Result:"Name is already in use.", "S3 folder is already in use." messages displayed 

#### Test case 6:Add Customer and Validate Login Credentials

    Objective:To verify that the add customer functionality correctly adds a new customer, retrieves the email and password, 
    and validates login with the same credentials.
    
    Test Steps:
    1.     Open the Chrome browser.
       2.     Navigate to the add customer page.
       3.     Fill out the customer form with a company name and a unique S3 folder name.
       4.     Retrieve the email and password values entered in the form.
       5.     Click on the save customer button.
       6.     Wait for the URL to change, indicating successful addition of the customer.
       7.     Open the dropdown menu by hovering over the login menu.
       8.     Click on the "Log out" link.
       9.     Verify that the system logs out successfully.
       10.     Validate login using the retrieved email and password.
       11.     Verify that the system successfully logs in with the provided credentials.
    Expected Result:The system should successfully add a new customer, retrieve the email and password values, log out the user, 
    and validate login using the same credentials. The test should pass without any errors.
    Actual Result: Customer was added successfully and was able to log in with credentials generated and log out

#### My Approach for Validating Login 

    To test the login functionality, I've implemented the following approach: after a successful login, 
    the presence of a logout option indicates success. Therefore, I search for the logout option 
    on the redirected page to confirm a successful login
    

To extend the testing framework to cover additional scenarios, we can leverage existing tests and adapt them for new features. 
For instance, the validation logic applied to the login page can be repurposed for validating registration pages. Similarly, 
tests designed for the "Add Customer" form can be reused for testing the "Edit Customer" functionality. Furthermore, 
after editing customer details, we can validate the login process to ensure the changes are reflected correctly.

Additionally, the login validation mechanism developed for the main login page can be easily modified and integrated into 
other sections, such as the "Add Login" option within the admin dashboard of the 360 Manager. This versatility 
allows for efficient testing across various features and dashboards within the application.






