from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--log-level=3')
chrome_options.add_argument("--start-maximized")

browser = webdriver.Chrome('Selenium\driver\chromedriver_93.exe', options=chrome_options)
browser.get('https://ezgif.com/webp-to-jpg')
browser.set_page_load_timeout(10)

browser.find_element(By.ID, "new-image").send_keys(r"C:\Users\Levon Grigoryan\Desktop\Visual Studio Code\Selenium_Commands\15_Capturing_Screenshots.py")

browser.quit()
