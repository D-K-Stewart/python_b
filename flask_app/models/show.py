from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

from flask_app.models.user import User
import re


# DATABASE = ''

class Show:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.title = db_data['title']
        self.network = db_data['network']
        self.release_date = db_data['release_date']
        self.description = db_data['description']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.user_id = db_data['user_id']
        
    @property  
    def creator(self):
        return User.get_one({'id': self.user_id})
# ----------------------------------------------------------------C

    @classmethod # doesn't taget the instance but instead targets the class itself
    def create(cls,data):
        query = "INSERT INTO shows (title, network, release_date, description, created_at, updated_at, user_id) VALUES (%(title)s, %(network)s, %(release_date)s, %(description)s, NOW(), NOW(), %(user_id)s);"
        return connectToMySQL('python_belt').query_db(query, data)
    
        # list of dictionaries

    # ---------------------------------------------------------------R

    @classmethod # doesn't taget the instance but instead targets the class itself
    def get_all(cls):
        query = "SELECT * FROM shows"
        results = connectToMySQL('python_belt').query_db(query)  #list of dictionaries
        
        print(results)
        if len(results):
            all_shows = []
            for shows in results:
                all_shows.append(cls(shows))
            return all_shows



    @classmethod # doesn't taget the instance but instead targets the class itself
    def update(cls, data):
        query = "UPDATE shows SET title=%(title)s, network=%(network)s, release_date=%(release_date)s, description=%(description)s WHERE id=%(id)s;"
        return connectToMySQL('python_belt').query_db(query, data)


    @classmethod # doesn't taget the instance but instead targets the class itself
    def get_one(cls, data):
        query = "SELECT * FROM shows WHERE shows.id = %(id)s;"
        results = connectToMySQL('python_belt').query_db(query, data)  #list of dictionaries
        if not results:
            return results

        data = {
            **results[0]
        }
        return cls(data)
    

    @classmethod 
    def delete_show(cls, data):
        query = "DELETE FROM shows WHERE id=%(id)s;"
        return connectToMySQL('python_belt').query_db(query, data)



    @staticmethod
    def validate_show(show):
        is_valid = True # we assume this is true
        if len(show['title']) < 3:
            flash("Title must be at least 3 characters.", 'error_show_title')
            is_valid = False
        if len(show['network']) < 2:
            flash("Network must be at least 3 characters.", 'error_show_network')
            is_valid = False
        # if len(show['release_date']) < 0:
        #     flash("Month Day Year must be given.", 'error_release_date')
        #     is_valid = False
        if len(show['description']) < 3:
            flash("Description must be at least 3 characters.", 'error_description')
            is_valid = False

        return is_valid