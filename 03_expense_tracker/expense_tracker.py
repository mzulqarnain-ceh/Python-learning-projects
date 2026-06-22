import sqlite3
import os
from datetime import date
folder=os.path.dirname(__file__)
path=os.path.join(folder,"expense.db")
conn=sqlite3.connect(path)
cursor=conn.cursor()
cursor.execute("create table if not exists expense(id INTEGER PRIMARY KEY AUTOINCREMENT, amount REAL, category TEXT, description TEXT, date TEXT)")
# Add Expense function
def add_expense():
    try:
        amount=float(input("Enter amount: "))
        if amount<=0:
            print("Enter amount that is greater than zero")
            return
    except ValueError:
        print("Please enter a valid amount")
        return
    category=input("Enter category: ")
    description=input("Enter description: ")
    if category== "" or description== "":
        print("Category and description cannot be empty")
        return
    today=str(date.today())
    cursor.execute("insert into expense(amount,category,description,date) values(?,?,?,?)",(amount,category,description,today))
    conn.commit()
    print("Expense added successfully")        
def view_all_expenses():
    cursor.execute("select * from expense")
    rows=cursor.fetchall()
    if len(rows)==0:
        print("No expenses found")
    else:
        for r in rows:
            print(f"ID: {r[0]} | amount:Rs {r[1]} | Category: {r[2]} | Description: {r[3]} | Date: {r[4]}")
def view_category_summary():
    print("Categories available are:")
    cursor.execute("SELECT DISTINCT category FROM expense")
    rows=cursor.fetchall()
    for r in rows:
        print(r[0])
    cat=input("Enter a category to get the summary of that category: ")
    cursor.execute("SELECT category, SUM(amount) FROM expense WHERE category = ? GROUP BY category",(cat,))
    rows=cursor.fetchall()
    if len(rows)==0:
        print("No expenses found in this category")
    else:
        for r in rows:
            print(f"Category: {r[0]} | Amount: Rs {r[1]}")
def view_monthly_summary():
    query=" SELECT SUBSTR(date,1,7), SUM(amount) FROM expense GROUP BY SUBSTR(date,1,7)"
    cursor.execute(query)
    rows=cursor.fetchall()
    if len(rows)==0:
        print("No expense found")
    else:
        for r in rows:
            print(f"Month: {r[0]} | Amount: Rs {r[1]}")
def delete_expense():
    try:
        expense_id=int(input("Enter the id of expense you want to delete: "))
    except ValueError:
        print("Please enter a valid id")
        return
    query="SELECT * FROM expense WHERE id=?"
    cursor.execute(query,(expense_id,))
    rows=cursor.fetchone()
    if rows is None:
        print("No expense found")
    else:
        cursor.execute("DELETE FROM expense WHERE id=?",(expense_id,))
        conn.commit()
        print("Expense deleted successfully")
#menu
while True:
    print("""
    1 for add expense
    2 for view all expenses
    3 for view category summary
    4 for view monthly summary
    5 for delete expense
    6 for exit""")
    try:
        c=int(input("Enter your choice: "))
    except ValueError:
        print("Enter a valid choice")
        continue
    if c==1:
        add_expense()
    elif c==2:
        view_all_expenses()
    elif c==3:
        view_category_summary()
    elif c==4:
        view_monthly_summary()
    elif c==5:
        delete_expense()
    elif c==6:
        break
    else:
        print("Please enter a valid choice")
conn.close()