from selenium import webdriver
from openpyxl import load_workbook

driver = webdriver.Chrome()
driver.get("")

#Read data from excel
wb = load_workbook("data.xlsx")
sheet = wb["sheet1"]

for row in sheet.iter_rows(min_row=2,max_row=sheet.max_row,min_col=1,max_col=2):
    username = row[0].value
    password = row[1].value

    #Enter username and password in the login form
    driver.find_element("id","username").send_keys(username)
    driver.find_element("id","password").send_keys(password)
    driver.find_element("id", "login").click()


    driver.back()
