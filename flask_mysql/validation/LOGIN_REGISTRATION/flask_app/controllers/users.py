from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def register_or_login():
    return render_template("index.html")

@app.route("/logout/<int:user_id>")
def logout(user_id):
    session.pop('user_id', None)
    return redirect("/")

@app.route("/register_user", methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pw_hash
    }
    user_id = User.insert_new_user(data)
    session['user_id'] = user_id
    return redirect(f"/success/{user_id}")

@app.route("/success/<int:user_id>")
def register_success(user_id):
    if 'user_id' not in session:
        return "You are not logged in <br><a href = '/'>" + "Click Here to Login</a>"
    data = {
        "user_id": user_id
    }
    return render_template('welcome.html', user = User.get_by_id(data))

@app.route("/login_user", methods=['POST'])
def login_success():
    data = { "email": request.form['email']}
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email or Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email or Password")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    # never render on a post!!!
    return redirect(f"/success/{user_in_db.id}")