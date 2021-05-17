from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/new_ninja")
def ninjas_index():
    return render_template('add_ninja.html', all_dojos = Dojo.get_all())

@app.route("/create_ninja", methods=["POST"])
def add_ninja_to_db():
    new_ninja_id = Ninja.insert_new_ninja(request.form)
    return redirect("/dojos")