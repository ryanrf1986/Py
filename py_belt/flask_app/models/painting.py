from pprint import pprint
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash, re
from flask_app.models.user import User

DATABASE = 'belt'

class Painting:
    def __init__( self , data:dict):
        self.id=data['id']
        self.title= data['title']
        # title
        self.description= data['description']
        # description
        self.price= data['price']
        if "first_name" in data:
            self.first_name=data['first_name']
        if "last_name" in data:
            self.last_name=data['last_name']
        self.user_id=data['user_id']

    @staticmethod
    def validate_painting(painting:dict):
        print(painting)
        is_valid = True 
        if len (painting['title']) < 2:
            flash ("Title must be at least 2 characters.")
            is_valid = False
        if len(painting['description']) < 10:
            flash("Description must be at least 10 characters.")
            is_valid = False
        if len(painting['price']) < 3:
            flash("Price must be at least 1.")
            is_valid = False
        return is_valid

    @classmethod
    def save(cls, data):
        query = "INSERT INTO paintings (title, description, price, user_id) VALUES(%(title)s, %(description)s, %(price)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_with_user_name(cls):
        query = "SELECT paintings.*, users.first_name, users.last_name FROM paintings LEFT JOIN users ON users.id=paintings.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        paintings=[]
        for painting in results:
            paintings.append(cls(painting))
        print(paintings)
        return paintings 

    @classmethod
    def get_one_with_user(cls, data):
        query = "SELECT paintings.*, users.first_name, users.last_name FROM paintings LEFT JOIN users ON users.id=paintings.user_id WHERE paintings.id=%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        painting = cls(results[0])
        print(painting.first_name)
        return painting
        
    @classmethod
    def get_all_user(cls, data:dict):
        query = "SELECT * FROM paintings WHERE user_id=%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        paintings=[]
        for painting in results:
            paintings.append(cls(painting))
        print(results)
        return paintings

    @classmethod
    def delete_painting(cls, data):
        query = "DELETE FROM paintings WHERE id = %(id)s;"
        connectToMySQL(DATABASE).query_db( query, data )

    @classmethod
    def edit_painting(cls, data):
        query = "UPDATE paintings SET title=%(title)s, description=%(description)s, price=%(price)s WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db( query, data )