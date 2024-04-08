from flask import Flask, render_template
app = Flask(__name__)


def index():
  return render_template("index.html",
    mytitle="HomePage", 
    mycontent="Hello World"
  )