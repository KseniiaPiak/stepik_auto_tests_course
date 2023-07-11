from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    # используем метод get для открытия ссылки
    browser.get("http://suninjuly.github.io/huge_form.html")
    # используем метод find_elements для поиска множества элементов
    elements = browser.find_elements(By.TAG_NAME, "input")
    # создаем цикл для заполнения полей найденных элементов
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

