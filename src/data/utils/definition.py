import sqlite3
from datetime import datetime, date


def create_database():
    '''
    Criar tabelas no banco de dados

    Input:
    - cursor: incluir o console do banco de dados

    Output:
    - nada
        -------
    '''
    try:
        db_connection = sqlite3.connect('data/database.sqlite3')
        cursor = db_connection.cursor()
        cursor.executescript("""
        CREATE TABLE IF NOT EXISTS participation (
            participation_id        INTEGER NOT NULL PRIMARY KEY,
            fk_team_id              INTEGER NOT NULL,
            team_name               VARCHAR(50),
            team_is_home            BIT NOT NULL,
            minutes_played          VARCHAR(10) NOT NULL,
            field_goals             INTEGER NOT NULL,
            field_goals_attempts    INTEGER NOT NULL,
            field_goals_percentage  DECIMAL(4,3) NOT NULL,
            three_point_field_goals INTEGER NOT NULL,
            three_point_field_goals_attempts INTEGER NOT NULL,
            three_point_field_goals_percentage DECIMAL(4,3) NOT NULL,
            free_throws             INTEGER NOT NULL,
            free_throws_attempts    INTEGER NOT NULL,
            free_throws_percentage  DECIMAL(4,3) NOT NULL,
            offensive_rebounds      INTEGER NOT NULL,
            defensive_rebounds      INTEGER NOT NULL,
            total_rebounds          INTEGER NOT NULL,
            assists                 INTEGER NOT NULL,
            steals                  INTEGER NOT NULL,
            blocks                  INTEGER NOT NULL,
            turnover                INTEGER NOT NULL,
            personal_faults         INTEGER NOT NULL,
            points                  INTEGER NOT NULL,
            mat_count_by_team       INTEGER NOT NULL,
            won                     BIT NOT NULL,
            FOREIGN KEY (fk_team_id) REFERENCES team (team_id)
        );
        CREATE TABLE IF NOT EXISTS match_data(
            match_id                    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            fk_participation_home       INTEGER NOT NULL,
            fk_participation_away       INTEGER NOT NULL,
            date                        DATE NOT NULL,
            FOREIGN KEY (fk_participation_home) references participation (participation_id),
            FOREIGN KEY (fk_participation_away) references participation (participation_id)
        );
        CREATE TABLE IF NOT EXISTS team (
            team_id         INTEGER NOT NULL PRIMARY KEY,
            team_name       VARCHAR(50),
            team_abv        VARCHAR(10)
        );
        
        """)

        db_connection.commit()

        print('Tabela(s) criadas com sucesso.')
    except Exception as exception:
        print(exception)
        raise(exception)
    finally:
        db_connection.close()


def fill_teams():
    try:
        db_connection = sqlite3.connect('data/database.sqlite3')
        cursor = db_connection.cursor()

        cursor.executescript("""
            INSERT INTO team (team_name, team_abv) 
                values
                    ('Anderson Packers', 'AND'),
                    ('Atlanta Hawks', 'ATL'),
                    ('Baltimore Bullets', 'BAL'),
                    ('Brooklyn Nets', 'BRK'),
                    ('Boston Celtics', 'BOS'),
                    ('Buffalo Braves', 'BUF'),
                    ('Capital Bullets', 'CAP'),
                    ('Charlotte Hornets', 'CHO'),
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
        """)

        db_connection.commit()

        print("Team preechido com sucesso.")
    except Exception as exception:
        print(exception)
        raise(exception)
    finally:
        db_connection.close()


def drop_tables():
    try:
        db_connection = sqlite3.connect('data/database.sqlite3')
        cursor = db_connection.cursor()

        cursor.executescript("""
            DROP TABLE IF EXISTS match_data;
            DROP TABLE IF EXISTS participation;
            DROP TABLE IF EXISTS team;
        """)

        db_connection.commit()

        print("Tabela(s) deletadas com sucesso.")
    except Exception as exception:
        print(exception)
        raise(exception)
    finally:
        db_connection.close()

def drop_team():
    try:
        db_connection = sqlite3.connect('data/database.sqlite3')
        cursor = db_connection.cursor()

        cursor.executescript("""
            DROP TABLE IF EXISTS team;
        """)

        db_connection.commit()

        print("team deletado com sucesso.")
    except Exception as exception:
        print(exception)
        raise(exception)
    finally:
        db_connection.close()


if __name__ == "__main__":

    print("""
        Tu quer fazer oq?
        [1] atualizar abreviações
        [2] Deletar bd e recriar vazio
    """)
    escolha = int(input())

    if escolha == 1:
        drop_team()
        create_database()
        fill_teams()
    elif escolha == 2:
        x = input("tem certeza mermão? vai acabar o banco, vai da mrd")
        for i in range(5):
            x = input("tem certeza mermão? "+ str(5 - i))

        drop_tables()
        create_database()
        fill_teams()

