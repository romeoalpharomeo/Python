from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/dojos")
def dojos_index():
    return render_template('dojos_main.html', all_dojos = Dojo.get_all())

@app.route("/create_dojo", methods=["POST"])
def add_dojo_to_db():
    new_dojo_id = Dojo.insert_new_dojo(request.form)
    return redirect("/dojos")

@app.route("/display_ninjas/<int:dojo_id>")
def display_ninjas_this_dojo(dojo_id):
    data = {
        "dojo_id": dojo_id
    }
    return render_template('display_ninjas_this_dojo.html', dojo = Dojo.get_by_id(data), all_ninjas = Ninja.get_ninjas_by_dojo_id(data))


