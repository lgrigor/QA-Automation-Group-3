# Импорт Selenium WebDriver и By

from selenium import webdriver
from selenium.webdriver.common.by import By

# Открыть файл отчета, если его не существует, он будет создан.

total_price = open("total-price.txt", "a+", encoding="utf-8")

# Переменная для цикла прогонов

n = 1

# Цикл прогонов

while n <= 2:           # Указать количество циклов
    total_price.write(f"Прогон номер {n}\n________________________________________________\n\n")    # Записываем номер прогона

    # Указываем браузеры и их драйверы

    brsrEdge = webdriver.Edge("WebDriver\msedgedriver_94.exe")      # Microsoft Edge
    brsrChrome = webdriver.Chrome("WebDriver\chromedriver_94.exe")  # Google Chrome

    # Открываем страницу в браузерах

    brsrEdge.get("https://www.saucedemo.com/")      # Microsoft Edge
    brsrChrome.get("https://www.saucedemo.com/")    # Google Chrome

    # Записываем логин и пароль

    # Microsoft Edge
    login_credentials_Edge = brsrEdge.find_element(By.ID, "login_credentials")      # Записываем логины
    login_password_Edge = brsrEdge.find_element(By.CLASS_NAME, "login_password")    # Записываем пароли

    loginEdge = login_credentials_Edge.text.split()                                 # Добавляем логины в список
    passwordEdge = login_password_Edge.text.split()                                 # Добавляем пароли в список

    # Google Chrome
    login_credentials_Chrome = brsrChrome.find_element(By.ID, "login_credentials")      # Записываем логины
    login_password_Chrome = brsrChrome.find_element(By.CLASS_NAME, "login_password")    # Записываем пароли

    loginChrome = login_credentials_Chrome.text.split()                                 # Добавляем логины в список
    passwordChrome = login_password_Chrome.text.split()                                 # Добавляем пароли в список

    # Находим и заполняем поля логина и пароля

    # Microsoft Edge
    brsrEdge.find_element(By.ID, "user-name").send_keys(loginEdge[3])                   # Записываем логин
    brsrEdge.find_element(By.XPATH, "//*[@id='password']").send_keys(passwordEdge[4])   # Записываем пароль

    # Google Chrome
    brsrChrome.find_elements(By.TAG_NAME, "input")[0].send_keys(loginChrome[3])         # Записываем логин
    brsrChrome.find_elements(By.TAG_NAME, "input")[1].send_keys(passwordChrome[4])      # Записываем пароль

    # Выполняем вход

    brsrEdge.find_element(By.CSS_SELECTOR, "#login-button").click()     # Microsoft Edge
    brsrChrome.find_element(By.CSS_SELECTOR, "#login-button").click()   # Google Chrome

    # Добавляем товар в корзину и покупаем его

    # Microsoft Edge
    brsrEdge.find_element(By.PARTIAL_LINK_TEXT, "Bolt T-Shirt").click()             # Заходим на страницу товара
    brsrEdge.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()     # Добавляем в корзину
    brsrEdge.find_element(By.CLASS_NAME, "shopping_cart_badge").click()             # Заходим в корзину
    brsrEdge.find_element(By.ID, "checkout").click()                                # Нажимаем оплатить
    brsrEdge.find_element(By.ID, "first-name").send_keys("Papa")                    # Вводим имя покупателя
    brsrEdge.find_element(By.ID, "last-name").send_keys("Carlo")                    # Вводим фамилию покупателя
    brsrEdge.find_element(By.ID, "postal-code").send_keys("0070")                   # Вводим почтовый индекс покупателя
    brsrEdge.find_element(By.ID, "continue").click()                                # Переходим на страницу оплаты

    totalEdge = brsrEdge.find_element(By.CLASS_NAME, "summary_total_label")         # Сохраняем сумму заказа

    total_price.write(f"Цена в Microsoft Edge:\n{totalEdge.text} \n")                # Записываем сумму заказа в отчет

    brsrEdge.find_element(By.ID, "finish").click()                                  # Подтверждаем покупку

    lastmsgEdge = brsrEdge.find_element(By.CLASS_NAME, "complete-header")           # Сообщение об операции

    if lastmsgEdge.text == "THANK YOU FOR YOUR ORDER":                              # Если операция прошла успешно, записываем сообщение об этом
        total_price.write(f"Операция успешно завершена.\n\n")
    else:                                                                           # Если в ходе операции были ошибки, записываем их
        total_price.write(f"В ходе операции произошла ошибка.\n\nСообщение ошибки:\n{lastmsgEdge.text}\n\n")

    brsrEdge.close()            # Закрываем браузер Microsoft Edge

    # Google Chrome
    brsrChrome.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()            # С главной страницы добавляем первый товар в корзину
    brsrChrome.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()        # С главной страницы добавляем второй товар в корзину
    brsrChrome.find_element(By.CSS_SELECTOR, "#shopping_cart_container > a > span").click()         # Заходим в корзину
    brsrChrome.find_element(By.ID, "continue-shopping").click()                                     # Нажимаем на продолжить покупки
    brsrChrome.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-onesie']").click()           # С главной страницы добавляем третий товар в корзину
    brsrChrome.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div/div[6]/div[2]/div[2]/button").click()           # С главной страницы добавляем четвертый товар в корзину
    brsrChrome.find_element(By.CLASS_NAME, "shopping_cart_link").click()                            # Снова заходим в корзину
    brsrChrome.find_element(By.ID, "checkout").click()                                              # Нажимаем оплатить
    brsrChrome.find_element(By.ID, "first-name").send_keys("Papa")                                  # Вводим имя покупателя
    brsrChrome.find_element(By.ID, "last-name").send_keys("Carlo")                                  # Вводим фамилию покупателя
    brsrChrome.find_element(By.ID, "postal-code").send_keys("0070")                                 # Вводим почтовый индекс
    brsrChrome.find_element(By.ID, "continue").click()                                              # Переходим на страницу оплаты

    totalChrome = brsrChrome.find_element(By.CLASS_NAME, "summary_total_label")                     # Сохраняем сумму заказа

    total_price.write(f"Цена в Google Chrome:\n{totalChrome.text} \n")                               # Записываем сумму заказа в отчет

    brsrChrome.find_element(By.ID, "finish").click()                                  # Подтверждаем покупку

    lastmsgChrome = brsrChrome.find_element(By.CLASS_NAME, "complete-header")               # Сообщение об операции

    if lastmsgChrome.text == "BLABLABLA":                                  # Если операция прошла успешно, вывести сообщение об этом
        total_price.write(f"Операция успешно завершена.\n\n________________________________________________\n\n")
    else:
        total_price.write(f"В ходе операции произошла ошибка.\n\nСообщение ошибки:\n{lastmsgChrome.text}\n\n________________________________________________\n\n")           # Если в ходе операции были ошибки, вывести их

    brsrChrome.close()          # Закрываем браузер Google Chrome

    n += 1                      # Добавляем один прогон к переменной цикла