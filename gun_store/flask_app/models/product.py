from pprint import pprint
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash, re
from flask_app.models.product import Product

DATABASE = 'gun_store'

class Product:
    def __init__( self , data:dict):
        self.id=data['id']
        self.product_name= data['product_name']
        # product_name
        self.type= data['type']
        # type
        self.sku= data['sku']
        if "first_name" in data:
            self.first_name=data['first_name']
        if "last_name" in data:
            self.last_name=data['last_name']
        self.user_id=data['user_id']

    @staticmethod
    def validate_product(product:dict):
        print(product)
        is_valid = True 
        if len (product['product_name']) < 2:
            flash ("Product_name must be at least 2 characters.")
            is_valid = False
        if len(product['type']) < 4:
            flash("Type must be at least 4 characters.")
            is_valid = False
        if len(product['sku']) < 3:
            flash("Sku must be at least 4.")
            is_valid = False
        return is_valid

    @classmethod
    def save(cls, data):
        query = "INSERT INTO products (product_name, type, sku, user_id) VALUES(%(product_name)s, %(type)s, %(sku)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_with_user_name(cls):
        query = "SELECT products.*, users.first_name, users.last_name FROM products LEFT JOIN users ON users.id=products.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        products=[]
        for product in results:
            products.append(cls(product))
        print(products)
        return products 

    @classmethod
    def get_one_with_user(cls, data):
        query = "SELECT products.*, users.first_name, users.last_name FROM products LEFT JOIN users ON users.id=products.user_id WHERE products.id=%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        product = cls(results[0])
        print(product.first_name)
        return product
        
    @classmethod
    def get_all_user(cls, data:dict):
        query = "SELECT * FROM products WHERE user_id=%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        products=[]
        for product in results:
            products.append(cls(product))
        print(results)
        return products

    @classmethod
    def delete_product(cls, data):
        query = "DELETE FROM products WHERE id = %(id)s;"
        connectToMySQL(DATABASE).query_db( query, data )

    @classmethod
    def edit_product(cls, data):
        query = "UPDATE products SET product_name=%(product_name)s, type=%(type)s, sku=%(sku)s WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db( query, data )