from selenium import webdriver
import time
import math


def calc(xx):
    return str(math.log(abs(12*math.sin(int(xx)))))


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    # Считать значение для переменной x
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
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

    # Найдём элемент radiobutton
    people_radio = browser.find_element_by_id("peopleRule")

    # Найдём атрибут "checked" с помощью встроенного метода get_attribute
    # и проверим его значение:
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

    # Мы можем написать проверку другим способом, сравнив строки:
    assert people_checked == "true", "People radio is not selected by default"

    # Применим метод get_attribute ко второму radiobutton
    robots_radio = browser.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None

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
