
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


def setup_firefox_driver(show_scraping_window: bool):
    binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
    option = Options()
    option.headless = show_scraping_window
    driver = webdriver.Firefox(
        firefox_binary=binary, executable_path=r'C:\\Geckodriver\\geckodriver.exe', options=option)  # https://github.com/mozilla/geckodriver/releases <- baixe de acordo
    return driver


def generate_date_list():
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
    is_leap_year = 1 if (year % 4 == 0 and (
        year % 400 == 0 or year % 100 != 0)) else 0
    return is_leap_year


def access_matches(formatted_date):
    day = formatted_date[0]
    month = formatted_date[1]
    year = formatted_date[2]
    url = f"https://www.basketball-reference.com/boxscores/?month={month}&day={day}&year={year}"

    return(url)

# entra no box score e filtra pelo primeiro quarto


def access_1q_in_box_score(driver, url, i):

    driver.get(url) if i > 0 else 0
    # entra no box-score do jogo
    driver.find_element_by_xpath(
        f'//*[@id="content"]/div[3]/div[{i+1}]/p/a[1]').click()

    # Para apresentar apenas 1°quarto
    driver.find_element_by_xpath(
        f'//*[@id="content"]/div[6]/div[2]/a').click()


# Retorna quantas partidas o site tem do dia escolhido
def get_match_amount(driver):
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

# coleta nome dos times e pega as tabelas


def get_team_table_names(driver):
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

# pega os valores das tabelas


def get_table_values(table,  collectable_value, value_name):
    table_component = table.find_all("td", {"data-stat": collectable_value})[0]
    collected_value = table_component.get_text()
    print(f'{value_name}: {collected_value}')


if __name__ == "__main__":
    print(20*'~~')
    print(20*'~~')
    print("Talvez modulo errado, de play no 'web_scraping_main.py'")
    print(20*'~~')
    print(20*'~~')
