from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

try:
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    submit = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    submit.click()
    sleep(15)

except:
    sleep(15)
    browser.quit()
