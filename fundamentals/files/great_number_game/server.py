from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'keep it secret, keep it safe' 

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/survey', methods=['POST'])
def create_user():
    print(request.form)
    session ['name'] = request.form['name']
    session ['location'] = request.form['location']
    session ['languages'] = request.form['languages']
    session ['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template("show.html")


# NINJA BONUS: Use a CSS framework to style your form

# NINJA BONUS: Include a set of radio buttons on your form

# SENSEI BONUS: Include a set of checkboxes on your form