import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/selects1.html')

x = browser.find_element(By.ID, "num1").text
y = browser.find_element(By.ID, "num2").text
a = int(x) + int(y)

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(str(a))
time.sleep(3)

btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
btn.click()

time.sleep(10)