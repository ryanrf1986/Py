from flask import render_template, redirect, request, session,flash
from flask_app import app, bcrypt
from flask_app.models.user import User
from flask_app.models.order import Order
from flask_app.models.product import Product

@app.route('/new')
def product_new():
    if not session.get('first_name'):
        return redirect ('/')
    return render_template('new.html')

@app.route('/create_product', methods=['post'])
def create_product():
    if not Product.validate_product(request.form):
        return redirect('/new')
    products=Product.save(request.form)
    print(products)
    return redirect('/index')
    
@app.route('/show/<int:id>')
def show(id):
    data = {'id':id}
    print(id)
    return render_template('show.html', products=Product.get_one_with_user(data))

@app.route('/delete/<int:id>')
def delete_product(id):
    data = {'id' : id}
    Product.delete_product(data)
    return redirect('/index')
    
@app.route('/edit/<int:id>')
def edit(id):
    data = {'id' : id}
    print(request.form)
    return render_template('edit.html', product=Product.get_one_with_user(data))

@app.route('/edit_product', methods=['POST'])
def handle_edit():
    print(request.form)
    Product.edit_product(request.form)
    return redirect('/index')