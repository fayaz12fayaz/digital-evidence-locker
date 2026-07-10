from database import DataBase_Connection
import bcrypt

class userLogIn():
    def __init__(self):
        self.db = DataBase_Connection()
        self.conn = self.db.connect_db()
        
    def login(self,username,password):
        self.username = username
        self.password = password 

        cursor = self.conn.cursor()
        query = "SELECT password,role,user_id from users WHERE username =  %s"


        cursor.execute(query,(username,))
        user = cursor.fetchone()

        if user is None:
            return False,None,None

        stored_hash = user[0].encode()

        if bcrypt.checkpw(
            password.encode(),
            stored_hash
        ):
            return True,user[1],user[2]
        else:
            return False,None,None

