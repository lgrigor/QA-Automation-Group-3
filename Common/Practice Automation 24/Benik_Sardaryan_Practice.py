import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--log-level=3")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

driver.get("http://practice.automationtesting.in/")

driver.implicitly_wait(10)

driver.find_element(By.ID, "menu-item-40").click()

driver.find_element(By.LINK_TEXT, "Home").click()

Arrivals = driver.find_elements(By.TAG_NAME, "h3")


assert len(Arrivals) == 3, "Число Arrivals не соответствует трем"    


driver.find_element(By.XPATH, "//*[@id='text-22-sub_row_1-0-2-0-0']/div//img").click()

Selenium_Ruby_link = driver.current_url

assert Selenium_Ruby_link == "http://practice.automationtesting.in/product/selenium-ruby/", "Ссылка для страницы Selenium Ruby на главной странице не верная."


driver.find_element(By.TAG_NAME, "button").click()

basket_item = driver.find_element(By.XPATH, "//*[@id='wpmenucartli']/a/span[1]")

assert basket_item.text == "1 Item", "Товар не добавлен в корзину."


driver.find_element(By.ID, "wpmenucartli").click()

Subtotal = driver.find_element(By.XPATH, "//*[@id='page-34']/div/div[1]/div/div/table/tbody/tr[1]/td/span")
Total = driver.find_element(By.XPATH, "//*[@id='page-34']/div/div[1]/div/div/table/tbody/tr[3]/td/strong/span")

Subtotal_int = Subtotal.text[1:]
Total_int = Total.text[1:]

assert float(Subtotal_int) < float(Total_int), "Subtotal больше или равно значению Total."


driver.find_element(By.XPATH, "//*[@id='page-34']/div/div[1]/div/div/div/a").click()



Billing_Details = driver.find_element(By.XPATH, "//*[@id='customer_details']/div[1]/div/h3")
Additional_Information = driver.find_element(By.XPATH, "//*[@id='customer_details']/div[2]/div/h3")
Your_order = driver.find_element(By.ID, "order_review_heading")
Payment = driver.find_element(By.ID, "payment")

assert Billing_Details, "Информация платежных реквизитах отсутствует"
assert Additional_Information, "Информация о дополнительной информации отсутствует"
assert Your_order, "Информация о заказе отсутствует"
assert Payment, "Возможность выбора платежной системы отсутствует"


driver.find_element(By.ID, "billing_first_name").send_keys("Burunduk")
driver.find_element(By.ID, "billing_last_name").send_keys("Barsukov")
driver.find_element(By.ID, "billing_email").send_keys("barsukov.burunduk@woo.com")
driver.find_element(By.ID, "billing_phone").send_keys("+12345678900")
driver.find_element(By.ID, "billing_address_1").send_keys("Forest")
driver.find_element(By.ID, "billing_city").send_keys("Forest city")
driver.find_element(By.ID, "billing_state").send_keys("California")
driver.find_element(By.ID, "billing_postcode").send_keys("0000")
driver.find_element(By.ID, "payment_method_cheque").click()
driver.find_element(By.ID, "place_order").click()


Order_Number = driver.find_element(By.CLASS_NAME, "order")
Order_Details = driver.find_element(By.XPATH, "//*[@id='page-35']/div/div[1]/h2")
Payment_Method = driver.find_element(By.CLASS_NAME, "method")

assert Order_Number, "Номера заказа не отображается"
assert Order_Details, "Детали заказа не отображаются"
assert Payment_Method, "Метод оплаты не отображается"


time.sleep(5)

driver.quit()