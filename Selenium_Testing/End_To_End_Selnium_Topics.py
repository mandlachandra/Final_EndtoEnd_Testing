# from selenium import webdriver
# from openpyxl import load_workbook
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time
#
# #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# # driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# # driver.maximize_window()
# # driver.implicitly_wait(10)
# # # wait = WebDriverWait(driver,10)
# # # element = wait.until(EC.presence_of_element_located(By.ID))
# #
# # #read data from excel
# # wb = load_workbook("C://Users//DELL//OneDrive//Desktop//Credentials.xlsx")
# # sheet = wb["Sheet1"]
# #
# # for row in sheet.iter_rows(min_row=2,max_row=sheet.max_row,min_col=1,max_col=2):
# #     username = row[0].value
# #     password = row[1].value
# #
# #     driver.find_element(By.NAME,'username').send_keys(username)
# #     driver.find_element(By.NAME,'password').send_keys(password)
# #     driver.find_element(By.XPATH,"//button[@type='submit']").click()
# #     time.sleep(4)
# #     #print("success")
# #
# #     #assert "orangehrmlive" in driver.title, "url does not contain orangehrmlive"
# #
# #     assert driver.current_url.startswith("https://opensource"), "url wont starts with https://"
# #
# #     print("All assertions are passed")
#
# #dropdown values
# # admin = driver.find_element(By.XPATH,"(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[1]")
# # admin.click()
# # time.sleep(2)
# #
# #
# # driver.find_element(By.XPATH,"//span[contains(text(),'Qualifications' )]").click()
# # options = driver.find_elements(By.XPATH,"//ul[@class='oxd-dropdown-menu']//a")
# #
# #
# # print("Dropdown values are:")
# # for opt in options:
# #     print(opt.text)
# #
# # time.sleep(4)
#
# #Window Handles
# # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# # driver.get("https://demoqa.com/browser-windows")
# # driver.maximize_window()
# # time.sleep(2)
# #
# # parent_handle = driver.current_window_handle
# # print("parent handle",parent_handle)
# #
# # driver.find_element(By.ID,"windowButton").click()
# # time.sleep(4)
# #
# # handles = driver.window_handles
# # print("All handles",handles)
# #
# # for handle in handles:
# #     if handle!=parent_handle:
# #         driver.switch_to.window(handle)
# #         print("child window",driver.title)
# #         driver.close()
# #
# # driver.switch_to.window(parent_handle)
# # print("Back to parent window",driver.title)
#
# #Alerts
# # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# # driver.get("https://demo.automationtesting.in/Alerts.html")
# # driver.maximize_window()
# # time.sleep(4)
# #
# # element = driver.find_element(By.XPATH,'//button[@class="btn btn-danger"]]').click()
# # alert = WebDriverWait(driver,10).until(EC.alert_is_present())
# #
# # assert alert.text == "I am an alert box!", f"Expected cheese' but got {alert.text}"
# #
# # alert.accept()
#
# #Frames
# #Ways to Switch to a Frame in Selenium Python
# #By Index
# # driver = webdriver.Chrome()
# # driver.switch_to.frame(0)
# #
# # #By Name
# # driver.switch_to.frame("Name")
# #
# # #By WebElement
# # frame_element = driver.find_element(By.XPATH,"")
# # driver.switch_to.frame(frame_element)
# #
# # #Switch to the first iframe
# # driver.switch_to.frame("iframefirst")
# #
# # #Now switch to nested iframe inside it
# # driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe"))
# #
# # #Interact with element inside iframe
# # element = driver.find_element(By.XPATH,"")
# # print("Text inside iframe",element.text)
# #
# # #switch back to main page
# # driver.switch_to.default_content()
#
# #Mouse & Keyboard Actions (ActionChains)
# # from selenium.webdriver import ActionChains
# # driver= webdriver.Chrome()
# #
# # actions = ActionChains(driver)
# # element = driver.find_element(By.ID,"menu")
# #
# # actions.move_to_element(element).click().perform()
# # actions.double_click().perform()
# # actions.context_click().perform()
#
# #File Upload & Download
# from selenium import webdriver
# #
# driver=webdriver.Chrome()
# # driver.find_element(By.ID,"uploadFile").send_keys("C://file.text")
#
# #Taking Screenshots
# driver.save_screenshot("screenshot.png")
#
# #JavaScript Execution
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
#
# #Assertions (Unittest / Pytest)
# assert "Orangehrm" in driver.title
#
# #Parallel Execution (Pytest-xdist)
# # pytest -n 3 test_file.py
#
# #Handling Dynamic Elements
# #element = WebDriverWait(driver,10).until(EC.presence_of_element_located(By.XPATH,""))
#
# #Headless Mode
# from selenium.webdriver.chrome.options import Options
#
# options = Options()
# options.add_argument("--headless")
# driver = webdriver.Chrome(options=options)
#
# #Grid/Remote Execution
# driver = webdriver.Remote(
#     command_executor="http://localhost:4444/wd/hub",
#     options=webdriver.ChromeOptions()
# )
# # Explanation of each part
# #
# # webdriver.Remote
# #
# # Used when you want to run tests remotely (not just local webdriver.Chrome()).
# #
# # This is essential in Selenium Grid, Docker, or cloud platforms like BrowserStack, Sauce Labs, LambdaTest, etc.
# #
# # command_executor="http://localhost:4444/wd/hub"
# #
# # This is the URL of the Selenium Grid Hub (or remote server).
# #
# # localhost:4444 → means Selenium Grid Hub is running on your local machine at port 4444.
# #
# # /wd/hub → WebDriver endpoint that listens for requests.
# #
# # 🔹 Example:
# #
# # Local Selenium Grid: http://localhost:4444/wd/hub
# #
# # Remote server: http://192.168.1.100:4444/wd/hub
# #
# # Cloud: https://hub.browserstack.com/wd/hub
# #
# # options=webdriver.ChromeOptions()
# #
# # Defines the browser type and configuration.
# #
# # Example: headless mode, user-agent, incognito.
# #
# # Since we passed ChromeOptions(), it will start Google Chrome on the remote machine.
# #
# # 🔹 When to use this?
# #
# # Selenium Grid: Run tests across multiple machines/browsers in parallel.
# #
# # Docker Selenium: Run Chrome/Firefox inside Docker containers.
# #
# # Cloud Testing: Run on BrowserStack, Sauce Labs, LambdaTest.
# #
# # 🔹 Example – Running on Selenium Grid
# # from selenium import webdriver
# #
# # chrome_options = webdriver.ChromeOptions()
# # chrome_options.add_argument("--headless")  # optional
# #
# # driver = webdriver.Remote(
# #     command_executor="http://localhost:4444/wd/hub",
# #     options=chrome_options
# # )
# #
# # driver.get("https://www.google.com")
# # print(driver.title)
# # driver.quit()
#
#
#
#
#
#
#
