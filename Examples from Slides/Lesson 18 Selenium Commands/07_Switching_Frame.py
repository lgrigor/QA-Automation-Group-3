from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

chrome_options = Options()
chrome_options.add_argument('--headless')
#chrome_options.add_argument('--log-level=3')
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

browser = webdriver.Chrome('Selenium\driver\chromedriver_93.exe', options=chrome_options)
browser.get(r"C:\Users\Levon Grigoryan\Desktop\Visual Studio Code\Selenium_Commands\07_Frames.html")

browser.switch_to.frame('4th')
#browser.switch_to.frame(browser.find_element(By.XPATH, '//frame[4]'))

paragraphs = browser.find_elements(By.TAG_NAME, 'p')
print(f"Paragraphs on 4th frame - {len(paragraphs)}")

browser.switch_to.default_content()
frames = browser.find_elements(By.TAG_NAME, 'frame')
print(f"Frames on main page - {len(frames)}")