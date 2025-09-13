import requests
import bs4

url = "https://quotes.toscrape.com/" 

quotes = requests.get(url)
soup = bs4.BeautifulSoup(quotes.text, "html.parser")

frases = soup.find_all("div", class_="quote")

for div in frases:
    texto = div.find("span", class_="text").text
    with open("frases.txt", "a") as arquivo:
        arquivo.write(f"{texto} \n\n")
         