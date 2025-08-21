# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time
#
# #replace with your credentials and file
# aws_username = ""
# aws_password = ""
# file_to_upload = "C://path/to/you/file.txt"
# bucket_name = "your_bucket_name"
#
# #launch chrome
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.maximize_window()
# time.sleep(2)
#
# #Go to AWS console login
# driver.get("https://signin.aws.amazon.com/console")
#
# #login
# time.sleep(2)
# driver.find_element(By.ID,"resolving_input").send_keys(aws_username,Keys.RETURN)
# time.sleep(2)
# driver.find_element(By.ID,"password").send_keys(aws_password)
# time.sleep(2)
# driver.find_element(By.ID,"signin_button").click()
#
# #wait for login and navigate to s3
# time.sleep(5)
# driver.get("https://s3.console.aws.amazon.com/home")
#
# #click your bucket
# time.sleep(4)
# driver.get(f"https://s3.console.aws.amazon.com/s3/buckets/{bucket_name}?tab=objects")
#
# #click upload
# time.sleep(5)
# upload_button = driver.find_element(By.XPATH,"//button[contains(text(), 'Upload')]")
# upload_button.click()
#
# #upload file
# time.sleep(5)
# file_input = driver.find_element(By.XPATH,"//input[@type='file']")
# file_input.send_keys(file_to_upload)
#
# #click upload to confirm
# time.sleep(5)
# final_upload = driver.find_element(By.XPATH,"//button[.='upload']")
# final_upload.click()
#
# print("File upload triggered.")
# time.sleep(5)
# driver.quit()
