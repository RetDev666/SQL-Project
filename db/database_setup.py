# db/database_setup.py
import mysql.connector
from config import db_config

# Підключення до бази даних
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Створення таблиць
cursor.execute("""
CREATE TABLE IF NOT EXISTS Materials (
    material_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    unit VARCHAR(20) NOT NULL,
    min_stock_level INT NOT NULL,
    expiration_date DATE
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Storage (
    storage_id INT PRIMARY KEY AUTO_INCREMENT,
    material_id INT NOT NULL,
    location VARCHAR(50),
    stock_level INT,
    FOREIGN KEY (material_id) REFERENCES Materials(material_id)
);
""")

connection.commit()
cursor.close()
connection.close()
