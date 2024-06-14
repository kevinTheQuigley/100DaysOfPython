import time 
from bs4 import BeautifulSoup
import lxml
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



FORM_URL= "https://docs.google.com/forms/d/e/1FAIpQLSePbKxKiLic4DbnNLdK1F7E0XgZaqu7Q5yGWEcvqT0x3_ht8g/viewform?usp=sf_link"
ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone"
zi_response = requests.get(ZILLOW_URL)

#soup = BeautifulSoup(FORM_URL)




soup = BeautifulSoup(zi_response.text, "html.parser")

songTitle= soup.select("li ul li h3")
addresses= soup.select("div div a address")
songTitles = []
songArtists = []



items = soup.find_all( "span",class_="PropertyCardWrapper__StyledPriceLine")
links = soup.find_all( "a",class_="StyledPropertyCardDataArea-anchor")



#res2 = soup.find_all("span",class_="score")


options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

#chrome_options = Options()
#chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
#driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.get(FORM_URL)

entries = driver.find_elements(By.CSS_SELECTOR,".whsOnd")
print(len(entries))

for entry in entries:
    entry.send_keys("hi")
    print(entry.text)

time.sleep(5)
driver.quit()