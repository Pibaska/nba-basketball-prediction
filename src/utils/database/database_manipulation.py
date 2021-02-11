import sqlite3


def insert_team_participation_data(cursor, data):
    cursor.executemany("INSERT INTO banana VALUES (?, ?)", data)


def retrieve_team_participation_data(cursor):
    cursor.execute("""SELECT * FROM banana""")

    rows = cursor.fetchall()
    return rows


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
    except Exception as e:
        print(e)
        raise e
    finally:
        cursor.execute("DROP TABLE banana")
        db.close()
