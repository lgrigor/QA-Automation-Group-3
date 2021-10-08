from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--log-level=3')
#chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

browser = webdriver.Chrome('Selenium\driver\chromedriver_93.exe', options=chrome_options)
browser.get("https://www.google.com/")

print(f'The title is {browser.title}')
assert browser.title == 'Gooogle', 'Error: Google page was not loaded!'