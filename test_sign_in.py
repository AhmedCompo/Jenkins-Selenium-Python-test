from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, WebDriverException
import time
import openpyxl

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(options=options)


wait = WebDriverWait(driver, 30)
actions = ActionChains(driver)
url = "https://corporate.friendycar.com/auth/login?redirectFrom=/"



# automating URL
def open_url(url):
    try:
        driver.get(url)
        print(f"URL opened successfully!")
    except TimeoutException:
        print(f"Timeout: Failed to open URL {url} within the specified time.")
    except WebDriverException as e:
        print(f"WebDriverException: Failed to open URL {url}. Error: {e}")


def error_msg(exeption):
    errorMsg = str(exeption)
    error_lines = errorMsg.split('\n')
    for line in error_lines[:2]:
        return line

# automating sign in process


def SignIn(email, password):
    driver.find_element(By.NAME, "email").clear()  # Clear old email value
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.ID, "passwordInput").clear()
    driver.find_element(By.ID, "passwordInput").send_keys(password)
    # remember_me_checkbox = driver.find_element(By.XPATH, "//label[@for='remember']")
    # remember_me_checkbox.click()
    driver.find_element(By.TAG_NAME, "button").click()
    try:
        # Check if sign-in is successful (Dashboard page is loaded)
        successful_signin_element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//h1[contains(text(), 'Dashboard')]"))
        )
        print("Sign in successful!")
        driver.save_screenshot("screenshot_after_signin.png")
        # sign-out here
        # driver.find_element(By.XPATH, "//button[contains(text(), 'Sign Out')]").click()
        # wait.until(EC.alert_is_present()).accept()
    # except UnexpectedAlertPresentException:
    #     print("Unexpected alert present during sign-in. Handling alert...")
    #     handle_unexpected_alert()
    except Exception as e:
        # Check different error scenarios
        if "Invalid credentials" in driver.page_source:
            print("Sign in failed: Invalid credentials")
        elif "Email is required" in driver.page_source:
            print("Sign in failed: Email is required")
        elif "Password is required" in driver.page_source:
            print("Sign in failed: Password is required")
        else:
            print("Sign in failed: Unexpected error -", error_msg(e))


def clear_old_values():
    driver.delete_all_cookies()
    print("Cleared old values.")


# Read test cases from the file and test each case

def test_cases_from_excel(filename):
    # Load the Excel workbook
    workbook = openpyxl.load_workbook(filename)
    worksheet = workbook.active
    first_row_skipped = False

    # Read each row in the worksheet and test the corresponding test case
    for row in worksheet.iter_rows(values_only=True):
        if not first_row_skipped:
            first_row_skipped = True
            continue

        email, password = row
        if email or password:
            # If email or password is not provided, replace None with empty string
            email = email if email else ""
            password = password if password else ""
            print(f"Testing with email: ({email}) , password: ({password})")
            SignIn(email,password)
            clear_old_values()
            print()


open_url(url)
start_time = time.time()
driver.maximize_window()
test_cases_from_excel("signIn_test_data.xlsx")
end_time = time.time() - start_time
print(f"Test completed in {end_time:.2f} seconds")
driver.quit()
