from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/simple_form_find_task.html"

# try/finally - позволяет выполнить код в finally при наличии ошибок в try
try:
    # создаем (инициализируем) объект класса Chrome
    browser = webdriver.Chrome()
    # открываем страницу браузера
    browser.get(link)

    # находим элемент по названию тега
    input1 = browser.find_element(By.TAG_NAME, "input")
    # эмитируем нажатие клавиши (вводим текст Ivan)
    input1.send_keys("Ivan")
    # находим элемент по аттрибуту name
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    # находим элемент по аттрибуту class
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    # находим элемент по его id
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    # находим элемент с помощью css_selector
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # используем метод sleep из модуля time для ожидания перед выполнением кода
    time.sleep(30)
    # используем метод quit для выхода 
    browser.quit()

