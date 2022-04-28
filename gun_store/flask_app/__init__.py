# __init__.py
from flask import Flask, session, flash
from flask_bcrypt import Bcrypt
import re


app = Flask(__name__)



app.secret_key = "nonononononono"

bcrypt = Bcrypt(app)