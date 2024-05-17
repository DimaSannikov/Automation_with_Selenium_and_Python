# pytest -rx -v lesson_3_5_step_5_fixture_mark_as_XFail_reason_test.py -- не работает
# pytest -rE -v lesson_3_5_step_5_fixture_mark_as_XFail_reason_test.py
# pytest -v lesson_3_5_step_5_fixture_mark_as_XFail_reason_test.py
# pytest -rX -v lesson_3_5_step_5_fixture_mark_as_XFail_reason_test.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "button.favorite")
