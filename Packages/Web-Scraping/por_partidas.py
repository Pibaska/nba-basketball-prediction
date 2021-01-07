import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
option = Options()
option.headless = True
driver = webdriver.Firefox(firefox_binary=binary,executable_path=r'C:\\geckodriver.exe')



url = "https://www.basketball-reference.com/boxscores/?month=5&day=3&year=2019"

xPathTabela = ""    

nomeArquivo =  "partidas" 
nomeDicionario = "partidas_2019-05-"
dicionario = {}



#Descobre quantas partidas o site tem do dia escolhido
def neoContadorDePartidas():
    element = driver.find_element_by_xpath('//*[@id="content"]/div[3]')
    html_content = element.get_attribute('outerHTML')
    soup = BeautifulSoup(html_content, 'html.parser')

    qtdPartidas = soup.find_all("div", {"class": "game_summary expanded nohover"}) # pega só divs que tenham tal classe
    qtd = len(qtdPartidas)

    return qtd


driver.get(url)

qtdPartidas = neoContadorDePartidas()

print('No dia escolhido ocorreram: ' + str(qtdPartidas) + ' partidas')

