from bs4 import BeautifulSoup
import lxml

import requests

yc_response = requests.get("https://news.ycombinator.com/news")

soup = BeautifulSoup(yc_response.text, "html.parser")

res = soup.find_all("span",class_="titleline")
res2 = soup.find_all("span",class_="score")
articles = soup.find(name = "a",class_="storylink")
print(res[0].getText())
print(res2[0].getText())
print(res[0].get("href"))
numList = []
[numList.append(int(res2[j].getText().split()[0])) for j in range(len(res2))]
print(res[numList.index(max(numList))].select("a")[0].get("href"))
