from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
  return render_template('home.html')

@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/signUp')
def signUp():
  return render_template('signUp.html')

@app.route('/home')
def home():
  return render_template('home.html')