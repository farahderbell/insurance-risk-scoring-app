import pymysql

def get_connection():
    return pymysql.connect(
        host="172.29.48.1",
        user="root",
        password="",
        database="assurance_maghrebia",
        port=3306,
        cursorclass=pymysql.cursors.DictCursor 
    )