
from selenium import webdriver
import time

driver = webdriver.Chrome('C:/Users/Ebubekir Dogan/Documents/GitHub/Python-Advance-Level/14 - Selenium/chromedriver') 

url:"https://github.com"
driver.get(url)


time.sleep(2)
driver.maximize_window()
print(driver.title)

time.sleep(2)
driver.close()