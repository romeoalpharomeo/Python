from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User


@app.route("/")
def index():
    return render_template('index.html', all_users = User.get_all())

@app.route("/add_user")
def add_user_page():
    return render_template("add_new.html")

@app.route("/create_user", methods=["POST"])
def add_user_to_db():
    if not User.validate_user(request.form):
        return redirect('/add_user')
    new_user_id = User.insert_new_user(request.form)
    return redirect(f"/show_single_user/{new_user_id}")

@app.route("/show_single_user/<int:id_num>")
def show_single_user_page(id_num):
    data = {
        "id": id_num
    }
    return render_template("show_single_user.html", user = User.get_by_id(data))

@app.route("/edit_user/<int:id_num>")
def edit_user_page(id_num):
    data = {
        "id": id_num
    }
    return render_template("edit_user.html", user = User.get_by_id(data))

@app.route("/edit_user_submit/<int:id_num>", methods=["POST"])
def update_user_in_db(id_num):
    data = {
        "id": id_num,
        "firstname": request.form['firstname'],
        "lastname": request.form['lastname'],
        "email": request.form['email']
    }
    User.update(data)
    return redirect(f"/show_single_user/{id_num}")

@app.route("/delete_this_user/<int:id_num>")
def delete_user_in_db(id_num):
    data = {
        "id": id_num,
    }
    User.delete(data)
    return redirect("/")
