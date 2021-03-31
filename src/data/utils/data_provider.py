'''
Este arquivo visa criar as medias que serão exigidas pelo AG

Media de pontos h/a
Spread h/a
Offensive Rebound h/a
Defensive Rebound h/a
Field Goal Percentage % h/a
3-Point Field Goal % h/a
Free throw % h/a
Turnover h/a
Assists h/a
talvez  Dificuldade enfrentada h/a
'''
import sqlite3
import random
from pathlib import Path
from os.path import join
from datetime import datetime as dt
from datetime import timedelta  
from core.utils.directory_manipulation import Directory

# dicionário com começo e final das seasons, de 2000 até 2020
#  começo: season["2015"][start]    fim: season["2015"][end]
seasons = {
    "1999": {"start": "1999-11-02", "end": "2000-04-19"},
    "2000": {"start": "2000-10-31", "end": "2001-04-18"},
    "2001": {"start": "2001-10-30", "end": "2002-04-17"},
    "2002": {"start": "2002-10-29", "end": "2003-04-16"},
    "2003": {"start": "2003-10-28", "end": "2004-04-14"},
    "2004": {"start": "2004-11-02", "end": "2005-04-20"},
    "2005": {"start": "2005-11-01", "end": "2006-04-19"},
    "2006": {"start": "2006-10-31", "end": "2007-04-18"},
    "2007": {"start": "2007-10-30", "end": "2008-04-16"},
    "2008": {"start": "2008-10-28", "end": "2009-04-16"},
    "2009": {"start": "2009-10-27", "end": "2010-04-14"},
    "2010": {"start": "2010-10-26", "end": "2011-04-13"},
    "2011": {"start": "2011-12-25", "end": "2012-04-26"},
    "2012": {"start": "2012-10-30", "end": "2013-04-17"},
    "2013": {"start": "2013-10-29", "end": "2014-04-16"},
    "2014": {"start": "2014-10-28", "end": "2015-04-15"},
    "2015": {"start": "2015-10-27", "end": "2016-04-13"},
    "2016": {"start": "2016-10-25", "end": "2017-04-12"},
    "2017": {"start": "2017-10-17", "end": "2018-04-11"},
    "2018": {"start": "2018-10-16", "end": "2019-04-10"},
    "2019": {"start": "2019-10-22", "end": "2020-03-11"},
    "2020": {"start": "2020-12-22", "end": "2021-05-16"},
    "2021": {"start": "2021-10-31", "end": "2022-04-10"}
}


def get_match_amount():
    """Busca quantas partidas estão presentes no banco de dados e retorna esse valor

    Raises:
        e: Exceção coringa do tipo Exception

    Returns:
        int: Quantidade de partidas presentes no banco de dados
    """

    try:
        db_connection = sqlite3.connect(join(Directory(Path(__file__).resolve().parent.parent.parent).cwd,
                                             'data', 'database.sqlite3'))
        cursor = db_connection.cursor()

        cursor.execute(
            """
            SELECT 
                match_id 
            FROM 
                match_data 
            ORDER BY 
                match_id DESC;
            """)

        lista = (cursor.fetchall())

        return lista[0][0]

    except Exception as e:
        print(e)
        raise e


def get_matches_by_season(date):
    """Escolhe todas as partidas da season -exceto dos 10 primeiros dias- e retorna alguns dados
    referentes a elas.

    Args:
        date (int): ano de inicio de uma temporada.

    Raises:
        e: Exceção do tipo Exception

    Returns:
        list: Uma lista com partidas e para cada partida uma lista com os seguintes valores:
            int dizendo se o time em casa ganhou (1=true, 0=false)
            id correspondendo à fk do time em casa
            id correspondente à fk do time fora
            data da partida
    """

    season_start = get_start_season_by_date(date)


    str_for_sql_date_start = str(dt.strptime(season_start, "%Y-%m-%d").date() + timedelta(days=10)) 
    str_for_sql_date_end = str(date[0])+"-"+str(date[1])+"-"+str(date[2])

    try:
        db_connection = sqlite3.connect(join(Directory(Path(__file__).resolve().parent.parent.parent).cwd,
                                             'data', 'database.sqlite3'))
        cursor = db_connection.cursor()

        cursor.execute(
            """        
            Select pt_home.won, pt_home.fk_team_id, pt_away.fk_team_id, md.date from match_data as md 
                INNER JOIN participation as pt_home On md.fk_participation_home = pt_home.participation_id
                INNER JOIN participation as pt_away On md.fk_participation_away = pt_away.participation_id
                    WHERE md.date >= ?
                    and   md.date <= ?
                    order by md.date desc
            """, [str_for_sql_date_start, str_for_sql_date_end])

        lista = cursor.fetchall()

        pre_averages_dict_list = []

        for item in lista:
            pre_averages_dict_list.append({
                "team_home_won": item[0],
                "team_home_id": item[1],
                "team_away_id": item[2],
                "match_data": item[3].split('-')
            })

        return pre_averages_dict_list

    except Exception as e:
        print(e)
        raise e


def row_factory(cursor, row):
    match_stats = {}

    for value_index, column in enumerate(cursor.description):
        # Fiz essa checagem pra esse método poder funcionar num INNER JOIN
        # com 2 linhas da mesma tabela (time de casa e time fora)
        match_stats[column[0]] = row[value_index]

    return match_stats


def get_averages(team_id, local, date):
    """Recebe uma data e tras as medias do time a partir do inicio da season ate a data informada
        O primeiro dia da season vem de uma lista

    Args:
        team_id (int), 
        local = 1(casa) ou 0(fora),
        date [dia,mes,ano]

    Returns:
        retorna os valores em um dicionario: 
        [
            Media de pontos:
            //Spread:
            Offensive Rebound:
            Defensive Rebound:
            Field Goal Percentage:
            3-Point Field Goal Percentage:
            Free throw Percentage:
            Turnover:
            Assists:
            //Dificuldade enfrentada:
        ]
    """

    # descobre de que season é a data, e retorna a data de inicio da mesma
    start_season = get_start_season_by_date(date)

    try:
        db_connection = sqlite3.connect(join(Directory(Path(__file__).resolve().parent.parent.parent).cwd,
                                             'data', 'database.sqlite3'))
        db_connection.row_factory = row_factory
        cursor = db_connection.cursor()

        participation_local = "pt_home" if local else "pt_away"
        participation_opponent = "pt_home" if not(local) else "pt_away"

        cursor.execute(
            """ 
            SELECT 
                AVG(""" + participation_local + """.won) as won,
                AVG(""" + participation_local + """.points) as points, 
                AVG(""" + participation_local + """.points - """ + participation_opponent + """.points) as spread, 
                AVG(""" + participation_local + """.offensive_rebounds) as offensive_rebounds,
                AVG(""" + participation_local + """.defensive_rebounds) as defensive_rebounds ,
                AVG(NULLIF(""" + participation_local + """.field_goals_percentage,0)) as field_goals_percentage ,
                AVG(NULLIF(""" + participation_local + """.three_point_field_goals_percentage,0)) as three_point_field_goals_percentage,
                AVG(NULLIF(""" + participation_local + """.free_throws_percentage,0)) as free_throws_percentage,
                AVG(""" + participation_local + """.turnover) as turnover, 
                AVG(""" + participation_local + """.assists) as assists 
                    from match_data as md 
                    INNER JOIN participation as pt_home 
                    ON md.fk_participation_home = pt_home.participation_id 
                    INNER JOIN participation as pt_away
                    on md.fk_participation_away = pt_away.participation_id
                            WHERE """ + participation_local + """.fk_team_id = ?
                            and """ + participation_local + """.team_is_home = ?
                            and md.date > ?
                            and md.date <  ?
                            order by md.date ASC;   
                """, [team_id, local, start_season, str(date[0])+"-"+str(date[1])+"-"+str(date[2])])
        dicionario = cursor.fetchall()

        return dicionario[0]

    except Exception as e:
        print(e)
        raise e


def get_start_season_by_date(date):
    """Recebe uma data e retorna a data do começo da season da qual ela pertence

    Args:
        date(list): A data de input, no formato de uma lista [ano, mês, dia]

    Returns:
        list: Outra lista com a data do início da season daquela data
    """
    strigDate = str(date[0])+"-"+str(date[1])+"-" + \
        str(date[2])  # transforma o date em string
    if dt.strptime(strigDate, "%Y-%m-%d").date() > dt.strptime(seasons[str(date[0])]["start"], "%Y-%m-%d").date():
        seasonStart = seasons[str(date[0])]["start"]
    else:
        seasonStart = seasons[str(int(date[0])-1)]["start"]

    return seasonStart


def get_team_id_from_name(team_name):
    try:
        db_connection = sqlite3.connect(join(Directory(Path(__file__).resolve().parent.parent.parent).cwd,
                                             'data', 'database.sqlite3'))
        cursor = db_connection.cursor()

        cursor.execute(
            """
            SELECT
                team_id
            FROM
                team
            WHERE
                team_name = ?
            """,
            [team_name]
        )

        team_id = cursor.fetchone()

        return team_id[0]
    except Exception as e:
        print(e)
        raise e


def get_matches_averages_by_season(date, **kwargs):
    # match_total = get_match_amount()

    matches_dict = get_matches_by_season(date)

    team_home_averages = []
    team_away_averages = []
    match_averages = []

    for match in matches_dict:
        team_home_averages = get_averages(
            match["team_home_id"], 1, match["match_data"])
        team_away_averages = get_averages(
            match["team_away_id"], 0, match["match_data"])

        match_averages.append({"team_home": team_home_averages.copy(), "team_away": team_away_averages.copy(),
                               "home_won": match["team_home_won"]})

    # Usar para ver os nulos
    # problem = 0 if team_home_averages[0][0] and team_home_averages[0][0] else 1
    # if problem:
    #     raise Exception("Sorry, no numbers below zero")

    return match_averages


def get_specific_match_averages(team_home_name, team_away_name, date):
    team_home_averages = get_averages(
        get_team_id_from_name(team_home_name), 1, date)
    team_away_averages = get_averages(
        get_team_id_from_name(team_away_name), 0, date)

    match_averages = {"team_home": team_home_averages,
                      "team_away": team_away_averages}

    return match_averages


if __name__ == "__main__":
    #     print(get_matches_averages_by_season("2017"))

    season_start = seasons["2017"]["start"].replace('/', '-')
    season_end = seasons["2017"]["end"].replace('/', '-')

    print()
# SELECT
#     AVG(pt_home.points),
#     AVG(pt_home.points - pt_away.points) as spread,
#     AVG(pt_home.offensive_rebounds),
#     AVG(pt_home.defensive_rebounds),
#     AVG(NULLIF(pt_home.field_goals_percentage,0)),
#     AVG(NULLIF(pt_home.three_point_field_goals_percentage,0)),
#     AVG(NULLIF(pt_home.free_throws_percentage,0)),
#     AVG(pt_home.turnover),
#     AVG(pt_home.assists)
#         from match_data as md
#         INNER JOIN participation as pt_home
#         ON md.fk_participation_home = pt_home.participation_id
#         INNER JOIN participation as pt_away
#         on md.fk_participation_away = pt_away.participation_id
#             WHERE pt_home.fk_team_id = 5

# SELECT
#     AVG(pt_away.points),
#     AVG(pt_away.points - pt_home.points) as spread,
#     AVG(pt_away.offensive_rebounds),
#     AVG(pt_away.defensive_rebounds),
#     AVG(NULLIF(pt_away.field_goals_percentage,0)),
#     AVG(NULLIF(pt_away.three_point_field_goals_percentage,0)),
#     AVG(NULLIF(pt_away.free_throws_percentage,0)),
#     AVG(pt_away.turnover),
#     AVG(pt_away.assists)
#         from match_data as md
#         INNER JOIN participation as pt_away
#         ON md.fk_participation_away = pt_away.participation_id
#         INNER JOIN participation as pt_home
#         on md.fk_participation_home = pt_home.participation_id
#             WHERE pt_away.fk_team_id = 5
