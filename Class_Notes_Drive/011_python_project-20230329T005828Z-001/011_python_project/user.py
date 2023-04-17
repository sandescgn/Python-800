import csv
import sqlite3
from sqlite3 import Error

FILE_NAME = "sample_users.csv"
DB_NAME = "sample_users.sqlite3"

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

COLUMNS = (
    "first_name",
    "last_name",
    "company_name",
    "address",
    "city",
    "county",
    "state",
    "zip",
    "phone1",
    "phone2",
    "email",
    "web",
)

INPUT_STRING = """
Enter the option: 
    1. CREATE TABLE
    2. DUMP users from csv INTO users TABLE
    3. ADD new user INTO users TABLE
    4. QUERY all users from TABLE
    5. DELETE all users
    6. DELETE user by id
    7. UPDATE user
    8. Press any key to EXIT
"""

LIMIT = None

NO_OF_ROWS_INPUT_STRING = f"""
How many rows would you like to fetch at once ?
    1. Fetch first 10 records from user table
    2. Fetch specified no. of first n records
    3. Fetch all records from users table
    4. Press any key to EXIT
"""

COLUMN_INPUT_STRING = f"""
Which column would you like to update?. Please make sure column is one of the following:
{COLUMNS} 
"""


def prettier(fn):
    def inner(*args, **kwargs):
        print("*" * 150)
        fn(*args, **kwargs)
        print("*" * 150)

    return inner


def open_csv_file(file_name=FILE_NAME, delimiter=","):
    with open(f"{file_name}") as f:
        csv_reader = csv.reader(f, delimiter=delimiter)
        users = [tuple(row) for row in csv_reader]
        return users[1:]


def create_connection(db_file):
    """
    create a database connection to the SQLite database specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    finally:
        return conn


@prettier
def create_table(conn, create_table_query):
    """create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_query)
        print("Successfully created table.")
    except Error as e:
        raise e


@prettier
def insert_users(conn, users):
    """
    Create a new user into the users table
    :param conn:
    :param user:
    :return: user id
    """
    if not isinstance(users, list):
        users = [tuple(users)]

    sql = """
        INSERT INTO 
        users
            (first_name, last_name, company_name, address, city, county, state, zip, phone1, phone2, email, web)
        VALUES
            (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    cur = conn.cursor()
    cur.executemany(sql, users)
    conn.commit()
    print("Successfully inserted data into table.")
    return cur.lastrowid


@prettier
def delete_user(conn, user_id):
    """
    Delete a user by id of user
    :param conn:  Connection to the SQLite database
    :param id: id of the user
    :return:
    """
    sql = "DELETE FROM users WHERE id=?"
    cur = conn.cursor()
    cur.execute(sql, (user_id,))
    conn.commit()
    print(f"Successfully deleted record with id {user_id}")


@prettier
def delete_all_users(conn):
    """
    Delete all rows in the users table
    :param conn: Connection to the SQLite database
    :return:
    """
    sql = "DELETE FROM users"
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    print(f"Successfully deleted all records")


@prettier
def update_user(conn, user_id, column_name, column_value):
    """
    update priority, begin_date, and end date of a user
    :param conn:
    :param user:
    :return: project id
    """
    sql = f"""UPDATE users SET {column_name} = ? WHERE id = ?;"""
    cur = conn.cursor()
    cur.execute(sql, (column_value, user_id))
    conn.commit()


def select_all_users(conn):
    """
    Query all rows in the users table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")

    rows = cur.fetchall()
    for row in rows:
        row = [str(field) for field in row]
        row = " | ".join(row)
        yield row


def check_options_and_select_users(users):
    print("*" * 150)
    options: str = input(NO_OF_ROWS_INPUT_STRING)

    if options == "1":
        LIMIT = 10

    elif options == "2":
        LIMIT = int(input("Enter valid integer: "))

    elif options == "3":
        LIMIT = None

    else:
        exit()

    if LIMIT:
        for i in range(LIMIT):
            try:
                next_user = next(users)
                print(next_user)
            except StopIteration:
                print("No records found!!! Please insert data first")
                exit()
    else:
        for user in users:
            print(user)
    print("*" * 150)


def main():
    conn = create_connection(DB_NAME)

    while True:
        user_input = input(INPUT_STRING)

        if conn is not None:
            if user_input == "1":
                create_table(conn, CREATE_USERS_TABLE_QUERY)

            elif user_input == "2":
                users = open_csv_file()
                insert_users(conn, users)

            elif user_input == "3":
                data = [input(f"{column}: ") for column in COLUMNS]
                insert_users(conn, tuple(data))

            elif user_input == "4":
                users = select_all_users(conn)
                check_options_and_select_users(users)

            elif user_input == "5":
                confirm = input(
                    "Are you sure you want to delete? Type y or yes to continue or Press n or no to skip."
                ).lower()
                if confirm in ["yes", "y"]:
                    delete_all_users(conn)

            elif user_input == "6":
                user_id = input("Enter id of user: ")
                if user_id.isnumeric():
                    delete_user(conn, user_id)
                else:
                    print("Exiting program.. Id of user should be valid integer.")
                    exit()

            elif user_input == "7":
                user_id = input("Enter id of user to update: ")
                if user_id.isnumeric():
                    column_name = input(COLUMN_INPUT_STRING)
                    column_value = input(f"Enter value of {column_name}: ")
                    update_user(conn, user_id, column_name, column_value)
                else:
                    print("Exiting program.. Id of user should be valid integer.")
                    exit()
            else:
                exit()
        else:
            print("Error! cannot create the database connection.")


if __name__ == "__main__":
    main()
