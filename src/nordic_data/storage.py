import sqlite3
from nordic_data.paths import DATA_DIR

# Function is needed so that we can create new databses for sources such as Riksbanken or Nasdaq
def create_table(db_path):

    connection = sqlite3.connect(DATA_DIR / db_path)

    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS observations (
        series_id TEXT NOT NULL,
        date TEXT NOT NULL,
        value REAL,
        PRIMARY KEY (series_id, date)
    )""")

    connection.commit()
    connection.close()