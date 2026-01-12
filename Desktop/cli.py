from auth import start_auth

def main():
    print("\n💳 WALLETWAY")
    print("Plan Smart. Spend Wise. Explore More.\n")
    start_auth()

if __name__ == "__main__":
    main()
import sqlite3
import hashlib
from user_menu import user_dashboard
from admin_menu import admin_dashboard

def hash_pw(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

def start_auth():
    while True:
        print("\n1. Login\n2. Sign Up\n3. Exit")
        choice = input("> ")

        if choice == "1":
            login()
        elif choice == "2":
            signup()
        else:
            exit()

def login():
    u = input("Username: ")
    p = hash_pw(input("Password: "))

    db = sqlite3.connect("walletway.db")
    cur = db.cursor()

    cur.execute("SELECT id, role FROM users WHERE username=? AND password=?", (u, p))
    user = cur.fetchone()

    if user:
        if user[1] == "admin":
            admin_dashboard(user[0])
        else:
            user_dashboard(user[0])
    else:
        print("❌ Invalid credentials")

def signup():
    u = input("Username: ")
    p = hash_pw(input("Password: "))
    name = input("Name: ")
    college = input("College: ")

    db = sqlite3.connect("walletway.db")
    cur = db.cursor()

    try:
        cur.execute(
            "INSERT INTO users(username,password,role,name,college,pocket_money) VALUES(?,?,?,?,?,?)",
            (u, p, "user", name, college, 0)
        )
        db.commit()
        print("✅ Account created!")
    except:
        print("❌ Username already exists")
from outings import outings_menu
from finance import finance_menu
from safety import safety_menu

def user_dashboard(user_id):
    while True:
        print("""
🏠 USER DASHBOARD
1. Outings Planner
2. Financial Planner
3. Engagement (Coming Soon)
4. Support & Safety
5. Logout
""")
        c = input("> ")

        if c == "1":
            outings_menu(user_id)
        elif c == "2":
            finance_menu(user_id)
        elif c == "4":
            safety_menu()
        elif c == "5":
            break
import sqlite3

def outings_menu(user_id):
    db = sqlite3.connect("walletway.db")
    cur = db.cursor()

    print("\n📍 OUTINGS PLANNER")
    dest = input("Destination: ")
    budget = float(input("Budget: "))
    date = input("Date: ")

    cur.execute(
        "INSERT INTO outings(user_id,destination,budget,date) VALUES(?,?,?,?)",
        (user_id, dest, budget, date)
    )
    db.commit()
    print("✅ Outing planned successfully")
import sqlite3
from datetime import date

def finance_menu(user_id):
    db = sqlite3.connect("walletway.db")
    cur = db.cursor()

    print("\n💸 FINANCIAL PLANNER")
    category = input("Category: ")
    amount = float(input("Amount: "))
    note = input("Note: ")

    cur.execute(
        "INSERT INTO expenses(user_id,category,amount,note,date) VALUES(?,?,?,?,?)",
        (user_id, category, amount, note, str(date.today()))
    )
    db.commit()
    print("✅ Expense recorded")
def safety_menu():
    print("""
🚨 SAFETY & SUPPORT
• Emergency Contacts
• Live Location Sharing (Future)
• Helpdesk: support@walletway
""")
import sqlite3

def admin_dashboard(admin_id):
    db = sqlite3.connect("walletway.db")
    cur = db.cursor()

    while True:
        print("""
🛠️ ADMIN PANEL
1. User Management
2. Content Management
3. Finance Oversight
4. Analytics & Reports
5. System Maintenance
6. Logout
""")
        c = input("> ")

        if c == "1":
            cur.execute("SELECT id, username, role FROM users")
            for u in cur.fetchall():
                print(u)
        elif c == "6":
            break
