import sqlite3
from sqlite3 import Error

DB_NAME = "user.sqlite3"


def create_connection():
    try:
        con = sqlite3.connect(DB_NAME)
        return con
    except Error as e:
        print("Connection error")
    except Exception as e:
        print(str(e))

CREATE_USERS_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name CHAR(255) NOT NULL,
        last_name CHAR(255) NOT NULL,
        company_name CHAR(255) NOT NULL,
        address CHAR(255) NOT NULL,
        city CHAR(255) NOT NULL,
        county CHAR(255) NOT NULL,
        state CHAR(255) NOT NULL,
        zip REAL NOT NULL,
        phone1 CHAR(255) NOT NULL,
        phone2 CHAR(255),
        email CHAR(255) NOT NULL,
        web text
    );
"""

def main():
    con = create_connection()


if __name__ == "__main__":
    main()