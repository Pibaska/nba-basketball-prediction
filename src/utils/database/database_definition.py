import sqlite3


def create_database(cursor):
    '''
Criar tabelas no banco de dados

Input:
- cursor: incluir o console do banco de dados

Output:
- nada
    -------
    '''
    cursor.executescript("""
    CREATE TABLE team_participation(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        team_name VARCHAR(50),
        minutes_played INTEGER,
        field_goals INTEGER,
        field_goals_attempts INTEGER,
        field_goals_percentage DECIMAL(4,3),
        par_3point_field_goals INTEGER,
        par_3point_field_goals_attempts INTEGER,
        par_3point_field_goals_percentage DECIMAL(4,3),
        free_throws INTEGER,
        free_throws_attempts INTEGER,
        free_throws_percentage DECIMAL(4,3),
        offensive_rebounds INTEGER,
        defensive_rebounds INTEGER,
        total_rebounds INTEGER,
        assists INTEGER,
        steals INTEGER,
        blocks INTEGER,
        turnover INTEGER,
        personal_faults INTEGER,
        points INTEGER,
        mat_count_by_team INTEGER,
        won BIT,
        team_is_home BIT
    );              
    CREATE TABLE match(
        mat_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        fk_team_home INTEGER NOT NULL,
        fk_team_away INTEGER NOT NULL,
        date DATE NOT NULL,
        count INTEGER NOT NULL,
        FOREIGN KEY (fk_team_home) references team_participation(id),
        FOREIGN KEY (fk_team_away) references team_participation(id)
    );""")
    print('Tabela criada com sucesso.')


if __name__ == "__main__":

    db = sqlite3.connect('data/database.sqlite3')
    cursor = db.cursor()

    create_database(cursor)
