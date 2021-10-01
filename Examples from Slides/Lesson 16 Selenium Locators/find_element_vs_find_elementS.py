from selenium import webdriver

browser = webdriver.Chrome('Selenium\driver\chromedriver_93.exe')
browser.get(r"C:\Users\Levon Grigoryan\Desktop\Visual Studio Code\Selenium\03_page_source.html")

all_usernames = browser.find_elements_by_xpath("//input")

print('\n\n')

for each_username in all_usernames:
    print(each_username)

print('\n\n')

first_username = browser.find_element_by_xpath("//input")
print(first_username)

print('\n\n')