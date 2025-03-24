from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Create a database if it doesn't exist
def create_db():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            category TEXT,
            amount REAL
        )
    ''')
    conn.commit()
    conn.close()

create_db()

@app.route("/")
def index():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    data = cursor.fetchall()
    conn.close()
    return render_template("index.html", data=data)

@app.route("/add", methods=["POST"])
def add_expense():
    date = request.form["date"]
    category = request.form["category"]
    amount = request.form["amount"]

    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (date, category, amount) VALUES (?, ?, ?)", (date, category, amount))
    conn.commit()
    conn.close()
    
    return redirect("/")

@app.route("/delete/<int:id>")
def delete_expense(id):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    
    return redirect("/")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_expense(id):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    if request.method == "POST":
        date = request.form["date"]
        category = request.form["category"]
        amount = request.form["amount"]
        cursor.execute("UPDATE expenses SET date = ?, category = ?, amount = ? WHERE id = ?", (date, category, amount, id))
        conn.commit()
        conn.close()
        return redirect("/")
    
    cursor.execute("SELECT * FROM expenses WHERE id = ?", (id,))
    expense = cursor.fetchone()
    conn.close()
    
    return render_template("edit.html", expense=expense)

if __name__ == "__main__":
    app.run(debug=True)
