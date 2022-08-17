from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    
    
     # Ваш код, который заполняет обязательные поля
    element1 = browser.find_element(By.NAME,"firstname")
    element1.send_keys("Елена")
    element2 = browser.find_element(By.NAME,"lastname")
    element2.send_keys("Иванова")
    element3 = browser.find_element(By.CSS_SELECTOR,"[placeholder='Enter email'][required]")
    element3.send_keys("qa@gmail.com")
    
    # Загрузка файла
    current_dir=os.path.abspath(os.path.dirname('__file__'))
    file_name="Text.txt"
    file_path=os.path.join(current_dir,file_name)
    element=browser.find_element(By.CSS_SELECTOR,"[type='file']")
    element.send_keys(file_path)
   
    time.sleep(2)
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()  