import bs4
import requests
import os

'''
exist_ok=True = verificar se a pasta ja existe se existir não vai dar erro 
'''
os.makedirs('XKCD', exist_ok=True) # Makedirs cria pasta 

for i in range(1,10):
    url = "https://xkcd.com/" + str(i)# grava a url do site
    xkcd = requests.get(url) # importa o código html do site 
    xkcd.raise_for_status()

    soup = bs4.BeautifulSoup(xkcd.text, "html.parser") # converte o site em html

    comic_elem = soup.select("#comic img")[0] # localiza o id comic e a tag img 
    comic_url = "http:" + comic_elem.get("src")

    print(f"baixando a imagem {comic_url}...") # aviso de download da url 

    res = requests.get(comic_url)
    res.raise_for_status

    image_file = os.path.join("XKCD", os.path.basename(comic_url))
    with open (image_file, "wb") as f:
        f.write(res.content)

    print(f"imagem salva em {image_file}")