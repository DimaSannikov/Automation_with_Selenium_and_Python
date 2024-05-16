from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)
    num3 = num1 + num2

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(num3))

    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()
    time.sleep(15)

except:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()