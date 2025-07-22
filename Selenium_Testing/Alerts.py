from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.selenium.dev/selenium/web/alerts.html#")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.XPATH,"//a[@id='alert']").click()
alert = WebDriverWait(driver,5).until(EC.alert_is_present())

assert alert.text == "cheese", f"Expected cheese' but got {alert.text}"

alert.accept()
