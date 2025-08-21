# #using contains
# #useful for dynamic attributes
# //input[contains(@id, 'user')]
#
# #using starts-with()
# //input[starts-with(@name, 'user')]
#
# #using text() to match exact text
# //button[text()='login']
#
# #using contains(text())
# //a[contains(text(),'forgot')]
#
# #using and / or conditions
# //input[@type='text' and @name='username']
#
# #parent to child navigation
# //div[@class='form-group']/input
#
# #child to parent navigation
# //input[@name='email']/..
#
# #following sibling
# //label[text()='email']/following-sibling::input
#
# #preceding-sibling
# //input[@name='email']/preceding-sibling::label
#
# #ancestor
# //input[@id='username']/ancestor::form
#
# #descendant
# //div[@class='container']//descendant::input
#
# #using indexing
# (//input[@type='text'])[2]
#
# #using position()
# (//button[@class='submit'])[position()=2]
#
# #complex
# <div class="form">
#     <label>Email</label>
#     <input type="text" name="email" id="user_1234">
# </div>
#
# //div[@class='form']//input[@id,'user']
#
# <a href="https://example.com/docs/tutorial.pdf">Download PDF</a>
#
# //a[contains(@href,'tutorial.pdf')]
#
# Can you locate an element by the URL it links to?
# yes by using Xpath like //a[@href='url'] or contains(@href,'keyword')

# from openpyxl import load_workbook
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# #Load excel file
# wb = load_workbook("C://Users//DELL//OneDrive//Desktop//Credentials.xlsx")
# sheet = wb["Sheet1"]
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# time.sleep(2)
#
# for row in sheet.iter_rows(min_row=2,max_row=sheet.max_row,min_col=1,max_col=2):
#     username = row[0].value
#     password = row[1].value
#
#     driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#     time.sleep(4)
#
#     driver.find_element(By.NAME,"username").send_keys(username)
#     driver.find_element(By.NAME,"password").send_keys(password)
#     driver.find_element(By.XPATH,"//button[@type='submit']").click()
#     time.sleep(2)
#     print("successfully Logged in")
#
# driver.quit()
