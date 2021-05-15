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

@app.route("/show_single_user/<int:id_num>")
def show_single_user_page(id_num):
    mysql = connectToMySQL("users")
    single_user = "SELECT * FROM users WHERE id = %(userID)s;"
    data = {
        "userID": id_num
    }
    show_this_user = mysql.query_db(single_user, data)
    print(show_this_user)
    return render_template("show_single_user.html", user = show_this_user, userid = id_num)

@app.route("/edit_user/<int:id_num>")
def edit_user_page(id_num):
    mysql = connectToMySQL("users")
    single_user = "SELECT * FROM users WHERE id = %(userID)s;"
    data = {
        "userID": id_num
    }
    show_this_user = mysql.query_db(single_user, data)
    user_ID = id_num
    return render_template("edit_user.html", id_num = user_ID, user_info = show_this_user)

@app.route("/edit_user_submit/<int:id_num>", methods=["POST"])
def update_user_in_db(id_num):
    mysql = connectToMySQL("users")
    query = "UPDATE users SET first_name = %(fn)s, last_name = %(ln)s, email = %(emal)s, updated_at = NOW() WHERE id = %(userID)s"
    print(query)
    data = {
        "userID": id_num,
        "fn": request.form['fname'],
        "ln": request.form['lname'],
        "emal": request.form['eml']
    }
    edit_user_complete = mysql.query_db(query, data)
    return redirect("/")

@app.route("/delete_this_user/<int:id_num>")
def delete_user_in_db(id_num):
    mysql = connectToMySQL("users")
    query = "DELETE FROM users WHERE id = %(userID)s;"
    print(query)
    data = {
        "userID": id_num,
    }
    delete_user_complete = mysql.query_db(query, data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)