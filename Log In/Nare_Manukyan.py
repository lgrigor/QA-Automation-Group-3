from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

username =  driver.find_element(By.XPATH, "//div[@class='login_credentials']").text[23:37]
password = driver.find_element(By.XPATH, "//div[@class='login_password']").text[23:36]

driver.find_element_by_name('user-name').send_keys(username)
driver.find_element_by_name('password').send_keys(password)
driver.find_element_by_id('login-button').click()
