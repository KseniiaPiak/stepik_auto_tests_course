from selenium import webdriver
from selenium.webdriver.common.by import By
from os.path import abspath, dirname, join
import time

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    inputs = browser.find_elements(By.CSS_SELECTOR, "input[type='text']")
    for el in inputs:
    	el.send_keys("Ksu")

    attachment = browser.find_element(By.ID, "file")
    current_dir = abspath(dirname(__file__))
    file_path = join(current_dir, "file.txt")
    attachment.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()