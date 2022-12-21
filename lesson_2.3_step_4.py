import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get('http://suninjuly.github.io/alert_accept.html')

try:
    button1 = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button1.click()

    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element(By.ID, 'input_value').text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)

    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)
    time.sleep(1)
    button2 = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button2.click()

finally:
    time.sleep(10)
    browser.quit()