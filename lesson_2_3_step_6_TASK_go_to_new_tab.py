from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

try:
    button = browser.find_element(By.CLASS_NAME, "trollface.btn.btn-primary")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    submit = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    submit.click()
    sleep(10)

except:
    sleep(10)
    browser.quit()