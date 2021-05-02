from urllib.request import Request, urlopen
import requests

import re,csv

import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions

BASE_URL = 'https://www.globo.com/busca/?q='
ROLL = 4

def get_html(palavra_busca):
    options = FirefoxOptions()
    #options.add_argument("--headless")
    driver = webdriver.Firefox(executable_path=r'D:\geckodriver.exe',options=options)
    driver.get(BASE_URL+palavra_busca)

    SCROLL_PAUSE_TIME = 1

    last_height = driver.execute_script("return document.body.scrollHeight")

    i =0
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(SCROLL_PAUSE_TIME)


        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height or i > ROLL:
            break
        i+=1
    last_height = new_height
    return driver.page_source

def salvar(titulo, link, text):
    r = requests.post("https://backend-hack-grrrl.herokuapp.com/news", json={'title': titulo, 'link': link, 'text': text})
    print(r.status_code, r.reason)



palavras_pesquisa = ['propaganda','mulher']

palavras_chave = ["machista", "feminista", "gênero", "representatividade","igualdade", "diversidade", "pink tax"]

for p in palavras_pesquisa:
    soup = BeautifulSoup(get_html(p), 'html.parser')

    news = soup.find_all(class_='widget widget--card widget--info')

    titulo = ""
    link = ""
    texto= ""
  
    for item in news:
        try:
            titulo = item.find(class_='widget--info__title').contents[0].strip()
            link = "https:"+item.find('a')['href']
            texto = item.find(class_='widget--info__description').contents[0].strip()
            noticia_valida = False
            for palavra in palavras_chave:
               if(palavra in titulo or palavra in texto):
                   noticia_valida = True
                   break
            if(noticia_valida):
                print()
                print(titulo)
                print(link)
                print(texto)
                #salvar(titulo, link, texto)
        except:
            continue

        

