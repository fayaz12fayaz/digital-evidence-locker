# digital-evidence-locker
A secure Digital Evidence Locker built with Python and MySQL featuring role-based authentication, evidence management, chain of custody tracking, activity logging, and bcrypt password hashing.


# 🔒 Digital Evidence Locker

A secure, role-based **Digital Evidence Locker** developed using **Python** and **MySQL** for managing digital evidence in law enforcement investigations. The system enables administrators and officers to securely manage cases, evidence, evidence transfers, and user activities while maintaining a complete **Chain of Custody**.

This project was built to demonstrate practical concepts of **Object-Oriented Programming (OOP)**, **Database Management**, **Authentication**, **Password Hashing**, and **Activity Logging** in Python.

---

# 📌 Features

## Authentication & Security

* Secure user login
* Password hashing using **bcrypt**
* Role-based access control
* Parameterized SQL queries to prevent SQL Injection

---

## 👨‍💼 Admin Module

The administrator can:

* Add new officers and administrators
* View all registered users
* Update user details
* Register new criminal cases
* Search case details
* View complete Chain of Custody
* View user login activity
* Logout securely

---

## 👮 Officer Module

The officer can:

* Add digital evidence
* View assigned cases
* Search cases
* Search evidence
* Transfer evidence
* View Chain of Custody
* Logout securely

---

## 🔄 Chain of Custody

The system records every evidence transfer including:

* From Location
* To Location
* Transferred By
* Received By
* Transfer Date & Time
* Transfer Reason

This ensures complete traceability of digital evidence throughout an investigation.

---

## 📋 Login Activity Tracking

Every login session records:

* Login Time
* Logout Time
* User Activity
* Username
* User ID

This creates an audit trail for accountability.

---

# 🛠 Technologies Used

| Technology                  | Purpose               |
| --------------------------- | --------------------- |
| Python                      | Backend Logic         |
| MySQL                       | Database              |
| mysql-connector-python      | Database Connectivity |
| bcrypt                      | Password Hashing      |
| Object-Oriented Programming | Project Architecture  |
| SQL                         | Database Operations   |

---

# 📁 Project Structure

```
Digital-Evidence-Locker/
│
├── main.py
├── database.py
├── user_login.py
├── admin.py
├── officer.py
├── adminoperations.py
├── officeroperations.py
├── login_activity.py
│
├── database/
│   └── schema.sql
│
├── screenshots/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 🗄 Database Tables

The project uses multiple relational tables including:

* users
* cases
* evidence
* evidence_transfers
* login_activity

These tables are connected using foreign key relationships to maintain data integrity.

---

# 🔐 Password Security

Passwords are **never stored in plain text**.

The application uses the **bcrypt** library to hash passwords before storing them in the database.

Example workflow:

```
User Password
      ↓
bcrypt Hashing
      ↓
Store Hashed Password
      ↓
Verify using bcrypt.checkpw()
```

---

# 🚀 Installation

## 1. Clone the repository

```bash
git clone https://github.com/yourusername/digital-evidence-locker.git
```

---

## 2. Move into the project directory

```bash
cd digital-evidence-locker
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Create the MySQL database

```sql
CREATE DATABASE digital_evidence_locker;
```

Import the SQL schema into the database.

---

## 5. Configure database connection

Open `database.py` and update:

```python
host="localhost"
user="your_username"
password="your_password"
database="digital_evidence_locker"
```

---

## 6. Run the application

```bash
python main.py
```

---

# 📷 Screenshots

Add screenshots of the application here.

Examples:

* Login Screen
* Admin Dashboard
* Officer Dashboard
* Add Evidence
* Search Evidence
* Register Case
* Chain of Custody
* Login Activity

---

# 💡 Concepts Demonstrated

* Object-Oriented Programming
* Classes and Objects
* Encapsulation
* Modular Programming
* MySQL Database Connectivity
* CRUD Operations
* Authentication
* Password Hashing
* Activity Logging
* Role-Based Access Control
* Chain of Custody
* Exception Handling
* SQL Queries

---

# 📈 Future Improvements

Some planned enhancements include:

* Graphical User Interface (Tkinter or PyQt)
* File upload support for digital evidence
* Image, video and document storage
* Evidence encryption
* Email notifications
* Dashboard and analytics
* Search filters
* PDF report generation
* REST API using Flask/FastAPI
* JWT Authentication
* Unit Testing
* Docker support

---

# 🎯 Learning Outcomes

This project helped strengthen understanding of:

* Python programming
* Database design
* MySQL
* Authentication systems
* Secure password storage
* Database relationships
* Software modularization
* Real-world software development practices

---

# 👨‍💻 Author

**Fayaz Ahamed**

Bachelor of Computer Applications (BCA)

Python Developer | Aspiring Software Engineer | Interested in Backend Development, Cybersecurity and Data Science

GitHub: https://github.com/fayaz12fayaz

LinkedIn: https://linkedin.com/in/

---

# 📄 License

This project is intended for educational and learning purposes.

Feel free to fork, learn from, and improve the project.

---

## ⭐ Support

If you found this project helpful, consider giving it a **⭐ Star** on GitHub.
