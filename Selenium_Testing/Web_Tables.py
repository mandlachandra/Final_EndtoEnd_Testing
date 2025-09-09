from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get("https://www.screener.in/company/NIFTY/")
driver.maximize_window()
time.sleep(4)

rows= driver.find_elements(By.XPATH,"//div[@class='responsive-holder fill-card-width']//tbody//tr")

print("List of all 'name' column values:\n")
for row in rows:
    try:
        email = row.find_element(By.XPATH,"./td[2]").text
        print(email)

    except:
        continue

driver.close()




