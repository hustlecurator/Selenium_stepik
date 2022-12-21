import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

message = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
button1 = browser.find_element(By.CSS_SELECTOR, 'button.btn')
button1.click()

x = browser.find_element(By.ID, 'input_value').text


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


y = calc(x)

input_field = browser.find_element(By.ID, "answer")
input_field.send_keys(y)
time.sleep(1)

button2 = browser.find_element(By.ID, 'solve')
button2.click()

time.sleep(10)
