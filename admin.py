from adminoperations import adminOperation
from officeroperations import officerOperation
from login_activity import loginAactivity
import bcrypt

class Admin:
    def __init__(self):
        self.ad_oper = adminOperation()
        self.off_oper = officerOperation()
        self.logInAct = loginAactivity()

    def admin_menu(self, officer_id):
        Running = True

        while Running == True:
                print("""
                        ==============================
                        DIGITAL EVIDENCE LOCKER
                                ADMIN MENU
                        ==============================
                        1. Add User
                        2. View All Officers and Admins
                        3. Update User
                        4. Search Case
                        5. View Chain of Custody
                        6. Register new case
                        7. Logout""")
                
                choice = int(input("Enter your choice : "))

                if choice == 1:
                        self.logInAct.activity("Add Officer",officer_id)
                        username = input("Enter username : ")
                        password = input("Enter password : ")
                        password = bcrypt.hashpw(
                                password.encode(),
                                bcrypt.gensalt()
                        ).decode()
                        role = input("enter role (admin/officer) : ")
                        full_name = input("enter full name : ")
                        email =input("Enter mail :")
                        phone = input("enter phone number :")
                        badge_number = input("enter badge_number :")
                        designation = input("enter designation :")
                        station_name = input("enter station_name :")

                        self.ad_oper.add_user(username,password,role,full_name,email,phone,badge_number,designation,station_name)

                elif choice == 2:
                        print("Before activity")
                        self.logInAct.activity("Viewed All Officers and Admins", officer_id)
                        print("After activity")
                                                
                        users = self.ad_oper.view_all_users()
                        print("-------------ALL Officers and Admins Details--------------- ")
                        for user in users:
                                print(F"""UserID   : {user[0]}
                                        Username   : {user[1]}
                                        Role       : {user[2]}""")
                                print('-'*50)

                elif choice == 3:
                        self.logInAct.activity("updated deails",officer_id)

                        print("--------------update deails--------------------------- ")  
                        user_id = int(input("enter officer ID : "))
                        print("""
                                        1.Password
                                        2.Phone Number 
                                        3.Designation
                                        4.station_name
                                        5.role """)   
                        choice = int(input("Enter your choice : "))  
                        if choice == 1:
                                password = input("Enter your New password : ")
                                result = self.ad_oper.updateDetails(user_id,password,choice)

                                if result:
                                        print("password updated successfully")
                                else:
                                        print("userID not found")
                        elif choice == 2:
                                number  = input("Enter your New password : ")
                                result = self.ad_oper.updateDetails(user_id,number,choice)

                                if result:
                                        print("number updated successfully")
                                else:
                                        print("userID not found")
                        elif choice == 3:
                                Designation  = input("Enter your New Designation : ")
                                result = self.ad_oper.updateDetails(user_id,Designation,choice)

                                if result:
                                        print("Designation updated successfully")
                                else:
                                        print("userID not found")
                        elif choice == 4:
                                station_name  = input("Enter your New station_name : ")
                                result = self.ad_oper.updateDetails(user_id,station_name,choice)

                                if result:
                                        print("station_name updated successfully")
                                else:
                                        print("userID not found")
                        elif choice == 5:
                                role  = input("Enter your New role : ")
                                result = self.ad_oper.updateDetails(user_id,role,choice)

                                if result:
                                        print("role updated successfully")
                                else:
                                        print("userID not found")
                        else:
                                print("invalid choice")  
                elif choice == 4:
                        self.logInAct.activity("searchCase",officer_id)

                        case_id = int(input("Enter the Case ID: "))
                        case_details = self.off_oper.searchCase(case_id)

                        for case in case_details:
                                print("-" * 50)
                                print(f"Case Title    : {case[0]}")
                                print(f"Crime Type    : {case[1]}")
                                print(f"Incident Date : {case[2]}")
                                print(f"Location      : {case[3]}")
                                print(f"Description   : {case[4]}")
                                print(f"Status        : {case[5]}")
                                print("-" * 50)

                elif choice == 5:
                        self.logInAct.activity(" Chain of Custody ",officer_id)
                                               
                        evidence_id = input("Enter evidence_id(EV001): ")
                        records = self.off_oper.viewChainOfCustody(evidence_id)

                        if not records:
                                print("No transfer history found.")
                        else:
                                print("\n========== Chain of Custody ==========\n")

                        for record in records:
                                print(f"Transfer ID     : {record[0]}")
                                print(f"Evidence ID     : {record[1]}")
                                print(f"From Location   : {record[2]}")
                                print(f"To Location     : {record[3]}")
                                print(f"Transferred By  : {record[4]}")
                                print(f"Received By     : {record[5]}")
                                print(f"Transfer Date   : {record[6]}")
                                print(f"Reason          : {record[7]}")
                                print("-" * 50)
                elif choice == 6:
                        self.logInAct.activity(" Register new case ",officer_id)

                        print("----------Register new case------------")
                        case_title = input("enter case_title : ")
                        crime_type = input("enter crime_type : ")
                        incident_date = input("enter when incident happend date (yyyy-mm-dd) :  ")
                        location = input("Enter the location where it happend : ")
                        description = input("Enter the description of the case : ")
                        assigned_officer_id = int(input("enter officer_id to asign : "))

                        self.ad_oper.newCase(case_title, crime_type, incident_date, location, description, assigned_officer_id)

                elif choice == 7:
                        self.logInAct.activity("logged out",officer_id)

                        self.logInAct.update_logout(officer_id,)
                        print("Logging out................")
                        print("Thank you")
                        Running = False
                else:
                        print("invalid choice")