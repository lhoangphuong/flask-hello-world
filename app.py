from flask import Flask, render_template, request, jsonify
import requests
import json


app = Flask(__name__)

@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"


@app.route('/cognito_auth', methods=['GET'])
def form():
    return render_template('cognito_auth.html')


@app.route('/cognito_auth', methods=['POST'])
def cognito_auth():
    url = 'https://cognito-idp.us-east-1.amazonaws.com/'
    headers = {
        'Content-Type': 'application/x-amz-json-1.1',
        'X-Amz-Target': 'AWSCognitoIdentityProviderService.InitiateAuth'
    }
    data = {
        "AuthFlow": "USER_PASSWORD_AUTH",
        "AuthParameters": {
            "USERNAME": request.form.get('username'),
            "PASSWORD": request.form.get('password')
        },
        "ClientId": request.form.get('client_id')
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return jsonify(response.json())