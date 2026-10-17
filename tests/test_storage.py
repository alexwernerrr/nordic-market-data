from nordic_data.storage import create_table
import sqlite3

def test_create_tables(tmp_path):

    create_table(tmp_path / "test.db")
    create_table(tmp_path / "test.db")
    
    connection = sqlite3.connect(tmp_path / "test.db")
    cursor = connection.cursor()
    name = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    assert ("observations",) in name, "No table called 'observations'"
    connection.close()