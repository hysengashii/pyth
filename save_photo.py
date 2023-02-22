from bs4 import BeautifulSoup
import requests
import os


if not os.path.exists('book_images'):
    os.makedirs('book_images')

r = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(r.content, "html.parser")
thumbnail_elements = soup.find_all("img", class_="thumbnail")

for element in thumbnail_elements:
    img_url = element['src']
    
    filename = os.path.join('book_images', img_url.split('/')[-1])
    
    with open(filename, 'wb') as f:
        f.write(requests.get('https://books.toscrape.com/' + img_url).content)
        print(f'Saved {filename}')