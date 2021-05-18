from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class DojoSurvey:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def insert_new_survey(cls,data):
        query = "INSERT INTO dojos (name, location, language, comment, created_at, updated_at) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW());"
        return connectToMySQL("dojo_survey_schema").query_db(query,data)

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(survey_id)s;"
        results = connectToMySQL('dojo_survey_schema').query_db(query,data)
        return cls(results[0])
    
    @staticmethod
    def validate_survey(survey):
        is_valid = True
        if len(survey['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(survey['comment']) < 7:
            flash("Comment must be at least 7 characters.")
            is_valid = False
        if (survey['location']) == "Choose Dojo Location":
            flash("Must pick a location.")
            is_valid = False
        if (survey['language']) == "Choose Favorite Language":
            flash("Must pick a language.")
            is_valid = False
        return is_valid