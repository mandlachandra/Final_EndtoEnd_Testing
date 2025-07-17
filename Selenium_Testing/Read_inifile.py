from selenium import webdriver
import configparser

driver = webdriver.Chrome()

config = configparser.ConfigParser()
config.read("config.ini")

browser = config["DEFAULT"]["browser"]
url = config["DEFAULT"]["base_url"]

if browser == "chrome":
    driver = webdriver.Chrome()
elif browser == "firefox":
    driver = webdriver.Firefox()

driver.get(url)
