from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import random as rd
import time
from arsewards import arsewards_dict
from setuptools import distutils

import undetected_chromedriver as uc
from selenium_stealth import stealth
'''
options = webdriver.ChromeOptions() 
options.headless = True
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
'''


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
#options.add_argument("--headless")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )


#driver.get("https://bot.sannysoft.com/")
#chrome_options = Options()
#chrome_options.add_experimental_option("detach", True)
#driver = webdriver.Chrome(options=options)
#driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.get("https://chatgpt.com/auth/login")           


nav_button = driver.find_element(By.CSS_SELECTOR, ".relative button")
time.sleep(2)
nav_button.click()
time.sleep(10)
email_input = driver.find_element(By.CSS_SELECTOR, ".email-input")
time.sleep(2)
email_input.send_keys(arsewards_dict["kevinsHiddenEmail"] + Keys.ENTER)
time.sleep(2)
