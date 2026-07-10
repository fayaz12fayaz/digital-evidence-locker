from database import DataBase_Connection
class adminOperation:
    def __init__(self):
        self.db = DataBase_Connection()
        self.conn = self.db.connect_db()
    
    def add_user(self,username,password,role,full_name,email,phone,badge_number,designation,station_name):

        cursor = self.conn.cursor()
        query = """ INSERT INTO users (username, password, role, full_name, email, phone, badge_number,designation,station_name) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) """
        cursor.execute(query,(username,password,role,full_name,email,phone,badge_number,designation,station_name))
        self.conn.commit()
        print("user added successfully!")
        cursor.close()

        cursor.close()

    def view_all_users(self):
        cursor = self.conn.cursor()
        query = "SELECT user_id, username, role FROM users"
        cursor.execute(query)
        users = cursor.fetchall()
        cursor.close()
        return users
    
    def updateDetails(self, user_id, val, choice):
        cursor = self.conn.cursor()

        if choice == 1:
            query = """
                UPDATE users
                SET password = %s
                WHERE user_id = %s
            """

        elif choice == 2:
            query = """
                UPDATE users
                SET phone = %s
                WHERE user_id = %s
            """

        elif choice == 3:
            query = """
                UPDATE users
                SET designation = %s
                WHERE user_id = %s
            """

        elif choice == 4:
            query = """
                UPDATE users
                SET station_name = %s
                WHERE user_id = %s
            """

        elif choice == 5:
            query = """
                UPDATE users
                SET role = %s
                WHERE user_id = %s
            """

        else:
            cursor.close()
            return False

        cursor.execute(query, (val, user_id))
        self.conn.commit()

        if cursor.rowcount > 0:
            cursor.close()
            return True
        else:
            cursor.close()
            return False
        
    def newCase(self, case_title, crime_type, incident_date, location, description, officer_id):
        cursor = self.conn.cursor()
        cursor.execute("select status from users where user_id =%s",(officer_id,))
        self.result=cursor.fetchone()
        if self.result[0].lower()=='active':

            query = """INSERT INTO cases (case_title,crime_type,incident_date,location,description,officer_id)
                        VALUES (%s,%s,%s,%s,%s,%s)"""
            values = (case_title, crime_type, incident_date, location, description, officer_id)
            cursor.execute(query, values)
            print("case details added successfully")
            cursor.execute("select max(case_id) from cases")
            print(f"inserted successfully with case_id = {cursor.fetchone()[0]}")
            self.conn.commit()
            cursor.close()
        else:
            print("officer is Inactive")



        





