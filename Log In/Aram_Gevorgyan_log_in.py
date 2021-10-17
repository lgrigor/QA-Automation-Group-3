from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(r'C:\Users\Aram\Drivers\chromedriver.exe')
browser.get("https://www.saucedemo.com/")

login = browser.find_element(By.XPATH, "//*[@id = 'login_credentials']")
user_login = login.text
#print(type(login.text))
word = user_login.split()
browser.find_element(By.ID, 'user-name').send_keys(word[3])
#print(word[3])

password = browser.find_element(By.CLASS_NAME, 'login_password')
user_password = password.text
word1 = user_password.split()
browser.find_element(By.ID, 'password').send_keys(word1[4])
print(word1[4])

login_button = browser.find_element(By.ID, 'login-button')
login_button.click()
#browser.find_element(By.ID, 'login-button').click()

#browser.quit()