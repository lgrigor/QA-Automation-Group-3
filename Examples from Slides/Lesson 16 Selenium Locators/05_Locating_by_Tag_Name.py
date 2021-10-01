from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome('Selenium\driver\chromedriver_93.exe')
browser.get(r"C:\Users\Levon Grigoryan\Desktop\Visual Studio Code\Selenium\05_page_source.html")

heading1 = browser.find_element(By.TAG_NAME, 'h1')
print(heading1.text)