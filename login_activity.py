from database import DataBase_Connection

class loginAactivity:
    def __init__(self):
        self.db = DataBase_Connection()
        self.conn = self.db.connect_db()

    def updateLogInDetails(self,user_id,username):
        cursor = self.conn.cursor()
        # self.username = username
        # qurey = """ SELECT username from users
        #             where user_id = %s """
        # cursor.execute(qurey,(user_id,))
        # self.username = cursor.fetchone()[0]

        qurey = """ INSERT INTO login_activity (user_id,username) values (%s,%s)"""
        cursor.execute(qurey,(user_id,username))
        self.conn.commit()
        cursor.close()

    def update_logout(self,user_id):
        cursor = self.conn.cursor()
        qurey = """UPDATE login_activity
                SET logout_time = NOW()
                WHERE user_id = %s
                AND logout_time IS NULL
                ORDER BY login_time DESC
                LIMIT 1"""
        cursor.execute(qurey,(user_id,))
        self.conn.commit()
        cursor.close()
        return None
    
    def activity(self, act, user_id):
        cursor = self.conn.cursor()

        query = """
        UPDATE login_activity
        SET activity = CONCAT(IFNULL(activity,''), '\n', %s)
        WHERE user_id = %s
        AND logout_time IS NULL
        ORDER BY login_time DESC
        LIMIT 1
        """

        cursor.execute(query, (act, user_id))
        self.conn.commit()

        print("Rows Updated:", cursor.rowcount)

        cursor.close()





        
        