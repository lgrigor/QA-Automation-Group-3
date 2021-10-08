from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

FIRST_SCREENSHOT = r'Selenium_Commands\Screenshots\home_page.png'
SECOND_SCREENSHOT = r'Selenium_Commands\Screenshots\random_video.png'

chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--log-level=3')
chrome_options.add_argument("--start-maximized")

browser = webdriver.Chrome('Selenium\driver\chromedriver_93.exe', options=chrome_options)
browser.get('https://www.youtube.com/')
browser.set_page_load_timeout(10)

browser.save_screenshot(FIRST_SCREENSHOT)
browser.find_element(By.XPATH, '//yt-img-shadow/img[@width="9999"]').click()

wait = WebDriverWait(browser, 5)
wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='ytp-time-current' and text()='0:01']")))
browser.save_screenshot(SECOND_SCREENSHOT)
browser.quit()
