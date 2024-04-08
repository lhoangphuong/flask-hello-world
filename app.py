from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


def index():
  pagetitle = "HomePage"
  return render_template("index.html",
    mytitle="HomePage", 
    mycontent="Hello World"
  )