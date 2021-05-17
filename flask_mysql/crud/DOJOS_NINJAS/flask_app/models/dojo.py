from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_ninjas').query_db(query)
        dojos = []
        for d in results:
            dojos.append(cls(d))
        return dojos
    
    @classmethod
    def insert_new_dojo(cls,data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL("dojos_ninjas").query_db(query,data)

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(dojo_id)s;"
        results = connectToMySQL('dojos_ninjas').query_db(query,data)
        return cls(results[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE dojos SET name = %(name)s, updated_at = NOW() WHERE id = %(id)s"
        return connectToMySQL('dojos_ninjas').query_db(query,data)
    
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL('dojos_ninjas').query_db(query,data)