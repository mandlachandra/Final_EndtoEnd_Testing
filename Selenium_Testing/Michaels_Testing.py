from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    driver.get("https://www.michaels.com/")
    driver.maximize_window()
    time.sleep(2)

    #locate the actual input inside the div
    search_bar = driver.find_element(By.XPATH,"//input[@aria-label='Search Input']")
    search_bar.clear()
    search_bar.send_keys("yarn")
    search_bar.send_keys(Keys.RETURN)
    time.sleep(10)
    #assert "yarn" in driver.title.lower(), "search keyword not found in title"
    assert "yarn" in driver.current_url.lower(), "search keyword not found in url"

    # heading = driver.find_element(By.XPATH, "//h1").text.lower()
    # assert "yarn" in heading, "Search heading does not contain keyword"

    print("All Assertions are passed")

    add_to_cart = driver.find_element(By.XPATH,"(//div[@class='ejd82nx0 css-ydh963']//button[contains(text(),'Add to Cart')])[1]")
    add_to_cart.click()
    time.sleep(4)
    continue_shopping = driver.find_element(By.XPATH,"//div[contains(text(),'Continue Shopping')]")



finally:
    driver.quit()
