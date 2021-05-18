from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.email import Email

@app.route("/enter_email")
def add_user_page():
    return render_template("enter_email.html")

@app.route("/create_email_record", methods=["POST"])
def add_email_to_db():
    if not Email.validate_email(request.form):
        return redirect('/enter_email')
    new_user_id = Email.insert_new_email(request.form)
    return redirect("/show_all_emails")

@app.route("/show_all_emails")
def index():
    return render_template('show_all_emails.html', all_emails = Email.get_all())
