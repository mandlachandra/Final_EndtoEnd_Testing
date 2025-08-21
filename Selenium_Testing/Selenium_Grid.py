# In Michaels project we had a requirement to validate our e-commerce application across multiple browsers
# like chrome,firefox and edge, since a large user base was spread across thes
# initially we were executing tests sequentially on our local machine which was very slow and not scalable
# To address this i implemented Selenium Grid for distributed and parallel execution
#
# ->I set up a hub on a central server and registered multiple Nodes(Chrome,fireforx and edge)
# running on different virtual machines
# ->We integreted this with our Pytest framework so that based on the browser parameter the test cases
# would dynamically pick the right node from the grid
#
# Ex:
# from selenium import webdriver
# driver = webdriver.Chrome()
#
# def get_driver(browser_name):
#     grid_url = "http://hub.michaels.com:4444/wb/hub"
#     capabilities = {"browserName":browser_name}
#     return webdriver.Remote(command_executor=grid_url,
#                             desired_capabilities=capabilities)
#
# def test_login():
#     driver = get_driver("chrome") #could be firefor or edge
#     driver.get("https://www.michaels.com")
#     assert "Michaels" in driver.title
#     driver.quit()
#
# #using Grid we achieved parallel execution across diferent browsers and OS combinations which
# reduced execution time drastically (from 3 hours sequentially to under 1 hour in parallel)
# ->Later we connected Selenium Grid with Jenkins pipeline so that every build triggered cross browser
# test execution automatically
#
# ->This helped us ensure cross browser compatability and catch browser specific UI bugs early
# improving product quality.
