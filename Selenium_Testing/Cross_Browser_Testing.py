#Cross browser testing is the process of verifying that your web application works as expected
#across multiple browsers and versions
# ->Chrome
# ->firefox
# ->Edge
# ->Safari
# ->opera
# #The main goal is to check the compatibility,UI consistency and functionality across browsers
#
# Why is Cross Browser Testing Important?

from selenium import webdriver

grid_url ="http://localhost:4444/wd/hub"

#run on chrome
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Remote(command_executor=grid_url,options=chrome_options)
driver.get("")
print("Title on Chrome",driver.title)
driver.quit()

#run on firefox
firefox_options = webdriver.FirefoxOptions()
driver=webdriver.Remote(command_executor=grid_url,options=firefox_options)
driver.get("")
print("Title in firefox",driver.title)
driver.quit()