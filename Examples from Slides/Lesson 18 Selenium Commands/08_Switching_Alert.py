from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
import time

chrome_options = Options()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--log-level=3')
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

browser = webdriver.Chrome('Selenium\driver\chromedriver_93.exe', options=chrome_options)
browser.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")

browser.find_element(By.ID, "promptexample").click()

alert_obj = browser.switch_to.alert

time.sleep(1)
print(f"Text in alert - {alert_obj.text}")

time.sleep(1)
alert_obj.send_keys('Levon Grigoryan')

time.sleep(1)
alert_obj.accept()
#alert_obj.dismiss()
