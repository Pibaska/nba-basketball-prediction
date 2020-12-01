from DriverFirefox import Driver_Firefox
from bs4 import BeautifulSoup
import pandas as pd
import time
import json


def Prototipo():
    gecko_driver, firefox_options = Driver_Firefox()

    # variaveis que serão utilizadas
    url = "https://www.nba.com/stats/teams/traditional/?sort=PTS&dir=-1"
    xPathAceitarTermos = "//div[@class='banner-actions-container']//button[@id='onetrust-accept-btn-handler']"
    xPathOrdenar = "/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[2]/div[1]/table/thead/tr/th[8]"
    xPathTabela = "//div[@class='nba-stat-table']//table"

    colunasColetadas = ['TEAM', 'PTS', 'WIN%', 'FG%', 'FT%']
    renomearColunas = ['Time', '%_vitória', 'pontos', '%_cestas de campo', '%_lances livres']

    nomeArquivo =  "Times_bask"
    nomeDicionario = "times_dict"

    # puxa a url
    gecko_driver.get(url)

    time.sleep(6)
    # clicka no /div/button    (é pra aceitar os termos)
    gecko_driver.find_element_by_xpath(xPathAceitarTermos).click()

    time.sleep(5)
    # clicka no /div/table/thead/tr/th
    gecko_driver.find_element_by_xpath(xPathOrdenar).click()

    # pega a parte do html
    element = gecko_driver.find_element_by_xpath(xPathTabela)
    html_content = element.get_attribute('outerHTML')

    # Analisa e parseia esse HTML e o transforma em um dado estruturado para podermos trabalhar
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find(name='table')

    # Estrutura o conteúdo em um DataFrame
    # (o metodo le uma string)(volta um array)(limitamos a um top10)
    df_full = pd.read_html(str(table))[0].head(20)
    df = df_full[colunasColetadas]  # Escolhendo as colunas
    df.columns = renomearColunas  # Renomeando as colunas
    print(df)

    # Transformar os Dados em um Dicionário de dados próprio
    top10ranking = {nomeDicionario: df.to_dict('records')}

    # Converter e salvar em um arquivo JSON
    js = json.dumps(top10ranking)  # converte o dicionario para um jason
    fp = open(nomeArquivo, 'w')  # Abre um arquivo novo
    fp.write(js)  # Escreve o conteudo nesse arquivo
    fp.close()  # Fecha o arquivo

    # fechar o navegador
    gecko_driver.quit()


if __name__ == '__main__':
    Prototipo()
