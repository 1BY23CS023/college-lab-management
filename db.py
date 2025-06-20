import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "root1204!",
        database = "labdb")

