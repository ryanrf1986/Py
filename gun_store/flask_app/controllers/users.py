from flask import render_template, redirect, request, session,flash
from flask_app import app, bcrypt
from flask_app.models.user import User
from flask_app.models.product import Product
from flask_app.models.order import Order

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register/user', methods = ['POST'])
def register():
    if User.get_by_email(request.form):
        flash("email already registered")
        return redirect('/')
    if not User.validate_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : pw_hash
    }
    user_id=User.save(data)
    session['user_id'] = user_id
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    return redirect('/index')

@app.route('/login', methods =['post'])
def login():
    data={'email':request.form['email']}
    user_in_db = User.get_by_email(data)

    if not user_in_db:
        flash ('invalid credentials')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash ('invalid credentials')
        return redirect('/')
    session['user_id'] = user_in_db.id
    session['first_name'] = user_in_db.first_name
    session['last_name'] = user_in_db.last_name
    return redirect('/dashboard')

@app.route('/edit/user/<int:id>')
def edit_user(id):
    data = {'id':id}

    print (id)
    return render_template('edit.html', users=User.get_one(data),products=Product.get_all_user(data))

@app.route('/edit_user', methods=['post'])
def handle_user_edit():
    User.update_user(request.form)
    print(request.form)
    session['first_name']=request.form['first_name']
    session['last_name']=request.form['last_name']
    return redirect('/index')


@app.route('/index')
def index():
    if not session.get('first_name'):
        return redirect('/')
    return render_template('index.html', name_on_template=session['first_name'], users=User.get_all(), products=Product.get_with_user_name())
    # push up to end of 67 if obects with username on the dashboard


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
    