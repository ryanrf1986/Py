from pprint import pprint
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash, re
from flask_app.models.order import Order

DATABASE = 'gun_store'

class Order:
    def __init__( self , data:dict):
        self.id=data['id']
        self.total= data['total']
        # total
        self.status= data['status']
        # status
        # self.price= data['price']
        if "first_name" in data:
            self.first_name=data['first_name']
        if "last_name" in data:
            self.last_name=data['last_name']
        self.user_id=data['user_id']

    @staticmethod
    def validate_order(order:dict):
        print(order)
        is_valid = True 
        if len (order['total']) < 2:
            flash ("Total must be at least 2 characters.")
            is_valid = False
        if len(order['status']) < 4:
            flash("Status must be at least 4 characters.")
            is_valid = False
        # if len(order['price']) < 3:
        #     flash("Price must be at least 1.")
        #     is_valid = False
        return is_valid

    @classmethod
    def save(cls, data):
        query = "INSERT INTO orders (total, status, user_id) VALUES(%(total)s, %(status)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_with_user_name(cls):
        query = "SELECT orders.*, users.first_name, users.last_name FROM orders LEFT JOIN users ON users.id=orders.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        orders=[]
        for order in results:
            orders.append(cls(order))
        print(orders)
        return orders 

    @classmethod
    def get_one_with_user(cls, data):
        query = "SELECT orders.*, users.first_name, users.last_name FROM orders LEFT JOIN users ON users.id=orders.user_id WHERE orders.id=%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        order = cls(results[0])
        print(order.first_name)
        return order
        
    @classmethod
    def get_all_user(cls, data:dict):
        query = "SELECT * FROM orders WHERE user_id=%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        orders=[]
        for order in results:
            orders.append(cls(order))
        print(results)
        return orders

    @classmethod
    def delete_order(cls, data):
        query = "DELETE FROM orders WHERE id = %(id)s;"
        connectToMySQL(DATABASE).query_db( query, data )

    @classmethod
    def edit_order(cls, data):
        query = "UPDATE orders SET total=%(total)s, status=%(status)s WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db( query, data )