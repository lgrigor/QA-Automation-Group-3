from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--log-level=3')

browser = webdriver.Chrome('Selenium\driver\chromedriver_93.exe', options=chrome_options)
browser.get("https://www.google.com/")

form = browser.find_element(By.CSS_SELECTOR, "input[name='q']")
form.send_keys('abracadabra')
form.send_keys(Keys.TAB)

time.sleep(1)
form.clear()
