from flask import Flask
from markupsafe import escape

#create an instance
app = Flask(__name__)

#create a route
@app.route('/')

def index():
  return "<p>Hello World</p>"

@app.route('/<name>')

def user(name):
  return f"<p>Hello, {escape(name)}!</p>"