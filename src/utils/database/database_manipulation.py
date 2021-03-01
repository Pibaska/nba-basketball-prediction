import sqlite3
import datetime


def insert_teams_data(team_data):
    try:
        db_connection = sqlite3.connect('data/database.sqlite3')
        cursor = db_connection.cursor()

        cursor.executemany("""
        INSERT INTO team (
            team_id,
            team_name,
            team_abv
        ) VALUES (?,?,?)""", team_data)

        db_connection.commit()
        print("Team data inserted successfully")
    except Exception as e:
        print(e)
        raise e
    finally:
        db_connection.close()


def insert_participation_data(participation_data):
    try:
        db_connection = sqlite3.connect('data/database.sqlite3')
        cursor = db_connection.cursor()

        cursor.executemany("""
        INSERT INTO participation (
            participation_id,
            fk_team_id,
            team_name,
            team_is_home,
            minutes_played,
            field_goals,
            field_goals_attempts,
            field_goals_percentage,
            three_point_field_goals,
            three_point_field_goals_attempts,
            three_point_field_goals_percentage,
            free_throws,
            free_throws_attempts,
            free_throws_percentage,
            offensive_rebounds,
            defensive_rebounds,
            total_rebounds,
            assists,
            steals,
            blocks,
            turnover,
            personal_faults,
            points,
            mat_count_by_team,
            won
        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", participation_data)

        db_connection.commit()
        print("Participation data inserted successfully")
    except Exception as e:
        print(e)
        raise e
    finally:
        db_connection.close()


def insert_match_data(match_data):

    try:
        db_connection = sqlite3.connect('data/database.sqlite3')
        cursor = db_connection.cursor()

        cursor.executemany("""
            INSERT INTO match_data (
                fk_participation_home,
                fk_participation_away,
                date
            ) VALUES (?, ?, ?);
        """, match_data)

        db_connection.commit()
        print("Match data inserted successfully")
    except Exception as e:
        print(e)
        raise e
    finally:
        db_connection.close()


def retrieve_participation_data(match_id, team_is_home):
    try:
        db_connection = sqlite3.connect('data/database.sqlite3')
        cursor = db_connection.cursor()

        cursor.execute(
            """SELECT * FROM participation WHERE fk_match_id = ? AND team_is_home = ?""", (match_id, team_is_home))
        return(cursor.fetchall())
    except Exception as e:
        print(e)
        raise e
    finally:
        db_connection.close()


def retrieve_match_data(match_id):
    try:
        db_connection = sqlite3.connect('data/database.sqlite3')
        cursor = db_connection.cursor()

        cursor.execute("""SELECT * FROM match_data WHERE id = ?""", match_id)
        return(cursor.fetchall())
    except Exception as e:
        print(e)
        raise e
    finally:
        db_connection.close()


def dict_factory(cursor, row):
    new_dict = {}
    for value_index, column in enumerate(cursor.description):
        new_dict[column[0]] = row[value_index]
    return new_dict


def retrieve_data_as_dict():
    try:
        db_connection = sqlite3.connect("data/database.sqlite3")
        db_connection.row_factory = dict_factory
        cursor = db_connection.cursor()
        cursor.execute(
            """
            SELECT * FROM match_data as md 
            INNER JOIN participation as home_tp 
            ON md.fk_participation_home = home_tp.participation_id
            INNER JOIN participation as away_tp
            ON md.fk_participation_away = away_tp.participation_id;""")
        print(cursor.fetchone())
    except Exception as e:
        print(e)
        raise e
    finally:
        db_connection.close()


def check_tables():
    try:
        db_connection = sqlite3.connect('data/database.sqlite3')
        cursor = db_connection.cursor()

        cursor.execute(""" SELECT * FROM participation;""")
        print(cursor.fetchall())
        cursor.execute("""SELECT * FROM match_data;""")
        print(cursor.fetchall())
        cursor.execute(""" SELECT * FROM team;""")
        print(cursor.fetchall())
    except Exception as e:
        print(e)
        raise e
    finally:
        db_connection.close()


def create_id_participation():
    try:
        db_connection = sqlite3.connect('data/database.sqlite3')
        cursor = db_connection.cursor()

        cursor.execute(
            """ SELECT participation_id FROM participation ORDER BY participation_id DESC  ;""")
        lista = cursor.fetchall()

        try:
            team_id = lista[0][0]
            return team_id + 1

        except Exception as e:
            return 0

    except Exception as e:
        print(e)
        raise e
    finally:
        db_connection.close()


def get_datetime(date):
    return datetime.date(date[2], date[1], date[0])


def get_last_date():
    """Gera uma lista de datas no formato [ano,mes,dia] começando pelo ultimo dia+1 que temos dados no banco

    Returns:
        list: A lista de datas formatadas como listas [ano,mes,dia]
    """
    try:
        db_connection = sqlite3.connect('data/database.sqlite3')
        cursor = db_connection.cursor()

        cursor.execute("""SELECT date FROM match_data ORDER BY date DESC""")
        dates = cursor.fetchall()

        try:
            formatted_date = dates[0][0].split("-")
            formatted_date[0] = int(formatted_date[0])  # ano
            formatted_date[1] = int(formatted_date[1])  # mes
            formatted_date[2] = int(formatted_date[2])  # dia

            formatted_date[2] += 1  # dia aumenta 1 pra começar no dia seguinte

            return formatted_date

        except Exception as e:
            return [2000, 1, 1]

    except Exception as e:
        print(e)
        raise e
    finally:
        db_connection.close()


if __name__ == "__main__":

    # fake_team_data = [('Magic', 'Orlando 2', '39:56', 7, 20, 0.350, 0,
    #                    0, 0.350, 8, 8, 1.000, 4, 5, 9, 1, 1, 0, 5, 4, 22, 3, 1, 0, 1)]
    # fake_match_data = [(2, 1, '31-12-2018', 1)]

    retrieve_data_as_dict()
    # SELECT * FROM match_data as md INNER JOIN participation as tp ON md.fk_participation_home = tp.team_id;
