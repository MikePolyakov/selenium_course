from selenium import webdriver
import time
import math


def calc(xx):
    return str(math.log(abs(12*math.sin(int(xx)))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    # Найти картинку сундука с сокровищами
    chest_element = browser.find_element_by_id("treasure")

    # Считать значение для переменной x
    x = chest_element.get_attribute("valuex")
    print(x)

    # Посчитать математическую функцию от x
    y = calc(x)
    print(y)

    # Ввести ответ в текстовое поле
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    # Отметить checkbox "I'm the robot"
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    # Выбрать radiobutton "Robots rule!"
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()

    # Нажать на кнопку Submit
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
