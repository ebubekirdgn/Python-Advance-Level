from twitterUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Twitter:
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome('C:/Users/Ebubekir Dogan/Documents/GitHub/Python-Advance-Level/14 - Selenium/chromedriver', chrome_options=self.browserProfile)
        self.username = username
        self.password = password
    
    def singIn(self):
        self.browser.get("https://twitter.com/login")
        time.sleep(2)

        usernameInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)

        btnSubmit =  self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div")

        btnSubmit.click()
 
        time.sleep(2)
    def search(self , hashtag):
        searchInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input")
        searchInput.send_keys(hashtag)
        searchInput.send_keys(Keys.ENTER)
        time.sleep(2)

        list = self.browser.find_elements_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]")
        for item in list:
            print(len(list))
            print("*************")
            print(item.text)
        

       
        last_height= self.browser.execute_script("return document.documentElement.scrollHeight")
        loopCounter=0

        while True:
            if loopCounter > 5:
                break
            self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
            time.sleep(2)
            new_height = self.browser.execute_script("return document.documentElement.scrollHeight")
            if last_height == new_height:
                break
            last_height = new_height
            loopCounter+=1
        
     
        # time.sleep(2)
        # print("count: "+ str(len(list)))

twitter = Twitter(username,password)
# login
twitter.singIn()
twitter.search("python")