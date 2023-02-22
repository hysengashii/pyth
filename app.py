
import requests
from bs4 import BeautifulSoup

url = "https://klankosova.tv/lajme/"


response = requests.get(url)


soup = BeautifulSoup(response.content, "html.parser")


article_content = soup.find("div", class_="col-xl-4 col-lg-5 col-md-6 col-sm-12 col-12")


article_text = article_content.get_text().strip()


with open("123", "w", encoding="utf-8") as file:
    file.write(article_text)

print("Article saved to file.")