import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=600,600')
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

browser = webdriver.Chrome('Selenium\driver\chromedriver_93.exe', options=chrome_options)
browser.get(r"C:\Users\Levon Grigoryan\Desktop\Visual Studio Code\Selenium_Commands\12_Page_Source.html")
browser.implicitly_wait(10)

browser.find_element(By.CSS_SELECTOR, '#try_it').click()

clock_start = time.strftime("%H:%M:%S", time.localtime())
element = browser.find_element(By.CSS_SELECTOR, '#waitCreate')
clock_stop = time.strftime("%H:%M:%S", time.localtime())

print(element.text)
print(f'START: {clock_start} - STOP: {clock_stop}')
