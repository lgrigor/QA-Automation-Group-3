
from os import name
from typing import Text
from selenium import webdriver
from selenium.webdriver.common.by import By

PATH = 'D:\driver\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

user_name = driver.find_element_by_id('login_credentials').text
print(user_name)

login_name =user_name.split('\n')
name = login_name[1]
print(name)

password = driver.find_element_by_class_name('login_password').text

password_name = password.split('\n')
pass_name = password_name[1]
print(pass_name)

user_name = driver.find_element_by_id('user-name').send_keys(name)
password= driver.find_element_by_id('password').send_keys(pass_name)
log_in = driver.find_element_by_id('login-button').click()
