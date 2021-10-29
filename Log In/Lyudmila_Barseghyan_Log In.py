from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome('chromedriver')
browser.get("https://www.saucedemo.com/")

browser.find_element_by_id("user-name").send_keys("standard_user")
browser.find_element_by_id("password").send_keys("secret_sauce")
browser.find_element_by_name("login-button").click()