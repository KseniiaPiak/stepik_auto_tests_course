from selenium import webdriver
from math import *
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(log(abs(12*sin(int(x)))))

try:
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/explicit_wait2.html")

	WebDriverWait(browser, 13).until(
		EC.text_to_be_present_in_element((By.ID, "price"), "$100")
	)

	button = browser.find_element(By.ID, "book")
	button.click()

	num = browser.find_element(By.ID, "input_value")
	x = num.text

	result = calc(x)
	input = browser.find_element(By.ID, "answer")
	input.send_keys(result)

	button = browser.find_element(By.ID, "solve")
	button.click()

finally:
	sleep(10)
	browser.quit()