from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get(" http://suninjuly.github.io/explicit_wait2.html")
    
    # говорим Selenium проверять в течение 12 секунд, пока появится цена $100
    message = WebDriverWait(browser, 12).until(        
        EC.text_to_be_present_in_element((By.ID,"price"),"$100") 
    )       
    #assert "100" in message.text 
    button= browser.find_element(By.ID, "book")
    button.click()
    
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
    button1 = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);",button1)
    button1.click()
    
finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit() 