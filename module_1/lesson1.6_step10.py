from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # используем максимально уникальный селектор от родителя к дочернему элементу с выделением по классам и названию тегов
    firstName = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.first_class > input.form-control.first")
    firstName.send_keys("Kseniia")

    lastName = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.second_class > input.form-control.second")
    lastName.send_keys("Piak")

    email = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.third_class > input.form-control.third")
    email.send_keys("kseniia.piak@mail.ru")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    # находим элемент по названию тега
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # получаем текст найденного элемента с помощью свойства text
    welcome_text = welcome_text_elt.text

    # вызываем функцию assert для проверки условия. Если условие не выполняется - выбрасывается ошибка
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
