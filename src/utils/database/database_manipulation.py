import sqlite3


def insert_team_participation_data(cursor, team_data):
    cursor.executemany("""
    INSERT INTO team_participation (
        team_name,
        team_location,
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
        team_is_home,
        fk_match
    ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", team_data)


def insert_match_data(cursor, match_data):
    try:
        cursor.executemany("""
            INSERT INTO match_data (
                fk_team_home,
                fk_team_away,
                date,
                count
            ) VALUES (?, ?, ?, ?);
        """, match_data)
        print("Match data inserted successfully!")
    except Exception as exception:
        print(exception)
        raise exception


def retrieve_team_participation_data(cursor, fk_match, team_is_home):
    return cursor.execute(
        """SELECT * FROM team_participation WHERE fk_match = ? AND team_is_home = ?""", (fk_match, team_is_home))


def retrieve_match_data(cursor, match_id):
    return cursor.execute("""SELECT * FROM match WHERE id = ?""", match_id)


def check_tables(cursor):
    cursor.execute(""" SELECT * FROM team_participation;""")
    print(cursor.fetchall())
    cursor.execute("""SELECT * FROM match_data""")
    print(cursor.fetchall())


if __name__ == "__main__":

    db = sqlite3.connect('data/database.sqlite3')
    cursor = db.cursor()

    fake_team_data = [('Magic', 'Orlando 2', '39:56', 7, 20, 0.350, 0,
                       0, 0.350, 8, 8, 1.000, 4, 5, 9, 1, 1, 0, 5, 4, 22, 3, 0, 1, 1)]
    fake_match_data = [(2, 1, '31-12-2018', 1)]

    try:
        insert_match_data(cursor, fake_match_data)
        check_tables(cursor)
    except Exception as e:
        print(e)
        raise e
    finally:
        db.close()
