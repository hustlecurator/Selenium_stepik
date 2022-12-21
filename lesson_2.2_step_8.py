import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/file_input.html')

try:
    button1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter first name"]')
    button1.send_keys('asd')
    button2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter last name"]')
    button2.send_keys('asd')
    button3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter email"]')
    button3.send_keys('asd')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test1.txt')
    f_import = browser.find_element(By.CSS_SELECTOR, '[type="file"]')
    f_import.send_keys(file_path)
    button4 = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button4.click()

finally:
    time.sleep(10)
    browser.quit()