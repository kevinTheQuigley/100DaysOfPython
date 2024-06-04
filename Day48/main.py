from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

#chrome_options = Options()
#chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
#driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.get("https://www.python.org/")

dateList = driver.find_elements(By.XPATH,value = '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[*]')

driver.quit()