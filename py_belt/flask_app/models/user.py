from pprint import pprint
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash, re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

DATABASE = 'belt'

class User:
    def __init__( self , data:dict):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.password = data['password']
        self.email = data ['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Now we use class methods to query our database

    @staticmethod
    def validate_user(user:dict):
        is_valid = True 
        if len (user['first_name']) < 2:
            flash ("First name must be at least 2 characters.")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last name must be at least 2 characters.")
            is_valid = False
        if len(user['password']) <8:
            flash("password must be at least 8 characters")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']):
            flash("invalid email")
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash("passwords do not match")
            is_valid = False
        return is_valid

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email= %(email)s"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if len(result)<1:
            return False
        return cls(result[0])

    @classmethod
    def get_one(cls, data:dict):
        query = "SELECT * FROM users WHERE id=%(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        print(result)
        return cls(result[0])

    @classmethod
    def update_user(cls, data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db( query, data )

    @classmethod
    def get_with_user_name(cls):
        query = "SELECT paintings.*, users.first_name FROM paintings LEFT JOIN users ON users.id=paintings.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        paintings=[]
        for painting in results:
            paintings.append(cls(painting))
        print(paintings)
        return paintings