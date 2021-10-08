from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--log-level=3')

browser = webdriver.Chrome('Selenium\driver\chromedriver_93.exe', options=chrome_options)
browser.get("https://www.google.com/")

form = browser.find_element(By.CSS_SELECTOR, "input[name='q']")
form.send_keys('abracadabra')

time.sleep(2)
search = browser.find_element(By.CSS_SELECTOR, "center > input[name='btnK']")
search.click()