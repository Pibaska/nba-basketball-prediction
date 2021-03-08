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
from datetime import datetime as dt


#dicionário com começo e final das seasons, de 2000 até 2020
#  começo: season["2015"][start]    fim: season["2015"][end]
seasons = {
"1999": {"start":  "2/11/1999", "end": "19/4/2000"},
"2000": {"start": "31/10/2000", "end": "18/4/2001"},
"2001": {"start": "30/10/2001", "end": "17/4/2002"},
"2002": {"start": "29/10/2002", "end": "16/4/2003"},
"2003": {"start": "28/10/2003", "end": "14/4/2004"},
"2004": {"start":  "2/11/2004", "end": "20/4/2005"},
"2005": {"start":  "1/11/2005", "end": "19/4/2006"},
"2006": {"start": "31/10/2006", "end": "18/4/2007"},
"2007": {"start": "30/10/2007", "end": "16/4/2008"},
"2008": {"start": "28/10/2008", "end": "16/4/2009"},
"2009": {"start": "27/10/2009", "end": "14/4/2010"},
"2010": {"start": "26/10/2010", "end": "13/4/2011"},
"2011": {"start": "25/12/2011", "end": "26/4/2012"},
"2012": {"start": "30/10/2012", "end": "17/4/2013"},
"2013": {"start": "29/10/2013", "end": "16/4/2014"},
"2014": {"start": "28/10/2014", "end": "15/4/2015"},
"2015": {"start": "27/10/2015", "end": "13/4/2016"},
"2016": {"start": "25/10/2016", "end": "12/4/2017"},
"2017": {"start": "17/10/2017", "end": "11/4/2018"},
"2018": {"start": "16/10/2018", "end": "10/4/2019"},
"2019": {"start": "22/10/2019", "end": "11/3/2020"},
"2020": {"start": "22/12/2020", "end": "16/5/2021"}
}

# o AG vai fazer o fit com partidas começadas apos 10 dias do começo da temporadas
# e então o AG vai se moviemtnar para frente no tempo apenas, e usará uma quantidade de jogos
#  Poderiamos previamente selecionar jogos para o fit
# É uma questão importante pois o fit funcionaria com um jogo só de DATA
# todas funções aqui vão rodar dentro de um dia 





#todos jogos do Atlanta Hawks(id=2) em casa a partir do dia '08/01/2000' ate o dia '20/02/2000'
""" 
SELECT * from match_data as md INNER JOIN participation as pt 
    ON md.fk_participation_home = pt.participation_id 
    WHERE pt.fk_team_id = 2 
    and pt.team_is_home = 1
    and md.date > '2000-01-08'
    and md.date < '2000-02-20'
    order by md.date ASC;
"""
#MEDIA da coisa de cima
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

def get_averages(team_id, local, date):
    """Recebe uma data e tras as medias do time a partir do inicio da season ate a data informada
        O primeiro dia da season vem de uma lista

    Args:
        team_id (int), 
        local = 0(casa) ou 1(fora),
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
    strigDate = str(date[0])+"/"+str(date[1])+"/"+str(date[2]) #transforma o date em string
    # descobre de que season é a data, e retorna a data de inicio da mesma
    #seasonStart = seasons[str(date[2])]["start"] if dt.strptime(strigDate, "%d/%m/%Y").date() > dt.strptime(seasons[str(date[2])]["start"], "%d/%m/%Y").date() else seasons[str(int(date[2])-1)]["start"]
    if dt.strptime(strigDate, "%d/%m/%Y").date() > dt.strptime(seasons[str(date[2])]["start"], "%d/%m/%Y").date():
        seasonStart = seasons[str(date[2])]["start"]
    else:   
        seasonStart= seasons[str(int(date[2])-1)]["start"]

    try:
        db_connection = sqlite3.connect('data/database.sqlite3')
        cursor = db_connection.cursor()

        cursor.execute(
                        f""" 
        SELECT 
            AVG(pt.points), 
            AVG(pt.offensive_rebounds),
            AVG(pt.defensive_rebounds),
            AVG(NULLIF(pt.field_goals_percentage,0)),
            AVG(NULLIF(pt.three_point_field_goals_percentage,0)),
            AVG(NULLIF(pt.free_throws_percentage,0)),
            AVG(pt.turnover),
            AVG(pt.assists)
                from match_data as md INNER JOIN participation as pt 
                ON md.fk_participation_away = pt.participation_id 
                WHERE pt.fk_team_id = ? 
                and pt.team_is_home = ?
                and md.date > ?
                and md.date < ?
                order by md.date ASC;   
                """, [team_id, local, str(dt.strptime(seasonStart, "%d/%m/%Y").date()), str(dt.strptime(strigDate, "%d/%m/%Y").date()) ])
        lista = cursor.fetchall()

        return lista

    except Exception as e:
        print(e)
        raise e
    finally:
        db_connection.close()
    




if __name__ == "__main__":
    
    print(dt.strptime("2/05/2000", "%d/%m/%Y").date())
    print(get_averages(2, 0, [20,2,2000]))