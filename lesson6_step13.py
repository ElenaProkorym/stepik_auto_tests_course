from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
        link = "http://suninjuly.github.io/selects1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        
        # Находим первое заначение и переводим в число
        a_element = browser.find_element(By.ID, "num1")
        a = int(a_element.text)
        # Находим второе заначение и переводим в число
        b_element = browser.find_element(By.ID, "num2")
        b = int(b_element.text)
        # Находим сумму 
        x= a+b
        # Находим значение Х в выпадающем меню и кликаем по нему
        browser.find_element(By.CSS_SELECTOR, (f"[value='{x}']")).click()
        
        # Находим кнопку Select и кликаем по кнопке
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        
        time.sleep(1)
	
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
    # закрываем браузер после всех манипуляций
        browser.quit()