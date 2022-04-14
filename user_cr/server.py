from flask_app import app
# import the class from user.py
from flask_app.controllers import users

@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template("read.html", all_users = users)

@app.route('/add')
def add():
    return render_template("create.html")

@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname" : request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the User class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')











if __name__ == "__main__":
    app.run(debug=True)