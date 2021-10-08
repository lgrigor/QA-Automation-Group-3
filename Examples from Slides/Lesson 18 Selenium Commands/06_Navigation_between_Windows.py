from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--log-level=3')
chrome_options.add_argument("--start-maximized")

browser = webdriver.Chrome('Selenium\driver\chromedriver_93.exe', options=chrome_options)
browser.get(r"C:\Users\Levon Grigoryan\Desktop\Visual Studio Code\Selenium_Commands\06_Page_Source.html")

source_page = browser.current_window_handle
browser.find_element(By.TAG_NAME, 'a').click()

ref_page = browser.current_window_handle

time.sleep(2)
browser.switch_to.window(source_page)
time.sleep(2)
browser.switch_to.window(ref_page)

for handle in browser.window_handles:
    print(handle)