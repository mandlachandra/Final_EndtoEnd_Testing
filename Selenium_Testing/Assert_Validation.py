from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import allure

#set up chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get("https://www.google.com")
    driver.maximize_window()
    time.sleep(2)
    print(driver.current_url)
    # html = driver.page_source
    # print(html)
    cookies = driver.get_cookies()
    print(cookies)
    driver.save_screenshot("screenshot.png")
    #driver.execute_script("window.open('https://youtube.com')")
    #driver.execute_script("window.open('https://facebook.com')")
    #driver.set_window_size(1024,768)


    #step 2: Assertions
    #Assert page title contains "google"
    assert "Google" in driver.title, "page does not contain 'google'"

    #step 3:Assert url is correct
    assert driver.current_url.startswith("https://www.google."),"url does not starts with https://"

    search_box = driver.find_element(By.NAME,"q")
    assert search_box.is_displayed(),"search_box is not visible"

    print("All assertions are passed")

    search_box.send_keys("OpenAI,CHATGPT")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    assert "OpenAI" in driver.title, "results page doesnot contains 'oOpenAI;"

    print("search test passed")

finally:
    driver.quit()






