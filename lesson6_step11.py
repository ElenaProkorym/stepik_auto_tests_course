from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
        link = "http://suninjuly.github.io/math.html"
        browser = webdriver.Chrome()
        browser.get(link)
        
        def calc(x):
            return str(math.log(abs(12*math.sin(int(x)))))
        # Ваш код, который заполняет обязательные поля
        x_element = browser.find_element(By.ID, "input_value")
        x = x_element.text
        y = calc(x)
        element = browser.find_element(By.CSS_SELECTOR,"[class ='form-control']") 
        element.send_keys(y)
    
        # Ставим галочку I'm the robot
        checbox = browser.find_element(By.ID, "robotCheckbox")
        checbox.click()

        radiobutton= browser.find_element(By.ID, "robotsRule")
        radiobutton.click()
        
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
	
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
    # закрываем браузер после всех манипуляций
        browser.quit()