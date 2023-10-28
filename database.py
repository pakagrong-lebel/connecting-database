# Python script to connect to a database and execute queries
import sqlite3
def connect_to_database(datase_path):
    connection = sqlite3.connect(database_path)
    return connection
def execute_query(connection, query):
cursor = connection.cursor()
cursor.execute(query)
result = cursor.fetchall()
return result