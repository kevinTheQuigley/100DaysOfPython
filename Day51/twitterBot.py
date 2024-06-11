import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from arsewards import arsewards_dict
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = ChromeOptions()
options.add_experimental_option("detach", True)

class TwitterBot():
    def __init__(self,up,down) :
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://x.com/login")
        self.driver.maximize_window()
        time.sleep(5)
        email_input = self.driver.find_element(By.CSS_SELECTOR,".r-30o5oe")
        email_input.send_keys(arsewards_dict["kevinsHiddenEmail"],Keys.ENTER)
        next_button = self.driver.find_element(By.CSS_SELECTOR,".css-175oi2r")
        next_button.click()

        time.sleep(5)
        pass_input = self.driver.find_elements(By.CSS_SELECTOR,".r-30o5oe")
        pass_input[1].send_keys(arsewards_dict["twitterAss"],Keys.ENTER)



        
        self.up = up
        self.down = down
    
    def getInternetSpeed(self):
        

    def tweet_at_provider(self):
        pass


tweeter = TwitterBot(50,150)

time.sleep(5)

