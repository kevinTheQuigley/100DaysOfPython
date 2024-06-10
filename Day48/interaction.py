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
driver.get("https://en.wikipedia.org/wiki/Main_Page")

articlecount = driver.find_element(By.CSS_SELECTOR,value = '#articlecount a') 
print(articlecount.text)
#intCount = articlecount.find_element(By.XPATH,value = ".//a").text()

driver.quit()