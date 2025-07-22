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

skills_dropdown = driver.find_element(By.ID,"Skills")
select_skill = Select(skills_dropdown)

#select by visible text
select_skill.select_by_visible_text("Python")
time.sleep(2)