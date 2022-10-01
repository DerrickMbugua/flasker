from flask import Flask, render_template
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

@app.get('/home')
def home():
  return render_template('index.html')