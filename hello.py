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
  return render_template('user.html', name=name)

@app.get('/home')
def home():
  return render_template('index.html')