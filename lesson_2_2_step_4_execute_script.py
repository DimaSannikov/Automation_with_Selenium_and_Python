from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()
# browser.execute_script("alert('Robots at work');")
browser.execute_script("document.title='Script executing';alert('Robots at work');")
sleep(5)
browser.quit()