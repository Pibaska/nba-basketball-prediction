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
from core.utils.directory_manipulation import Directory

# dicionário com começo e final das seasons, de 2000 até 2020
#  começo: season["2015"][start]    fim: season["2015"][end]
seasons = {
    "1999": {"start": "1999-11-2", "end": "2000-4-19"},
    "2000": {"start": "2000-10-31", "end": "2001-4-18"},
    "2001": {"start": "2001-10-30", "end": "2002-4-17"},
    "2002": {"start": "2002-10-29", "end": "2003-4-16"},
    "2003": {"start": "2003-10-28", "end": "2004-4-14"},
    "2004": {"start": "2004-11-2", "end": "2005-4-20"},
    "2005": {"start": "2005-11-1", "end": "2006-4-19"},
    "2006": {"start": "2006-10-31", "end": "2007-4-18"},
    "2007": {"start": "2007-10-30", "end": "2008-4-16"},
    "2008": {"start": "2008-10-28", "end": "2009-4-16"},
    "2009": {"start": "2009-10-27", "end": "2010-4-14"},
    "2010": {"start": "2010-10-26", "end": "2011-4-13"},
    "2011": {"start": "2011-12-25", "end": "2012-4-26"},
    "2012": {"start": "2012-10-30", "end": "2013-4-17"},
    "2013": {"start": "2013-10-29", "end": "2014-4-16"},
    "2014": {"start": "2014-10-28", "end": "2015-4-15"},
    "2015": {"start": "2015-10-27", "end": "2016-4-13"},
    "2016": {"start": "2016-10-25", "end": "2017-4-12"},
    "2017": {"start": "2017-10-17", "end": "2018-4-11"},
    "2018": {"start": "2018-10-16", "end": "2019-4-10"},
    "2019": {"start": "2019-10-22", "end": "2020-3-11"},
    "2020": {"start": "2020-12-22", "end": "2021-5-16"}
}

# o AG vai fazer o fit com partidas começadas apos 10 dias do começo da temporada
# e então o AG vai se movimentar para frente no tempo apenas, e usará uma quantidade de jogos
#  Poderiamos previamente selecionar jogos para o fit
# É uma questão importante pois o fit funcionaria com um jogo só de DATA
# todas funções aqui vão rodar dentro de um dia


# todos jogos do Atlanta Hawks(id=2) em casa a partir do dia '08/01/2000' ate o dia '20/02/2000'
""" 
SELECT * from match_data as md INNER JOIN participation as pt 
    ON md.fk_participation_home = pt.participation_id 
    WHERE pt.fk_team_id = 2 
    and pt.team_is_home = 1
    and md.date > '2000-01-08'
    and md.date < '2000-02-20'
    order by md.date ASC;
"""
# MEDIA da coisa de cima
"""
SELECT 
  AVG(pt.points), --Pontos h/a
  AVG(pt.offensive_rebounds),--Offensive Rebound h/a
  AVG(pt.defensive_rebounds),--Defensive Rebound h/a
  AVG(NULLIF(pt.field_goals_percentage,0)),--Field Goal Percentage % h/a
  AVG(NULLIF(pt.three_point_field_goals_percentage,0)),--3-Point Field Goal % h/a
  AVG(NULLIF(pt.free_throws_percentage,0)),--Free throw % h/a
  AVG(pt.turnover),--Turnover h/a
  AVG(pt.assists)--Assists h/a AVG 
	from match_data as md INNER JOIN participation as pt 
    ON md.fk_participation_home = pt.participation_id 
    WHERE pt.fk_team_id = 2 
    and pt.team_is_home = 1
    and md.date > '2000-01-08'
    and md.date < '2000-02-20'
    order by md.date ASC;   
"""

# EXPLICAÇÃO DA USABILIDADE DO SELECT ACIMA
# temporada começou em 08/01/2000
# O ag ta no dia 20/02/2000
# lembrando q estamos ignorando SPREAD e a DIFICULDADE ENFRENTADA por enquanto


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


def get_matches_by_season(season, amount):
    """Escolhe uma partida aleatória entre todas as partidas salvas e retorna alguns dados
    referentes a ela.

    Args:
        match_amount (int): Quantidade de partidas salvas para escolher um índice aleatoriamente

    Raises:
        e: Exceção do tipo Exception

    Returns:
        list: Uma lista com os seguintes valores da partida aleatória:
            int dizendo se o time em casa ganhou (1=true, 0=false)
            id correspondendo à fk do time em casa
            id correspondente à fk do time fora
            data da partida
    """

    # pegar match aleatoria a partir de id
    season_start = seasons[season]["start"].replace('/', '-') 
    season_end   = seasons[season]["end"].replace('/', '-')


    try:
        db_connection = sqlite3.connect(join(Directory(Path(__file__).resolve().parent.parent.parent).cwd,
                                                 'data', 'database.sqlite3'))
        cursor = db_connection.cursor()

        # cursor.execute(
        #     """        
        #     Select pt_home.won, pt_home.fk_team_id, pt_away.fk_team_id, md.date from match_data as md 
        #         INNER JOIN participation as pt_home On md.fk_participation_home = pt_home.participation_id
        #         INNER JOIN participation as pt_away On md.fk_participation_away = pt_away.participation_id
        #             WHERE md.match_id = ?
        #     """, [str_match_id])

        cursor.execute(
            """        
            Select pt_home.won, pt_home.fk_team_id, pt_away.fk_team_id, md.date from match_data as md 
                INNER JOIN participation as pt_home On md.fk_participation_home = pt_home.participation_id
                INNER JOIN participation as pt_away On md.fk_participation_away = pt_away.participation_id
                    WHERE md.date >= ?
                    and   md.date <= ?
                    order by md.date desc
            """, [season_start, season_end])

        lista = cursor.fetchall()

        for i in range(amount):
            pre_averages_dict = {
                "team_home_won": lista[i][0],
                "team_home_id": lista[i][1],
                "team_away_id": lista[i][2],
                "match_data": lista[i][3].split('-')
            }

        return pre_averages_dict

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
    strigDate = str(date[0])+"/"+str(date[1])+"/" + \
        str(date[2])  # transforma o date em string

    # descobre de que season é a data, e retorna a data de inicio da mesma
    if dt.strptime(strigDate, "%Y/%m/%d").date() > dt.strptime(seasons[str(date[0])]["start"], "%Y/%m/%d").date():
        seasonStart = seasons[str(date[0])]["start"]
    else:
        seasonStart = seasons[str(int(date[0])-1)]["start"]

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
                """, [team_id, local, str(dt.strptime(seasonStart, "%Y/%m/%d").date()), str(dt.strptime(strigDate, "%Y/%m/%d").date())])
        dicionario = cursor.fetchall()

        return dicionario[0]

    except Exception as e:
        print(e)
        raise e


def get_spread():

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


def get_matches_averages_by_season(season, amount, **kwargs):
    # match_total = get_match_amount()

    pre_averages_dict = get_matches_by_season(season, amount)

    team_home_averages = get_averages(
        pre_averages_dict["team_home_id"], 1, pre_averages_dict["match_data"])
    team_away_averages = get_averages(
        pre_averages_dict["team_away_id"], 0, pre_averages_dict["match_data"])

    match_averages = {"team_home": team_home_averages, "team_away": team_away_averages,
                      "home_won": pre_averages_dict["team_home_won"]}
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
    season_end   = seasons["2017"]["end"].replace('/', '-')

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
