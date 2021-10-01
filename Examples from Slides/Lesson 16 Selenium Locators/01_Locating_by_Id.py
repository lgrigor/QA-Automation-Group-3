from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome('Selenium\driver\chromedriver_93.exe')
browser.get("https://www.facebook.com/")

browser.find_element_by_id('email').send_keys('levon.grigoryan97@gmail.com')
browser.find_element(By.ID, 'email').send_keys('levon.grigoryan97@gmail.com')