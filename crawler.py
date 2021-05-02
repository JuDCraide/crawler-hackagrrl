from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome('C:\Program Files (x86)/chromedriver.exe')
driver.get("https://gauchazh.clicrbs.com.br/ultimas-noticias/tag/feminismo/")

lst_elementos_xpath = driver.find_elements_by_xpath('/html/body/div[5]/div/div[2]/div[2]/main/section/div[1]/div/section[1]/div[2]/div/ul/*//div[@class="article-calls"]/h2')
lst_links_xpath = driver.find_elements_by_xpath('/html/body/div[5]/div/div[2]/div[2]/main/section/div[1]/div/section[1]/div[2]/div/ul/li/a')

lst_palavras_chave = [
      'Dove',
    'Skol',
    'Itaipava',
    'Avon',
    'Natura',
    'OBoticario',
    'Eudora',
    'Empoderamento',
    'Feminismo',
    'Diversidade',
    'Inclusão',
    'Racismo',
    'Objetificação',
]

lst_links_crawler = []

i = 0
for elemento in lst_elementos_xpath:
    titulo_noticia = elemento.get_attribute("innerText").splitlines()[0]
    link_noticia = lst_links_xpath[i].get_attribute("href").splitlines()[0]

    for palavra_chave in lst_palavras_chave:
        if palavra_chave in titulo_noticia:
            lst_links_crawler.append(link_noticia)

    i += 1

for link in lst_links_crawler:
    driver.get(link)
    print(link)
    try:
        lst_materias = driver.find_elements_by_xpath('//*/div[@class="article-paragraph"]/p')
        texto_materia = lst_materias[0].get_attribute("innerText")
        print(texto_materia)
    except:
        pass
driver.close()