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
import datetime



# criar lista com inicio das temporadas

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
  AVG(pt.points),
  AVG(pt.offensive_rebounds) ,--Offensive Rebound h/a
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

def get_averages(date):
    """Recebe uma data e tras as medias do time a partir do inicio da season ate a data informada
        O primeiro dia da season vem de uma lista

    Args:
        dia: O dia final 
        mes: O mes final
        ano: O ano final

    Returns:
        bool: True se o ano do input for bissexto
    """
