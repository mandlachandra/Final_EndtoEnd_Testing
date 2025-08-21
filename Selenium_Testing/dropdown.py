from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
time.sleep(2)

driver.get("https://demo.automationtesting.in/Register.html")

# dropdown = driver.find_element(By.ID,"Skills")
# select = Select(dropdown)

dropdown = driver.find_element(By.ID,"Skills")
select = Select(dropdown)

select.select_by_visible_text("Python")
select.select_by_index(2)
time.sleep(2)
print("success")

# #select by visible text
# select_skill.select_by_visible_text("Python")
# time.sleep(2)
# print("success")

#4. How do you switch between frames or iframes?

# 5. How do you handle multiple browser windows or tabs?
# windows = driver.window_handles
# driver._switch_to.window((windows[1]))

# 6. How do you handle file uploads in Selenium?
# If the upload element is <input type = "file">,use send_keys()
# driver.find_element(By.ID,"upload").send_keys("c://path.pdf")

