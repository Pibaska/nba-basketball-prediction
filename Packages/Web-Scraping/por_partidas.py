
# Para rodar esse script: -------------------------------------------------------
# baixe geckodriver e o coloque em " C:\\Geckodriver\\geckodriver.exe "
#        https://github.com/mozilla/geckodriver/releases  
# baixe o firefox
# -------------------------------------------------------------------------
# berb esteve aqui

import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


# url = "https://www.basketball-reference.com/boxscores/?month=5&day=4&year=2020" #url da tela de partidas
# nomeArquivo =  "partidas" #arquivo .json
# nomeDicionarioAno = "partidas_x" #nome que vai se alterar por dia
# nomeDicionarioDia = "partidas_x/x/x" #nome que vai se alterar por dia
dicionario = {}
diasNosMeses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def SetupDriver(mostra):
    binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
    option = Options()
    option.headless = mostra
    driver = webdriver.Firefox(
        firefox_binary=binary, executable_path=r'C:\\Geckodriver\\geckodriver.exe', options=option) #https://github.com/mozilla/geckodriver/releases <- baixe de acordo
    return driver    

def TodoDia(driver):
    listaDaData = []
    listaDasDatas = []
    for ano in range(20):
        # calcula se é ano bissexto
        trueAno = 2000 + ano
        bissexto = 1 if (trueAno % 4 == 0 and (trueAno %
                                            400 == 0 or trueAno % 100 != 0)) else 0  # opeador ternário

        for mes in range(12):
            rangeDias = diasNosMeses[mes]

            rangeDias += bissexto if (rangeDias == 28) else 0

            for dia in range(rangeDias):
                listaDaData = [dia+1, mes+1, trueAno]
                listaDasDatas.append(listaDaData)

    return listaDasDatas      

#recebendo os dias, navega pelo site e entra nos jogos
def PuxaJogosDoDia(driver, listaDaData):
    # aqui é onde ce vai fazer os processo pesado. (no fim é onde tu vai chamar um monte de função)
    dia = listaDaData[0]
    mes = listaDaData[1]
    ano = listaDaData[2]
    # cria e chama a url
    url = f"https://www.basketball-reference.com/boxscores/?month={mes}&day={dia}&year={ano}"   

    return(url)

# entra no box score e filtra pelo primeiro quarto
def EntraNoBoxScore(driver, url, i):  

    driver.get(url) if i > 0 else 0
    # entra no box-score do jogo
    driver.find_element_by_xpath(
        f'//*[@id="content"]/div[3]/div[{i+1}]/p/a[1]').click()

    # Para apresentar apenas 1°quarto
    driver.find_element_by_xpath(
        f'//*[@id="content"]/div[6]/div[2]/a').click()



# Retorna quantas partidas o site tem do dia escolhido
def ContadorDePartidas(driver):
    element = driver.find_element_by_xpath(
        '//*[@id="content"]/div[3]')  # puxa a div que tem os jogos
    html_content = element.get_attribute('outerHTML')  # pega seu HTML
    # Transforma em algo facil de mexer
    soup = BeautifulSoup(html_content, 'html.parser')

    # pega só divs que tenham tal classe
    Partidas = soup.find_all("div", {"class": "game_summary expanded nohover"})
    qtd = len(Partidas)  # Vê quantas achou

    return qtd

#coleta nome dos times e pega as trabelas
def FazColeta(driver):
    tudo = '//*[@id="content"]'
    elementDeTudo = driver.find_element_by_xpath(tudo)
    html_contentDeTudo = elementDeTudo.get_attribute('outerHTML')
    sopaDeTudo = BeautifulSoup(html_contentDeTudo, 'html.parser')

    tabelasTodas = sopaDeTudo.find_all(
        "table", {"class": "sortable stats_table now_sortable"}) 
    tabelasDosTimes = [tabelasTodas[0], tabelasTodas[2]]

    caixaTimesNomes = sopaDeTudo.find("div", {"class": "scorebox"})
    nomes = caixaTimesNomes.find_all("a", {"itemprop": "name"})

    return nomes, tabelasDosTimes

#pega os valores das tabelas
def PegaComponente(tabela,  coletavel, nomeColetavel):
    componente = tabela.find_all("td", {"data-stat": coletavel})[0]
    valorColetado = componente.get_text()
    print(f'{nomeColetavel}: {valorColetado}')




#função de teste
def TestaBissexto():
    for ano in range(2000):
        # calcula se é ano bissexto
        trueAno = ano
        if (trueAno % 4 == 0 and (trueAno % 400 == 0 or trueAno % 100 != 0)):
            print(trueAno)



print(20*'~~')
print(20*'~~')
print("Talvez modulo errado, de play no 'main.py'")
print(20*'~~')
print(20*'~~')


