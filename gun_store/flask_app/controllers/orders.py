from flask import render_template, redirect, request, session,flash
from flask_app import app, bcrypt
from flask_app.models.user import User
from flask_app.models.order import Order
from flask_app.models.product import Product

@app.route('/new')
def order_new():
    if not session.get('first_name'):
        return redirect ('/')
    return render_template('kart.html')

@app.route('/create_order', methods=['post'])
def create_order():
    if not Order.validate_order(request.form):
        return redirect('/kart')
    orders=Order.save(request.form)
    print(orders)
    return redirect('/dashboard')
    
@app.route('/show/<int:id>')
def show(id):
    data = {'id':id}
    print(id)
    return render_template('show.html', orders=Order.get_one_with_user(data))

@app.route('/delete/<int:id>')
def delete_order(id):
    data = {'id' : id}
    Order.delete_order(data)
    return redirect('/dashboard')
    
@app.route('/edit/<int:id>')
def edit(id):
    data = {'id' : id}
    print(request.form)
    return render_template('edit.html', order=Order.get_one_with_user(data))

@app.route('/edit_order', methods=['POST'])
def handle_edit():
    print(request.form)
    Order.edit_order(request.form)
    return redirect('/dashboard')
