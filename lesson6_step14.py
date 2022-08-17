from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
        link = "http://SunInJuly.github.io/execute_script.html"
        browser = webdriver.Chrome()
        browser.get(link)
        
        def calc(x):
            return str(math.log(abs(12*math.sin(int(x)))))
        # Ваш код, который заполняет обязательные поля
        x_element = browser.find_element(By.ID, "input_value")
        x = x_element.text
        y = calc(x)
        # Чтобы браузер проскроллил страницу вниз
        button = browser.find_element_by_tag_name("button")
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()
        # Ввести ответ в текстовое поле 
        element = browser.find_element(By.CSS_SELECTOR,"[class ='form-control']") 
        element.send_keys(y)
    
        # Ставим галочку I'm the robot
        checbox = browser.find_element(By.ID, "robotCheckbox")
        checbox.click()
        
        # Переключить radiobutton "Robots rule!
        radiobutton= browser.find_element(By.ID, "robotsRule")
        radiobutton.click()
        
        # Нажать на кнопку "Submit"
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        
        time.sleep(1)
	
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
    # закрываем браузер после всех манипуляций
        browser.quit()