from selenium import webdriver 
from selenium.webdriver.common.by import By 
import time
import math 

link="http://suninjuly.github.io/redirect_accept.html"

try:
    browser=webdriver.Chrome()
    browser.get(link)
    button=browser.find_element(By.CSS_SELECTOR,"button.btn")
    button.click()
    new_window=browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    
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
    time.sleep(10)
    browser.quit()