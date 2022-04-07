from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
    # Run the app in debug mode.

# import statements, maybe some other routes
    
@app.route('/success')
def success():
    return "success"
    
# app.run(debug=True) should be the very last statement! 

@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    # return "Hello, " + name
    return f"Hello {name}"

@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    # return "username: " + username + ", id: " + id
    return f"username {username} id {id}"

@app.route('/dojo')
def dojo():
    print("dojo")
    return "Dojo!"


@app.route('/say/<s>')
def say(s):
    return str(s)



@app.route('/repeat/<int:n>/<var>') # for a route
def repeat(n, var):
    # print(n)
    # print(var)
    # print(var * int((n))
    # return str((var + '') * int((n))
    return f"{var} " * n











if __name__=="__main__":   # Ensure this file is being run directly and not from a different module must be at end!!!!    
    app.run(debug=True)