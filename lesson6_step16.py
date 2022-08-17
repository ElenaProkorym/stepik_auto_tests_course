from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(0)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    #Ввести ответ в текстовое поле 
    element = browser.find_element(By.CSS_SELECTOR,"[class ='form-control']") 
    element.send_keys(y)
    # Нажать Submit
    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button1.click()
        
   
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()  