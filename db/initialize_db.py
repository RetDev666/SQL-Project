# db/initialize_db.py
import mysql.connector
from mysql.connector import errorcode
from db.config import db_config

TABLES = {}

# SQL для створення таблиці materials
TABLES['materials'] = """
CREATE TABLE IF NOT EXISTS materials (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    unit VARCHAR(50),
    min_stock_level INT,
    expiration_date DATE
);
"""

# SQL для створення таблиці issues
TABLES['issues'] = """
CREATE TABLE IF NOT EXISTS issues (
    id INT AUTO_INCREMENT PRIMARY KEY,
    material_id INT NOT NULL,
    quantity INT NOT NULL,
    issued_to VARCHAR(255),
    purpose VARCHAR(255),
    issue_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (material_id) REFERENCES materials(id) ON DELETE CASCADE
);
"""

def create_database(cursor):
    try:
        cursor.execute(f"CREATE DATABASE {db_config['database']} DEFAULT CHARACTER SET 'utf8'")
    except mysql.connector.Error as err:
        print(f"Помилка при створенні бази даних: {err}")
        exit(1)

def initialize_database():
    # Підключення до MySQL
    cnx = mysql.connector.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password']
    )
    cursor = cnx.cursor()

    # Перевіряємо, чи існує база даних
    try:
        cnx.database = db_config['database']
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor)
            cnx.database = db_config['database']
        else:
            print(err)
            exit(1)

    # Створюємо таблиці
    for table_name, ddl in TABLES.items():
        try:
            print(f"Створення таблиці {table_name}...")
            cursor.execute(ddl)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print(f"Таблиця {table_name} вже існує.")
            else:
                print(err.msg)

    cursor.close()
    cnx.close()

if __name__ == "__main__":
    initialize_database()
