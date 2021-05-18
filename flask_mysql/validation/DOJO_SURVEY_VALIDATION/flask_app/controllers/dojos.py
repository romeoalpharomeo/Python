from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.dojo import DojoSurvey

@app.route("/")
def dojos_index():
    return render_template('survey.html')

@app.route('/result', methods=['POST'])
def create_survey():
    if not DojoSurvey.validate_survey(request.form):
        return redirect('/')
    new_survey_id = DojoSurvey.insert_new_survey(request.form)
    return redirect(f"/show_survey_results/{new_survey_id}")

@app.route("/show_survey_results/<int:survey_id>")
def dojos_results(survey_id):
    data = {
        "survey_id": survey_id
    }
    return render_template('showresults.html', survey = DojoSurvey.get_by_id(data))
