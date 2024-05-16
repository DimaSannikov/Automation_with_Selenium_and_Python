"""Explicit Waits (WebDriverWait и expected_conditions)"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait                 # Explicit Waits (WebDriverWait и expected_conditions)
from selenium.webdriver.support import expected_conditions as EC        # Explicit Waits (WebDriverWait и expected_conditions)

browser = webdriver.Chrome()

# говорим WebDriver искать каждый элемент в течение 5 секунд
# browser.implicitly_wait(5)                                              # Selenium Waits (Implicit Waits)

browser.get("http://suninjuly.github.io/wait2.html")

button = browser.find_element(By.ID, "verify")                          # Selenium Waits (Implicit Waits)
# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify")))                  # Explicit Waits (WebDriverWait и expected_conditions)
button.click()
# говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
button = WebDriverWait(browser, 5).until_not(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text
