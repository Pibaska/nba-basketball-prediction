
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

if __name__ == "__main__":
    import web_scraping_functions as ws_functions
    from utils.database import database_manipulation as db
else:
    import web.web_scraping_functions as ws_functions
    import utils.database.database_manipulation as db

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

    last_year = db.get_last_date()[0]
    last_month = db.get_last_date()[1]
    last_day = db.get_last_date()[2]

    for year_increment in range(20):
        last_year += year_increment
        is_leap_year = check_for_leap_year(last_year)

        for month_increment in range(12):
            if month_increment + 1 >= last_month:
                last_month = 0

                day_range = diasNosMeses[month_increment]
                day_range += is_leap_year if (day_range == 28) else 0

                for day_increment in range(day_range):
                    if day_increment >= last_day:
                        last_day = 0

                        formatted_date = [last_year,
                                          month_increment + 1, day_increment+1]
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

    day = formatted_date[2]
    month = formatted_date[1]
    year = formatted_date[0]
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

    team_name_scorebox = parsed_content.find("div", {"class": "scorebox"})
    team_names = team_name_scorebox.find_all("a", {"itemprop": "name"})

    team_tables = ['1', '2']
    for i in range(2):
        table_content_xpath = '//*[@id="box-' + \
            abbreviations[team_names[i].get_text()] + '-q1-basic"]'
        table_content_element = driver.find_element_by_xpath(
            table_content_xpath)
        table_content_html = table_content_element.get_attribute('outerHTML')
        table_parsed_content = BeautifulSoup(table_content_html, 'html.parser')

        content_table = table_parsed_content

        team_tables[i] = content_table

    return team_names, team_tables


def get_table_values(table,  collectable_value):
    """Pega os valores das tabelas

    Args:
        table (?): Tabela da qual os valores vão ser extraídos
        collectable_value (str): Como o valor a ser coletado é chamado dentro da tabela
    """
# //*[@id="box-ORL-q1-basic"]/tfoot/tr
    foot_component = table.find("tfoot")
    td_component = foot_component.find_all(
        "td", {"data-stat": collectable_value})[0]
    collected_value = td_component.get_text()
    return collected_value


if __name__ == "__main__":
    print(20*'~~')
    print(20*'~~')
    print("Talvez modulo errado, de play no 'web_scraping_main.py'")
    print(20*'~~')
    print(20*'~~')

    print(generate_date_list())


abbreviations = {
    'Anderson Packers': 'AND',
    'Atlanta Hawks': 'ATL',
    'Baltimore Bullets': 'BAL',
    'Brooklyn Nets': 'BKN',
    'Boston Celtics': 'BOS',
    'Buffalo Braves': 'BUF',
    'Capital Bullets': 'CAP',
    'Charlotte Hornets': 'CHH',
    'Charlotte Bobcats': 'CHN',
    'Chicago Bulls': 'CHI',
    'Chicago Packers': 'CHP',
    'Chicago Zephyrs': 'CHP',
    'Chicago Stags': 'CHS',
    'Cincinnati Royals': 'CIN',
    'Cleveland Cavaliers': 'CLE',
    'Dallas Mavericks': 'DAL',
    'Dallas Chaparrals': 'DLC',
    'Denver Nuggets': 'DEN',
    'Denver Rockets': 'DEN',
    'Detroit Pistons': 'DET',
    'Fort Wayne Pistons': 'FTW',
    'Golden State Warriors': 'GSW',
    'Houston Rockets': 'HOU',
    'Indiana Pacers': 'IND',
    'Indianapolis Olympians': 'INO',
    'Kansas City Kings': 'KCK',
    'Kansas City-Omaha Kings': 'KCO',
    'Los Angeles Clippers': 'LAC',
    'Los Angeles Lakers': 'LAL',
    'Memphis Grizzlies': 'MEM',
    'Miami Heat': 'MIA',
    'Milwaukee Bucks': 'MIL',
    'Milwaukee Hawks': 'MLH',
    'Minneapolis Lakers': 'MPL',
    'Minnesota Muskies': 'MNM',
    'Minnesota Timberwolves': 'MIN',
    'New Jersey Nets': 'NJN',
    'New Orleans Hornets': 'NOK',
    'New Orleans Jazz': 'NOR',
    'New Orleans Pelicans': 'NOP',
    'New York Knicks': 'NYK',
    'New York Nets': 'NYN',
    'Oklahoma City Hornets': 'NOK',
    'Oklahoma City Thunder': 'OKC',
    'Orlando Magic': 'ORL',
    'Philadelphia 76ers': 'PHI',
    'Philadelphia Warriors': 'PHW',
    'Phoenix Suns': 'PHO',
    'Portland Trail Blazers': 'POR',
    'Rochester Royals': 'ROC',
    'Sacramento Kings': 'SAC',
    'San Antonio Spurs': 'SAS',
    'San Diego Clippers': 'SDC',
    'San Diego Rockets': 'SDR',
    'San Francisco Warriors': 'SFW',
    'Seattle SuperSonics': 'SEA',
    'Sheboygan Redskins': 'SHE',
    'St. Louis Bombers': 'SLB',
    'St. Louis Hawks': 'STL',
    'Syracuse Nationals': 'SYR',
    'Toronto Raptors': 'TOR',
    'Tri-Cities Blackhawks': 'TRI',
    'Utah Jazz': 'UTA',
    'Vancouver Grizzlies': 'VAN',
    'Washington Bullets': 'WAS',
    'Washington Capitals': 'WSC',
    'Washington Wizards': 'WAS',
    'Waterloo Hawks': 'WAT'
}

'''
    ('Anderson Packers', 'AND'),
    ('Atlanta Hawks', 'ATL'),
    ('Baltimore Bullets', 'BAL'),
    ('Brooklyn Nets', 'BKN'),
    ('Boston Celtics', 'BOS'),
    ('Buffalo Braves', 'BUF'),
    ('Capital Bullets', 'CAP'),
    ('Charlotte Hornets', 'CHH'),
    ('Charlotte Bobcats', 'CHN'),
    ('Chicago Bulls', 'CHI'),
    ('Chicago Packers', 'CHP'),
    ('Chicago Zephyrs', 'CHP'),
    ('Chicago Stags', 'CHS'),
    ('Cincinnati Royals', 'CIN'),
    ('Cleveland Cavaliers', 'CLE'),
    ('Dallas Mavericks', 'DAL'),
    ('Dallas Chaparrals', 'DLC'),
    ('Denver Nuggets', 'DEN'),
    ('Denver Rockets', 'DEN'),
    ('Detroit Pistons', 'DET'),
    ('Fort Wayne Pistons', 'FTW'),
    ('Golden State Warriors', 'GSW'),
    ('Houston Rockets', 'HOU'),
    ('Indiana Pacers', 'IND'),
    ('Indianapolis Olympians', 'INO'),
    ('Kansas City Kings', 'KCK'),
    ('Kansas City-Omaha Kings', 'KCO'),
    ('Los Angeles Clippers', 'LAC'),
    ('Los Angeles Lakers', 'LAL'),
    ('Memphis Grizzlies', 'MEM'),
    ('Miami Heat', 'MIA'),
    ('Milwaukee Bucks', 'MIL'),
    ('Milwaukee Hawks', 'MLH'),
    ('Minneapolis Lakers', 'MPL'),
    ('Minnesota Muskies', 'MNM'),
    ('Minnesota Timberwolves', 'MIN'),
    ('New Jersey Nets', 'NJN'),
    ('New Orleans Hornets', 'NOK'),
    ('New Orleans Jazz', 'NOR'),
    ('New Orleans Pelicans', 'NOP'),
    ('New York Knicks', 'NYK'),
    ('New York Nets', 'NYN'),
    ('Oklahoma City Hornets', 'NOK'),
    ('Oklahoma City Thunder', 'OKC'),
    ('Orlando Magic', 'ORL'),
    ('Philadelphia 76ers', 'PHI'),
    ('Philadelphia Warriors', 'PHW'),
    ('Phoenix Suns', 'PHO'),
    ('Portland Trail Blazers', 'POR'),
    ('Rochester Royals', 'ROC'),
    ('Sacramento Kings', 'SAC'),
    ('San Antonio Spurs', 'SAS'),
    ('San Diego Clippers', 'SDC'),
    ('San Diego Rockets', 'SDR'),
    ('San Francisco Warriors', 'SFW'),
    ('Seattle SuperSonics', 'SEA'),
    ('Sheboygan Redskins', 'SHE'),
    ('St. Louis Bombers', 'SLB'),
    ('St. Louis Hawks', 'STL'),
    ('Syracuse Nationals', 'SYR'),
    ('Toronto Raptors', 'TOR'),
    ('Tri-Cities Blackhawks', 'TRI'),
    ('Utah Jazz', 'UTA'),
    ('Vancouver Grizzlies', 'VAN'),
    ('Washington Bullets', 'WAS'),
    ('Washington Capitals', 'WSC'),
    ('Washington Wizards', 'WAS'),
    ('Waterloo Hawks', 'WAT');
'''
