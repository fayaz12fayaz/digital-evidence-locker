import mysql.connector
class DataBase_Connection:
    try:
        def connect_db(self):
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="your_password",
                database="digital_evidence_locker"
            )
            return conn
    except mysql.connector.Error as err:
        print(err)
