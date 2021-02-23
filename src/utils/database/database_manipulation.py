import sqlite3


def insert_team_participation_data(team_data):
    try:
        db_connection = sqlite3.connect('data/database.sqlite3')
        cursor = db_connection.cursor()

        cursor.executemany("""
        INSERT INTO team_participation (
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
            won,
            fk_match
        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", team_data)

        db_connection.commit()
        print("Team participation data inserted successfully")
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
                fk_team_home,
                fk_team_away,
                date,
                count
            ) VALUES (?, ?, ?, ?);
        """, match_data)

        db_connection.commit()
        print("Match data inserted successfully")
    except Exception as e:
        print(e)
        raise e
    finally:
        db_connection.close()


def retrieve_team_participation_data(match_id, team_is_home):
    try:
        db_connection = sqlite3.connect('data/database.sqlite3')
        cursor = db_connection.cursor()

        cursor.execute(
            """SELECT * FROM team_participation WHERE fk_match = ? AND team_is_home = ?""", (match_id, team_is_home))
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


def check_tables():
    try:
        db_connection = sqlite3.connect('data/database.sqlite3')
        cursor = db_connection.cursor()

        cursor.execute(""" SELECT * FROM team_participation;""")
        print(cursor.fetchall())
        cursor.execute("""SELECT * FROM match_data""")
        print(cursor.fetchall())
    except Exception as e:
        print(e)
        raise e
    finally:
        db_connection.close()


if __name__ == "__main__":

    fake_team_data = [('Magic', 'Orlando 2', '39:56', 7, 20, 0.350, 0,
                       0, 0.350, 8, 8, 1.000, 4, 5, 9, 1, 1, 0, 5, 4, 22, 3, 1, 0, 1)]
    fake_match_data = [(2, 1, '31-12-2018', 1)]

    check_tables()
