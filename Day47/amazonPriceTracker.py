import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import smtplib
from arsewards import arsewards_dict
import random
import pandas
#globals




url = "https://www.amazon.co.uk/gp/product/B0BN1W3JMF/ref=ox_sc_act_title_1?smid=A1KDIF4S4TI05O&psc=1"
#url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

my_header = {
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8"
    #"Accept"    : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
}

def get_amazon_item_soup(product_url):
    request_headers = {
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    ua = UserAgent(browsers=['edge', 'chrome'])
    user_agent = ua.random

    while True:
        request_headers["User-Agent"] = user_agent
        product_page = requests.get(product_url, headers=request_headers).text

        if "api-services-support@amazon.com" in product_page:
            user_agent = ua.random

        else:
            return BeautifulSoup(product_page, "html.parser")

soup = get_amazon_item_soup(url)

'''
item_prices = soup.findAll(name="span", class_="a-price")

#response = requests.get(url, headers=my_header)

if len(item_prices) > 0:
    target_price = item_prices[0]
    price = int(target_price.find(class_="a-price-whole").next_element) + int(
        target_price.find(class_="a-price-fraction").text) / 100

    print(price)

else:
    print("Item price not found")


'''
item_prices = soup.find(name="span", class_="aok-offscreen").get_text()
item_price = float(item_prices.replace("£",""))
target_price = 35


my_email = "KevinsFancyTester12@gmail.com"
destination_email = arsewards_dict["kevinsHiddenEmail"]
password =   arsewards_dict[my_email]
gmPass = arsewards_dict["KevinsFancyGmAppPassword"]
gmail_link = "smtp.gmail.com"

if item_price < target_price:
    print("Target price reached")
    with  smtplib.SMTP(host = gmail_link) as connection:
        body = "Yay! The price limit has been reached. Please log on to check it out"
        connection.starttls()
        connection.login(user= my_email, password = gmPass)
        connection.sendmail(msg = f"Subject:Amazon price tracking \n\n{body}", from_addr=my_email, to_addrs=destination_email)
        connection.close()
    

