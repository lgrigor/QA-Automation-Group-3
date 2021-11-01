from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome('chromedriver')
browser.get("https://www.saucedemo.com/")

find_user_name = browser.find_element(By.ID, "login_credentials")
find_user_password = browser.find_element(By.CLASS_NAME, "login_password")
user_name = browser.find_element(By.ID, "user-name").send_keys(find_user_name.text.split('\n')[1])
password = browser.find_element(By.ID, "password").send_keys(find_user_password.text.split('\n')[1])
browser.find_element(By.ID, "login-button").click()
