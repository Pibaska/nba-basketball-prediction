
# Para rodar esse script: -------------------------------------------------------
# baixe geckodriver e o coloque em " C:\\Geckodriver\\geckodriver.exe "
#        https://github.com/mozilla/geckodriver/releases
# baixe o firefox
# -------------------------------------------------------------------------

import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

diasNosMeses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def setup_firefox_driver(show_scraping_window: bool):
    """Faz a configuração inicial do webdriver do firefox. Rodar essa função primeiro.

    Args:
        show_scraping_window (bool): Define se a janela vai ser mostrada durante o web scraping ou não

    Returns:
        webdriver: O driver do firefox configurado e pronto para procurar elementos em sites
    """

    binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
    option = Options()
    option.headless = show_scraping_window
    driver = webdriver.Firefox(
        firefox_binary=binary, executable_path=r'C:\\Geckodriver\\geckodriver.exe', options=option)  # https://github.com/mozilla/geckodriver/releases <- baixe de acordo
    return driver


def generate_date_list():
    """Gera uma lista de datas no formato [dia, mês, ano]

    Returns:
        list: A lista de datas formatadas como listas
    """
    formatted_date = []
    formatted_date_list = []
    for year_increment in range(20):
        year = 2000 + year_increment
        is_leap_year = check_for_leap_year(year)

        for month in range(12):
            day_range = diasNosMeses[month]

            day_range += is_leap_year if (day_range == 28) else 0

            for day in range(day_range):
                formatted_date = [day+1, month+1, year]
                formatted_date_list.append(formatted_date)

    return formatted_date_list


def check_for_leap_year(year):
    """Recebe um ano e diz se ele é bissexto

    Args:
        year (int): O ano a ser checado

    Returns:
        bool: True se o ano do input for bissexto
    """

    is_leap_year = 1 if (year % 4 == 0 and (
        year % 400 == 0 or year % 100 != 0)) else 0
    return is_leap_year


def generate_day_url(formatted_date):
    """Gera o URL para pegar os dados de partidas de determinado dia

    Args:
        formatted_date (list): A data desejada no formato de lista [dia, mês, ano]

    Returns:
        str: A URL gerada a partir da data do input
    """

    day = formatted_date[0]
    month = formatted_date[1]
    year = formatted_date[2]
    url = f"https://www.basketball-reference.com/boxscores/?month={month}&day={day}&year={year}"

    return url


def access_1q_in_box_score(driver, url, i):
    """Entra no box score e filtra pelo primeiro quarto

    Args:
        driver (webdriver): Driver que vai acessar as URLs
        url (str): Endereço da página a ser acessada
        i (int): ???
    """

    driver.get(url) if i > 0 else 0
    # entra no box-score do jogo
    driver.find_element_by_xpath(
        f'//*[@id="content"]/div[3]/div[{i+1}]/p/a[1]').click()

    # Para apresentar apenas 1°quarto
    driver.find_element_by_xpath(
        f'//*[@id="content"]/div[6]/div[2]/a').click()


def get_match_amount(driver):
    """Retorna quantas partidas o site tem do dia escolhido

    Args:
        driver (webdriver): Driver que vai encontrar os elemtnos da página

    Returns:
        int: Quantidade de jogos disponíveis no dia escolhido
    """

    element = driver.find_element_by_xpath(
        '//*[@id="content"]/div[3]')  # puxa a div que tem os jogos

    html_content = element.get_attribute('outerHTML')  # pega seu HTML

    # Transforma em algo facil de mexer
    parsed_div = BeautifulSoup(html_content, 'html.parser')

    # pega só divs que tenham tal classe
    match_list = parsed_div.find_all(
        "div", {"class": "game_summary expanded nohover"})
    match_amount = len(match_list)  # Vê quantas achou

    return match_amount

#


def get_team_table_names(driver):
    """Coleta nome dos times e pega as tabelas

    Args:
        driver (webdriver): Driver que vai achar as tabelas

    Returns:
        list, list: Os nomes dos times e os nomes das tabelas correspondentes
    """

    page_content = '//*[@id="content"]'
    content_element = driver.find_element_by_xpath(page_content)
    content_html = content_element.get_attribute('outerHTML')
    parsed_content = BeautifulSoup(content_html, 'html.parser')

    content_tables = parsed_content.find_all(
        "table", {"class": "sortable stats_table now_sortable"})
    team_tables = [content_tables[0], content_tables[2]]

    team_name_scorebox = parsed_content.find("div", {"class": "scorebox"})
    team_names = team_name_scorebox.find_all("a", {"itemprop": "name"})

    return team_names, team_tables


def get_table_values(table,  collectable_value, value_name):
    """Pega os valores das tabelas

    Args:
        table (?): Tabela da qual os valores vão ser extraídos
        collectable_value (str): Como o valor a ser coletado é chamado dentro da tabela
        value_name (str): Nome pro valor depois que ele for coletado
    """

    table_component = table.find_all("td", {"data-stat": collectable_value})[0]
    collected_value = table_component.get_text()
    print(f'{value_name}: {collected_value}')


if __name__ == "__main__":
    print(20*'~~')
    print(20*'~~')
    print("Talvez modulo errado, de play no 'web_scraping_main.py'")
    print(20*'~~')
    print(20*'~~')
