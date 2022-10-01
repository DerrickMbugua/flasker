from flask import Flask

#create an instance
app = Flask(__name__)

#create a route
@app.route('/')

def index():
  return "<p>Hello World</p>"