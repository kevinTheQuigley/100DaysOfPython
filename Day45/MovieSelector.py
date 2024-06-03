from bs4 import BeautifulSoup
import lxml

import requests

movie_response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(movie_response.text, "html.parser")

res = soup.find_all("h3",class_="title")
print(res[0].getText())

with open("movie.txt","a",encoding = "utf-8") as output:
    for i in range(100):
        output.write(res[99-i].getText()+"\n")