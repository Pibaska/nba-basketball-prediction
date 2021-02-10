
# esse codigo deve: -------------------------------------------------------
# função que repete tudo a baixo por todos os dias de uma temporada
# entra na tela de Jogos de um dia expecífico
# ve quantos jogos tem
# entra no "Box Score" do primeiro jogo pega as coisas, volta, e entra no proximo
# salva em json
# -------------------------------------------------------------------------

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
    driver = webdriver.Firefox(firefox_binary=binary,executable_path=r'C:\\geckodriver.exe', options=option)
    return driver


#Retorna quantas partidas o site tem do dia escolhido
def ContadorDePartidas():
    element = driver.find_element_by_xpath('//*[@id="content"]/div[3]') # puxa a div que tem os jogos
    html_content = element.get_attribute('outerHTML') # pega seu HTML
    soup = BeautifulSoup(html_content, 'html.parser') # Transforma em algo facil de mexer

    Partidas = soup.find_all("div", {"class": "game_summary expanded nohover"}) # pega só divs que tenham tal classe
    qtd = len(Partidas) # Vê quantas achou

    return qtd

    
def TestaBissexto():
    for ano in range(2000):
        # calcula se é ano bissexto
        trueAno =  ano
        if (trueAno % 4 == 0 and (trueAno % 400 == 0 or trueAno % 100 != 0)):
            print(trueAno)


def PegaComponente(tabela,  coletavel, nomeColetavel):
    componente = tabela.find_all("td", {"data-stat": coletavel})[0]
    valorColetado = componente.get_text()
    print(f'{nomeColetavel}: {valorColetado}')



def FazColeta():
# pela class [0] [2] class="sortable stats_table now_sortable"
    tudo = '//*[@id="content"]' 
    elementDeTudo = driver.find_element_by_xpath(tudo)
    html_contentDeTudo = elementDeTudo.get_attribute('outerHTML')
    sopaDeTudo = BeautifulSoup(html_contentDeTudo, 'html.parser')

    tabelasTodas = sopaDeTudo.find_all("table", {"class": "sortable stats_table now_sortable"}) 
    tabelasDosTimes = [tabelasTodas[0], tabelasTodas[2]] 

    caixaTimesNomes = sopaDeTudo.find("div", {"class": "scorebox"})
    nomes = caixaTimesNomes.find_all("a", {"itemprop": "name"})

    itensParaColetar = ['pts','fg', 'fg3']
    nomeItensParaColetar = ['Pontos', 
                            'De 2  ', 
                            'De 3  ']
    print('--partida--')
    for x in range(2):
        local = 'casa' if x else 'fora'
        nome = nomes[x].get_text()
        
        print(f'{local} - {nome}')

        for i in range(len(itensParaColetar)):
            PegaComponente( tabelasDosTimes[x],  itensParaColetar[i], nomeItensParaColetar[i]) # casa

        print('-')


def PuxaJogosDoDia(dia, mes, ano):
    #aqui é onde ce vai fazer os processo pesado. (no fim é onde tu vai chamar um monte de função)
    dia += 1
    mes += 1
    # cria e chama a url
    url = f"https://www.basketball-reference.com/boxscores/?month={mes}&day={dia}&year={ano}"
    driver.get(url)
    print('---------D-I-A---------')
    print(f'{dia}/{mes}/{ano }')

    qtdJogos = ContadorDePartidas()
    print(f'Partidas: {qtdJogos}')

    for i in range(qtdJogos): #entra nos jogos para ver mais detalher
        driver.get(url) if i>0 else 0
        driver.find_element_by_xpath(f'//*[@id="content"]/div[3]/div[{i+1}]/p/a[1]').click() # entra no box-score do jogo 
        driver.find_element_by_xpath(f'//*[@id="content"]/div[6]/div[2]/a').click() # Para apresentar apenas 1°quarto

        FazColeta()
        # coletar da tabela
        # mandar pra um dicionário de dicionarios provavelmente




#------------------------------------------------------------------------------ as coisa

#escolhe False mostra o firefox sendo aberto. True faz escondido
driver = SetupDriver(False) # se deixar escondido lembre de checar pelo gerenciador de tarefas

for ano in range(20):
    # calcula se é ano bissexto
    trueAno = 2000 + ano
    bissexto = 1 if (trueAno % 4 == 0 and (trueAno % 400 == 0 or trueAno % 100 != 0)) else 0 # opeador ternário

    for mes in range(12):
        rangeDias = diasNosMeses[mes]
        rangeDias += bissexto if (rangeDias == 28) else 0

        for dia in range (rangeDias):
            PuxaJogosDoDia(dia, mes, trueAno)
            




driver.quit()