import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(params=['chrome'])
def setUp(request):
    if request.param == 'chrome':
        chrome_options = Options()
        chrome_options.add_argument('--log-level=3')
        chrome_options.add_argument('--start-maximized')
        browser = webdriver.Chrome(ChromeDriverManager().install(), options = chrome_options)
        
    return browser