from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import unittest

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

def form(link):
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    input2.send_keys("Ivanov")
    input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    input3.send_keys("IvanIvanov@mail.ru")
    
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # находим элемент, содержащий текст
    welcome_text_elt = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1")))
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью self.assertEqual() проверяем, что ожидаемый текст совпадает с текстом на странице сайта+
    return welcome_text


class TestForm(unittest.TestCase):
    def test_form1(self):
        self.assertEqual("Congratulations! You have successfully registered!", form(link1), "Registration wasn't successful")

    def test_form2(self):
        self.assertEqual("Congratulations! You have successfully registered!", form(link2), "Registration wasn't successful")

if __name__ == "__main__":
    unittest.main()
