from instagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Instagram:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome('C:/Users/Ebubekir Dogan/Documents/GitHub/Python-Advance-Level/14 - Selenium/chromedriver')
        self.username = username
        self.password = password
    
    
    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(1)
        
        usernameInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)

    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(1)
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(2)
        dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
        
        followerCount = len(dialog.find_elements_by_css_selector("li"))

        print(f"first count: {followerCount}")


instgrm = Instagram(username, password)
instgrm.signIn()
