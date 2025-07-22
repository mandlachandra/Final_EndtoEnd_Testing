from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from openpyxl import load_workbook
import time

# ✅ Read credentials from Excel
def read_credentials(file, sheet_name):
    wb = load_workbook(file)
    sheet = wb[sheet_name]
    username = sheet['A2'].value
    password = sheet['B2'].value
    return username, password

# ✅ Automate OrangeHRM Login
def orangehrm_login(username, password):
    # Set path for your ChromeDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    # Enter Username
    username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    username_field.send_keys(username)

    # Enter Password
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys(password)

    # Click Login Button
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    # ✅ Verify login success
    try:
        dashboard = wait.until(EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))
        print("✅ Login Successful: Reached Dashboard")
    except:
        print("❌ Login Failed: Check credentials")

    time.sleep(5)
    driver.quit()

# ✅ Main Execution
if __name__ == "__main__":
    excel_file = "C://Users//DELL//OneDrive//Desktop//Credentials.xlsx"
    sheet_name = "Sheet1"
    user, pwd = read_credentials(excel_file, sheet_name)
    orangehrm_login(user, pwd)
