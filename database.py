import mysql.connector
class DataBase_Connection:
    def connect_db(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="digital_evidence_locker"
        )
        return conn