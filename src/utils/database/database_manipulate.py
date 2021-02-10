import sqlite3

def insert_team_participation_data(cursor, data):
    examples = [(2, "def"), (3, "ghi"), (4, "jkl")]
    cursor.execute("""CREATE TABLE if not exists banana(
        numero INTEGER,
        string VARCHAR(4)
    );""")
    cursor.executemany("INSERT INTO banana VALUES (?, ?)", examples)

    for row in cursor.execute("SELECT * FROM banana"):
        print(row)
    
    cursor.execute("DROP TABLE banana")

if __name__ == "__main__":
    
    db = sqlite3.connect('data/database.sqlite3')
    cursor = db.cursor()

    fake_team_data = []

    try:
        insert_team_participation_data(cursor, fake_team_data)
    except Exception as e:
        print(e)
    finally:
        db.close()