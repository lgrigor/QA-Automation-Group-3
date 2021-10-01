from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome('Selenium\driver\chromedriver_93.exe')
browser.get(r"C:\Users\Levon Grigoryan\Desktop\Visual Studio Code\Selenium\03_page_source.html")

# Scenario 1
#username = browser.find_element_by_xpath("/html/body/form/input[2]")
#username = browser.find_element_by_xpath("//input[1]")
#username = browser.find_element_by_xpath("//input[@name='username']")
#username = browser.find_element_by_xpath("//form/input[@name='username']")
#username = browser.find_element_by_xpath("//form[@id='loginForm']/input[1]")

#username.send_keys('levon.grigoryan97@gmail.com')


# Scenario 2
clear_button = browser.find_element(By.XPATH, "//tool[@section=\"developer\"]")
clear_button = browser.find_element(By.XPATH, "//form[@id='loginForm']/input[4]")

clear_button.click()