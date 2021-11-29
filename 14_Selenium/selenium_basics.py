from selenium import webdriver
import time

driver = webdriver.Chrome('C:/Users/Ebubekir Dogan/Documents/GitHub/Python-Advance-Level/14 - Selenium/chromedriver') 


url = "http://github.com"
driver.get(url)

time.sleep(2)
driver.maximize_window()
driver.save_screenshot("github.com-homepage.png")

url = "http://github.com/ebubekirdgn"
driver.get(url)

print(driver.title)

if "ebubekirdgn" in driver.title:
    driver.save_screenshot("github-ebubekirdgn.png")

time.sleep(2)

driver.back()
# driver.forward()

time.sleep(2)

driver.close()

