# from selenium import webdriver
#from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()

# try:
#     element = driver.find_element(By.ID,"login")
#     element.click()
#
# except NoSuchElementException:
#     print("login button not found")


#how to handle multiple exceptions

# from selenium.common.exceptions import (
#     NoSuchElementException,
#     ElementNotInteractableException,
#     TimeoutException
# )
# try:
#     driver.find_element(By.ID,"submit").click()
#
# except (NoSuchElementException, ElementNotInteractableException, TimeoutException) as e:
#     print(f"Error occured: {type(e).__name__}")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# driver = webdriver.Chrome()
# driver.get("https://demo.automationtesting.in/Alerts.html")
# driver.maximize_window()
# time.sleep(2)
#
# element = driver.find_element(By.XPATH,'//button[contains(@class,"btn btn-danger")]').click()
# time.sleep(2)
# alert = driver.switch_to.alert
# print("Alert text is:",alert.text)
# alert.accept()
# driver.quit()



# element =driver.find_element(By.XPATH,"(//button[contains(text(),'click')])[1]")
# element.click()
# time.sleep(2)
#
# main_window = driver.current_window_handle
# print(main_window)
#
# for handle in driver.window_handles:
#     if handle!=main_window:
#         driver.switch_to.window(handle)
#         print("title of new tab:",driver.title)
#         driver.close()
#
# driver.switch_to.window(main_window)
# print("back to main window:",driver.title)
# driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service

#Alert Code

# driver = webdriver.Chrome()
# driver.get("https://demo.automationtesting.in/Alerts.html")
# time.sleep(2)
#
# element = driver.find_element(By.XPATH,'//button[contains(@class,"btn btn-danger")]').click()
# time.sleep(2)
# alert = driver.switch_to.alert
# print("alert text is:",alert.text)
# alert.accept()
# driver.quit()

#Frames
# driver = webdriver.Chrome()
# driver.get('https://demo.automationtesting.in/Frames.html')
# driver.maximize_window()
# time.sleep(2)
#
# driver.switch_to.frame("frame1")
# heading = driver.find_element(By.XPATH,'(//div[contains(@class,"col-xs-6 col-xs-offset-5")]//child::input)[1]')
# print("frame text:",heading.text)
# driver.switch_to.default_content()
# driver.quit()

#Window Handles
# driver = webdriver.Chrome()
# driver.get("https://demoqa.com/browser-windows")
# driver.maximize_window()
# time.sleep(2)
#
# parent_handle = driver.current_window_handle
# print("parent handle:",parent_handle)
#
# driver.find_element(By.XPATH,"//button[@id='tabButton']").click()
# time.sleep(2)
#
# #get all windows
# handles = driver.window_handles
# print("All handles:",handles)
#
# #switch to the child window(2nd handle)
# for handle in handles:
#     if handle!=parent_handle:
#         driver.switch_to.window(handle)
#         print("child window Title:",driver.title)
#         time.sleep(2)
#         driver.close()
#
# #switch back to parent window
# driver.switch_to.window(parent_handle)
# print("Back to Parent Title:",driver.title)
#
# driver.quit()
#Window Handles
# driver = webdriver.Chrome()
# driver.get("https://demoqa.com/browser-windows")
# driver.maximize_window()
# time.sleep(2)
# parent_handle = driver.current_window_handle
# print("parent handle:",parent_handle)
# driver.find_element(By.XPATH,"//button[@id='tabButton']").click()
# time.sleep(2)
# handles = driver.window_handles
# print("All handles",handles)
#
# for handle in handles:
#     if handle!=parent_handle:
#         driver.switch_to.window(handle)
#         print("child window:",driver.title)
#         driver.close()
#
# driver.switch_to.window(parent_handle)
# print("Back to parent title:",driver.title)

#......................
#Dropdown
# from selenium import webdriver
# #from selenium.webdriver.common.action_chains import ActionChains
# driver = webdriver.Chrome()
# driver.get("")
# driver.maximize_window()
# time.sleep(2)
#
# dropdown = driver.find_elements(By.ID,"cityDropdown")
#
# all_options = dropdown.options
#
# cities = [option.text for option in all_options]
# print("cities in dropdown:",cities)
# driver.quit()

#..................
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
#Mouse Hover
# driver = webdriver.Chrome()
# driver.get("https://demoqa.com/menu")
# driver.maximize_window()
# time.sleep(4)
# #locate the element to hover
# menu = driver.find_element(By.XPATH,'//a[text()="Main Item 2"]')
#
# #create actionchains object
# actions = ActionChains(driver)
# actions.move_to_element(menu).perform()
# time.sleep(2)
#
# #locate a submenu item revealed after hover
# submenu = driver.find_element(By.XPATH,"//a[text()='SUB SUB LIST »']")
# actions.move_to_element(submenu).perform()
#
# #click on a sub sub menu item
# sub_sub_item = driver.find_element(By.XPATH,"//a[text()='Sub Sub Item 1']")
# sub_sub_item.click()
#
# time.sleep(2)
# driver.quit()


#what is shadwo dom ?
#Shadow Dom in selenium involves interacting with web elements encapsulated with shadow DOM
#Seperate DOM Tree attached to a regular DOM element.
#Selenium provides methods for accessing and manipulating these hidden elements through JavaScript execution
#and native support in Selenium 4

#Understanding Shadow DOM
#Encapsulation: Shadow DOM allows for encapsulation of styles and behaviour preventing interference with main document.
#Shadow Host : The regular DOM element to which the shadow DOM is attached
#Shadow Tree : The DOM tree within the shadow DOM
#Shadow Root : The root node of the shadow tree

#selenium and Shadow DOM
#Selenium 4 : Introduced native support for Shadow DOM, allowing for direct interaction with shadow roots.
#Javascript Execution: Selenium can execute javascript to interact with Shadow DOM elements, especially when older
#selenium versions are used or when direct support is unavailable
#XPath and CSS Selectors: XPath and CSS selectors can be used to target elements within the shadow DOM,
#But with specific considerations for navigating the nested structure

#Steps for Automating Shadow DOM Elements
#1.Identify Shadow DOM: Inspect the element in the browser's developer tools to confirm its presence within a Shadow DOM
#2.Access Shadow Root: Use getShadowRoot() (Selenium 4) or execute JavaScript to retrieve the Shadow root of the host element
#3.Interact with Elements : Once the Shadow root is obtained , you can locate and interact with elements within the
#Shadow DOM using Standard Selenium methods like findelement or findelements
#4.Handle Nested Shadow DOM: For nested Shadow DOMS, repeat the process for each level of nesting , accessing shadow roots iteratively
#
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("your_page_url")
#
# # Get the shadow host element
# shadow_host = driver.find_element_by_css_selector("your_shadow_host_selector")
#
# # Access the shadow root (Selenium 4)
# shadow_root = shadow_host.shadow_root
#
# # Find an element within the shadow DOM
# element_in_shadow = shadow_root.find_element_by_css_selector("your_element_selector")
#
# # Perform actions on the element
# element_in_shadow.click()
#
# driver.quit()
# #...........................................
#2.what is the diff b/w json.dump and json.load
#json.loads() : This function is used to parse a JSON string and converts into a python object
#json.dump() :This function is used to serialize a python object into a JSON formatted string and write it to a file like object

#..........................
#3.Nested list
# def flatten_list(nested_list):
#     flat = []
#     for item in nested_list:
#         if isinstance(item,list):
#             flat.extend(flatten_list(item))
#         else:
#             flat.append(item)
#     return flat
#
# input_data = [3, 5, [9, [7, 8, [12, 71]]]]
# output = flatten_list(input_data)
# print(output)

# #Write a program to find out common letters b/w 2 strings
#
# # str1 = "reene"
# # str2 = "naina"
#
# # def common_letters():
# #     str1 = input("enter the first string:")
# #     str2 = input("enter the second string:")
# #     s1 = set(str1)
# #     s2 = set(str2)
# #     lst = s1 & s2  # & is used to extract common letter
# #     print(lst)
# #
# # common_letters()
#
# #write a python program to count the frequency of words appearing in a string
#
# # def frequency_words():
# #     str = input("enter the string:")
# #     lst = str.split()
# #     d = {}
# #
# #     for i in lst:
# #         if i not in d.keys():
# #             d[i] = 0
# #         d[i] = d[i]+1
# #     print(d)
# #
# # frequency_words()
#
# #how to convert 2 lists into dictionary
#
#
# # def list_to_dict():
# #     keys = [1,2,3]
# #     values = ["one","two","three"]
# #     result = dict(zip(keys,values))
# #     print(result)
# #
# # list_to_dict()
#
# # def list_to_dict():
# #     keys = [1, 2, 3]
# #     values = ["one","two","three"]
# #     result =dict(zip(keys, values))
# #     print(result)
# #
# # list_to_dict()
#
# #Find missing numbers in an array using summation
#
# # def missing_summation():
# #     n = a[-1]
# #     sum1 = 0
# #     total = n*(n+1)//2
# #     sum1 = sum(a)
# #     print(total-sum1)
# #
# # a = [1,2,4,5,6,7]
# # missing_summation()
#
# #Find the smallest and largest element in a array
#
# def largest():
#     n = len(arr)
#     max = arr[0]
#
#     for i in range(0,n):
#         if arr[i]>max:
#             max = arr[i]
#     return max
# arr = [63,54,98,34,89,42,18]
# largest(arr)
#
#
# # def largest(arr):
# #     n = len(arr)
# #     max = arr[0]
# #     for i in range(n):
# #         if arr[i]>max:
# #             max = arr[i]
# #     return max
# # arr = [63,54,98,34,89,42,18]
# # largest()
#
#
#
#
#















