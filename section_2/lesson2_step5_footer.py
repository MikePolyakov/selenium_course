from selenium import webdriver

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

# футер перекрывает нужную нам кнопку
# button = browser.find_element_by_tag_name("button")
# button.click()

button = browser.find_element_by_tag_name("button")
# проскроллить нужный элемент, чтобы он точно стал видимым
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

# команда проскроллит страницу на 100 пикселей вниз:
browser.execute_script("window.scrollBy(0, 100);")

assert True
