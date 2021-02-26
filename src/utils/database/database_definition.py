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
        CREATE TABLE IF NOT EXISTS team_participation (
            team_id INTEGER NOT NULL PRIMARY KEY,
            team_name VARCHAR(50),
            team_is_home BIT NOT NULL,
            minutes_played VARCHAR(10) NOT NULL,
            field_goals INTEGER NOT NULL,
            field_goals_attempts INTEGER NOT NULL,
            field_goals_percentage DECIMAL(4,3) NOT NULL,
            three_point_field_goals INTEGER NOT NULL,
            three_point_field_goals_attempts INTEGER NOT NULL,
            three_point_field_goals_percentage DECIMAL(4,3) NOT NULL,
            free_throws INTEGER NOT NULL,
            free_throws_attempts INTEGER NOT NULL,
            free_throws_percentage DECIMAL(4,3) NOT NULL,
            offensive_rebounds INTEGER NOT NULL,
            defensive_rebounds INTEGER NOT NULL,
            total_rebounds INTEGER NOT NULL,
            assists INTEGER NOT NULL,
            steals INTEGER NOT NULL,
            blocks INTEGER NOT NULL,
            turnover INTEGER NOT NULL,
            personal_faults INTEGER NOT NULL,
            points INTEGER NOT NULL,
            mat_count_by_team INTEGER NOT NULL,
            won BIT NOT NULL,
            fk_match INTEGER NOT NULL,
            FOREIGN KEY (fk_match) REFERENCES match_data (id)
        );
        CREATE TABLE IF NOT EXISTS match_data(
            match_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            fk_team_home INTEGER NOT NULL,
            fk_team_away INTEGER NOT NULL,
            date DATE NOT NULL,                          
            FOREIGN KEY (fk_team_home) references team_participation (id),
            FOREIGN KEY (fk_team_away) references team_participation (id)
        );""")
        print('Tabelas criadas com sucesso.')
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
            DROP TABLE match_data;
            DROP TABLE team_participation;
        """)

        print("Tabelas deletadas com sucesso.")
    except Exception as exception:
        print(exception)
        raise(exception)
    finally:
        db_connection.close()


if __name__ == "__main__":
    drop_tables()
    create_database()
