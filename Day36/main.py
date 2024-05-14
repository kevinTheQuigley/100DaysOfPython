from arsewards import arsewards_dict
import requests
from datetime import datetime,timedelta
from pandas.tseries.offsets import BDay



APIKEY = arsewards_dict["alpha_vantage_API"] 
news_api = arsewards_dict["news_API"]
print(APIKEY)
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
the_number = arsewards_dict["the_number"]

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 

parameters1 = {
    "function" :"TIME_SERIES_INTRADAY",
    "symbol" : STOCK,
    "interval": "60min",
    "apikey": APIKEY
}



res = requests.get(url = "https://www.alphavantage.co/query",params = parameters1).json()



t1 = (datetime.now() - BDay(1)).strftime("%Y-%m-%d") + " 19:00:00"
t2 = (datetime.now() - BDay(2)).strftime("%Y-%m-%d") + " 19:00:00"
#print(res)
price1 = float(res["Time Series (60min)"][t1]["4. close"])
price2 = float(res["Time Series (60min)"][t2]["4. close"])
print(price2-price1)
parameters2 = {
    "q" :COMPANY_NAME,
    #"from" : (datetime.now() - BDay(1)).strftime("%Y-%m-%d") 
    "sortBy": "popularity",
    "apiKey": news_api 
}



if True:#(price2-price1)> 5:
    res = requests.get(url = "https://newsapi.org/v2/everything",params = parameters2).json()
    title1 = res["articles"][0]["title"]
    title2 = res["articles"][1]["title"]
    title3 = res["articles"][2]["title"]
    titles = "\n".join([title1,title2,title3])
    print(title1)


    import pywhatkit as kit

    the_number = arsewards_dict['the_number']

    message=(f"Yo!\nShit's going down in the market today. tesla stock price is down by {(price1-price2)/price2}\n"+
        titles)
    kit.sendwhatmsg_instantly(the_number, message,13, 12, 1)


"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

