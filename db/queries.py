# db/queries.py
import mysql.connector
from config import db_config

def get_materials():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("SELECT material_id, name, unit, min_stock_level, expiration_date FROM materials")
    materials = cursor.fetchall()
    cursor.close()
    connection.close()
    return materials


def add_material(name, unit, min_stock_level, expiration_date):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO Materials (name, unit, min_stock_level, expiration_date) 
        VALUES (%s, %s, %s, %s)
    """, (name, unit, min_stock_level, expiration_date))
    connection.commit()
    cursor.close()
    connection.close()
# db/queries.py

def move_material(material_id, from_location, to_location, quantity):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO Movements (material_id, from_location, to_location, quantity, movement_date)
        VALUES (%s, %s, %s, %s, CURDATE())
    """, (material_id, from_location, to_location, quantity))
    connection.commit()
    cursor.close()
    connection.close()

def issue_material(material_id, quantity, issued_to, purpose):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO Issues (material_id, quantity, issued_to, purpose, issue_date)
        VALUES (%s, %s, %s, %s, CURDATE())
    """, (material_id, quantity, issued_to, purpose))
    connection.commit()
    cursor.close()
    connection.close()
