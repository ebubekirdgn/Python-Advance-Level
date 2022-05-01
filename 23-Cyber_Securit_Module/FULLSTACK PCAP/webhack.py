# Selenium kütüphanesini kurmak için
# pip install selenium

# web driver kurulumları için
# https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
# işletim sistemine göre web driver yüklendikten sonra
# gerekli ortam değişkeni tanımlamaları yapılmalıdır


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox() # kullanacağımız driver
driver.get('https://www.github.com/login')  # hedef web sitesi

# deneyeceğimiz kullanıcı adı ve şifre
username = 'deneme'
password = 'deneme'

# sayfadaki form elemanlarını yakalayalım
username_input = driver.find_element_by_name('login')
password_input = driver.find_element_by_name('password')
login = driver.find_element_by_name('commit')

# sayfadaki form elemanları temizleyelim
username_input.clear()
password_input.clear()

# belirlediğimiz kullanıcı adı ve şifreyi forma ekleyelim
# süreci görebilmeniz için time kodu eklenmiştir
# gerçek kullanımda time.sleep(5) komutunu kaldırabilirsiniz
username_input.send_keys(username)
time.sleep(5)
password_input.send_keys(password)
time.sleep(5)
login.click()
