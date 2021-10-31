from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome(r'C:\Users\ARARAT MANUKYAN\Desktop\homework1.py\drivers\chromedriver.exe')
browser.get("https://www.saucedemo.com/")

log = browser.find_element(By.ID,'login_credentials').text
login = log.split()
browser.find_element_by_id("user-name").send_keys(login[3])
passw = browser.find_element_by_class_name('login_password').text
word = passw.split()
password= browser.find_element(By.XPATH,"//div[@class='form_group']//input[@name='password']").send_keys(word[4])
Login = browser.find_element(By.ID, "login-button").click()



#browser.find_element_by_id('user-name').send_keys(name)
#password= browser.find_element(By.XPATH,"//div[@class='form_group']//input[@name='password']")
#password.send_keys('secret_sauce')
#Login = browser.find_element(By.ID, "login-button")
#Login.click()

