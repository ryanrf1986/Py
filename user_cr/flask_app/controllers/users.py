from flask import Flask, render_template, redirect, request
# import the class from user.py
from flask_app.models.user import User
from flask_app import app
@app.route("/")
def index():
    # call the get all classmethod to get all users
    users = User.get_all()
    print(users)
    return render_template("index.html", users=users)

@app.route("/create")
def create():
    # call the get all classmethod to get all users
    return render_template("create.html")

@app.route("/create_friend",methods=["POST"])
def handle():
    print(request.form)
    User.save(request.form)
    # call the get all classmethod to get all users
    return redirect("/")
            
@app.route("/destroy/<int:id>")
def destroy(id):
    data= {'id':id}
    User.destroy(data)
    return redirect('/')
