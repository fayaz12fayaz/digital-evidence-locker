from user_login import userLogIn
from admin import Admin
from officer import Officer
from login_activity import loginAactivity
import bcrypt

login = userLogIn()
admin = Admin()
officer = Officer()
logInAct = loginAactivity()

print("=============DigitalEvidenceLocker==============")
username = input("Enter your Username : ")
password = input("Password : ")


status,role,officer_id = login.login(username,password)

if status:
    logInAct.updateLogInDetails(officer_id,username)
    
    if role == "Admin":
        admin.admin_menu(officer_id)
    elif role == "Officer":
        officer.officer_menu(officer_id)           
else:
    print("invalid username and password")