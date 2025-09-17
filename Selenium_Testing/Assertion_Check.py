from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#1.URL Assertion
#Check if URL has changed from PLP to PDP Page
driver = webdriver.Chrome()

plp_url = driver.current_url
driver.find_element(By.XPATH,"//div[@class='product-card'][1]").click()

WebDriverWait(driver,10).until(EC.url_changes())

assert "product" in driver.current_url.lower()

#2.Title Assertion
title = driver.title
assert "product" in title or "Michaels" in title

#3.Element Presence Assertion
#check PDP-Specific elements(which don't exists in PLP)
# Product name
# Add to cart button
# Price element

product_name = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//h1[@class='product-title']")))
assert product_name.is_displayed()

add_to_cart = driver.find_element(By.ID,"addToCartButton")
assert add_to_cart.is_displayed()



