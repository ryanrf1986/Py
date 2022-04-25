from flask import render_template, redirect, request, session,flash
from flask_app import app, bcrypt
from flask_app.models.user import User
from flask_app.models.painting import Painting

@app.route('/new')
def recipes_new():
    if not session.get('first_name'):
        return redirect ('/')
    return render_template('new.html')

@app.route('/create_painting', methods=['post'])
def create_painting():
    if not Painting.validate_painting(request.form):
        return redirect('/new')
    paintings=Painting.save(request.form)
    print(paintings)
    return redirect('/dashboard')
    
@app.route('/show/<int:id>')
def show(id):
    data = {'id':id}
    print(id)
    return render_template('show.html', paintings=Painting.get_one_with_user(data))

@app.route('/delete/<int:id>')
def delete_painting(id):
    data = {'id' : id}
    Painting.delete_painting(data)
    return redirect('/dashboard')
    
@app.route('/edit/<int:id>')
def edit(id):
    data = {'id' : id}
    print(request.form)
    return render_template('edit.html', painting=Painting.get_one_with_user(data))

@app.route('/edit_painting', methods=['POST'])
def handle_edit():
    print(request.form)
    Painting.edit_painting(request.form)
    return redirect('/dashboard')
