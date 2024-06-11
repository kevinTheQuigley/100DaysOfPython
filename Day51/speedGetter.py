import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from arsewards import arsewards_dict
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def getInternetSpeed():
    options = ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    #chrome_options = Options()
    #chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    #driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    driver.get("https://www.speedtest.net/")

    time.sleep(2)
    nav_button = driver.find_element(By.CSS_SELECTOR, "#onetrust-reject-all-handler")
    nav_button.click()
    go_button = driver.find_element(By.CSS_SELECTOR,".js-start-test")
    go_button.click()
    time.sleep(50)
    down_speed = driver.find_element(By.CSS_SELECTOR,".download-speed")
    dS = float(down_speed.text)
    print (dS)
    up_speed = driver.find_element(By.CSS_SELECTOR,".upload-speed")
    print (up_speed.text)
    uS = float(up_speed.text)
    print (uS)

    driver.close()
    return(dS,uS)

print(getInternetSpeed())