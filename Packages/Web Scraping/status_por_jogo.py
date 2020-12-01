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

xPathTabela = "//*[@id='team-stats-per_game']"
colunasColetadas = ['Team','G','3P']
renomearColunas = ['time','jogos','cestas_de_3']
nomeArquivo =  "status_por_jogo" 
nomeDicionario = "status_por_jogo_"
dicionario = {}


for i in range(20):
    soma = 2000 + i
    url = "https://www.basketball-reference.com/leagues/NBA_" + str(soma) + ".html#team-stats-per_game::none"

    driver.get(url)

    time.sleep(3)

    element = driver.find_element_by_xpath(xPathTabela)
    html_content = element.get_attribute('outerHTML')

    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find(name='table')

    df_full = pd.read_html(str(table))[0].head(30)
    df = df_full[colunasColetadas]  # Escolhendo as colunas
    df.columns = renomearColunas  # Renomeando as colunas
    print(df)

    dicionario[nomeDicionario + str(soma)] = df.to_dict('records') #converte o dataframe(df) em um dicionario


# Converter e salvar em um arquivo JSON
js = json.dumps(dicionario)  # converte o dicionario para um jason
fp = open(nomeArquivo + '.json', 'w')  # Abre um arquivo novo
fp.write(js)  # Escreve o conteudo nesse arquivo
fp.close()  # Fecha o arquivo

driver.quit() # fechar o navegador
