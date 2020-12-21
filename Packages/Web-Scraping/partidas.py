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


xPathTabela = "//*[@id='content']/div[3]/div[1]"
"""
//*[@id="content"]/div[2]/h2 # coletar o texto, dividilo e pegar o numero

numero = (conteudo.split(' '))[0]


//*[@id="content"]/div[3]/div[1] #partida do dia (vai ter q calcular quantas teve no dia eu acho)
+
/table[2]  # tabelinha dividida por quartos
+
/tbody/tr[1] # 1=TimeVencedor  2=TimePerdedor  
+
/td[1] #1=nome 2=1quarto 3=2quarto ect 
"""
nomeArquivo =  "partidas" 
nomeDicionario = "partidas_2019-05-"
dicionario = {}


#Descobre quantas partidas o site tem do dia escolhido
def contadorDePartidas():
    element = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]")
    html_content = element.get_attribute('outerHTML')
    soup = BeautifulSoup(html_content, 'html.parser')

    qtdPartidas = soup.find_all('h2')[0].get_text()

    return qtdPartidas


url = "https://www.basketball-reference.com/boxscores/?month=5&day=3&year=2019"

driver.get(url)

qtdPartidas = contadorDePartidas()
print('No dia escolhido ocorreram: ' + qtdPartidas + ' partidas')


#Coletar 
element = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]")
html_content = element.get_attribute('outerHTML')
soup = BeautifulSoup(html_content, 'html.parser')

# print(soup)
# print(html_content.contents[0])


'''
element = driver.find_element_by_xpath(xPathTabela)
html_content = element.get_attribute('outerHTML')

soup = BeautifulSoup(html_content, 'html.parser')
print(soup)
'''

"""

table = soup.find(name='table')

dicionario[nomeDicionario + str(soma)] = df.to_dict('records') #converte o dataframe(df) em um dicionario


# Converter e salvar em um arquivo JSON
js = json.dumps(dicionario)  # converte o dicionario para um jason
fp = open(nomeArquivo + '.json', 'w')  # Abre um arquivo novo
fp.write(js)  # Escreve o conteudo nesse arquivo
fp.close()  # Fecha o arquivo

driver.quit() # fechar o navegador
"""