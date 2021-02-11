import sqlite3


def insert_team_participation_data(cursor, data):
    cursor.executemany("INSERT INTO banana VALUES (?, ?)", data)


def retrieve_team_participation_data(cursor):
    cursor.execute("""SELECT * FROM team_participation""")

    rows = cursor.fetchall()
    return rows

def retrieve_match_data(cursor):
    cursor.execute("""SELECT * FROM match""")


if __name__ == "__main__":

    db = sqlite3.connect('data/database.sqlite3')
    cursor = db.cursor()

    fake_team_data = [(2, "def"), (3, "ghi"), (4, "jkl")]

    try:
        cursor.execute("""CREATE TABLE if not exists banana(
        numero INTEGER,
        string VARCHAR(4)
        );""")

        insert_team_participation_data(cursor, fake_team_data)
        print(retrieve_team_participation_data(cursor))
        pass
    except Exception as e:
        print(e)
        raise e
    finally:
        cursor.execute("DROP TABLE banana")
        db.close()
