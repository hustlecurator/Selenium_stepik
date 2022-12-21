import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get('http://suninjuly.github.io/redirect_accept.html')

try:
    button1 = browser.find_element(By.CSS_SELECTOR, 'button.trollface')
    button1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.ID, 'input_value').text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)

    field = browser.find_element(By.ID, 'answer')
    field.send_keys(y)

    button2 = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button2.click()

finally:
    time.sleep(10)
    browser.quit()