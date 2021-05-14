from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL

app = Flask(__name__)
@app.route("/")
def index():
    mysql = connectToMySQL('users')
    users = mysql.query_db('SELECT * FROM users')
    print(users)
    return render_template('index.html', all_users = users)

@app.route("/add_user")
def add_user_page():
    return render_template("add_new.html")

@app.route("/create_user", methods=["POST"])
def add_user_to_db():
    mysql = connectToMySQL("users")
    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(fn)s, %(ln)s, %(emal)s, NOW(), NOW());"
    data = {
        "fn": request.form['fname'],
        "ln": request.form['lname'],
        "emal": request.form['eml']
    }
    new_user_id = mysql.query_db(query, data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)