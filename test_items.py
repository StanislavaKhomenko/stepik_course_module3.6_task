from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button_presence(browser):
    browser.get(link)
    button = browser.find_elements(By.CSS_SELECTOR, "button[class='btn btn-lg btn-primary btn-add-to-basket']")
    assert button, "Add to Basket button is absent on the page"
