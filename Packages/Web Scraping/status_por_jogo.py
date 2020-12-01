from bs4 import BeautifulSoup
from DriverFirefox import Driver_Firefox
import pandas as pd
import time
import json


def Status_PJogo():
    gecko_driver, firefox_options = Driver_Firefox()

    xPathTabela = "//*[@id='team-stats-per_game']"
    colunasColetadas = ['Team','G','3P']
    renomearColunas = ['time','jogos','cestas_de_3']
    nomeArquivo =  "status_por_jogo"
    nomeDicionario = "status_por_jogo_"
    dicionario = {}
    for i in range(20):
        soma = 2000 + i
        url = "https://www.basketball-reference.com/leagues/NBA_" + str(soma) + ".html#team-stats-per_game::none"

        gecko_driver.get(url)

        time.sleep(3)

        element = gecko_driver.find_element_by_xpath(xPathTabela)
        html_content = element.get_attribute('outerHTML')

        soup = BeautifulSoup(html_content, 'html.parser')
        table = soup.find(name='table')

        df_full = pd.read_html(str(table))[0].head(30)
        df = df_full[colunasColetadas]  # Escolhendo as colunas
        df.columns = renomearColunas  # Renomeando as colunas
        print(df)
        # converte o dataframe(df) em um dicionario
        dicionario[nomeDicionario + str(soma)] = df.to_dict('records')

    # Converter e salvar em um arquivo JSON
    js = json.dumps(dicionario)  # converte o dicionario para um jason
    fp = open('' + nomeArquivo + '.json', 'w')  # Abre um arquivo novo
    fp.write(js)  # Escreve o conteudo nesse arquivo
    fp.close()  # Fecha o arquivo

    gecko_driver.quit() # fechar o navegador
