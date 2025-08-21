# from selenium import webdriver
#
# #launching browser
# driver = webdriver.Chrome()
#
# #Open a website
# driver.get("")
#
# #get current url
# print(driver.current_url)
#
# #get page title
# print(driver.title)
#
# #maximize/minimize/fullscreen
# driver.maximize_window()
# driver.minimize_window()
# driver.fullscreen_window()
#
# #refresh
# driver.refresh()
#
# #get page source
# html = driver.page_source
# print(html)
#
# #close the current tab
# driver.close()
#
# #quit
# driver.quit()
#
# #delete all cookies
# driver.delete_all_cookies()
#
# #take screenshot of page
# driver.save_screenshot("screenshot.png")
#
# #open a new tab or window
# driver.execute_script("window.open('https://google.com)")
#
# #switch b/w 2 tabs
# handles = driver.window_handles
# driver.switch_to.window(handles[1])
#
# #set browser window size & position
# driver.set_window_size(1024,768)
# driver.set_window_position(100,100)