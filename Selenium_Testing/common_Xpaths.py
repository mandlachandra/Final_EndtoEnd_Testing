#All rows in a table
#//table[@id='employeeTable']/tbody/tr

#First row in a table
#//table[@id='employeeTable']/tbody/tr[1]

#second cell (age) of first row
#//table[@id='employeeTable']/tbody/tr[1]/td[2]

#4. Loop Over Rows in Selenium
# rows = driver.find_elements(By.XPATH,"//table[@id='employeeTable']/tbody/tr")
# for row in rows:
#     email = row.find_element(By.XPATH,"./td[4]").text
#     print(email)

#Dynamic XPATH based on Header name
