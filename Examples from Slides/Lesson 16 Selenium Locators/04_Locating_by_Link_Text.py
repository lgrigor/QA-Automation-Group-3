from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome('Selenium\driver\chromedriver_93.exe')
browser.get(r"C:\Users\Levon Grigoryan\Desktop\Visual Studio Code\Selenium\04_page_source.html")

continue_link = browser.find_element(By.LINK_TEXT, 'Continue')
continue_link = browser.find_element(By.PARTIAL_LINK_TEXT, 'Conti')

#print(continue_link.get_attribute('href'))
#print(continue_link.text)
continue_link.click()