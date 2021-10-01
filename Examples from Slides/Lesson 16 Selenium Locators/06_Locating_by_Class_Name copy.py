from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome('Selenium\driver\chromedriver_93.exe')
browser.get(r"C:\Users\Levon Grigoryan\Desktop\Visual Studio Code\Selenium\06_page_source.html")

content = browser.find_element_by_class_name('content')
print(content.text)