import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_is_there_add_to_basket_btn(browser):
    browser.get(link)
    time.sleep(30)
    add_to_basket_btn = browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form > button")
    assert add_to_basket_btn
