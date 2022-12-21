import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/execute_script.html')

try:
    x = browser.find_element(By.ID, "input_value").text


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    input_field = browser.find_element(By.ID, "answer").send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, "[type='checkbox']").click()

    browser.execute_script("window.scrollBy(0, 150);")
    option2 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']").click()

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


finally:
    time.sleep(5)
    browser.quit()