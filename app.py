from google.oauth2 import id_token
from google.auth.transport import requests

import os

# Third-party libraries
from flask import (
    Flask,
    render_template,
    request,
    Response,
    redirect,
    url_for,
    session,
    jsonify
)

app = Flask(__name__)
GOOGLE_CLIENT_ID = os.environ['GOOGLE_CLIENT_ID']

'''
Login page get Google Signin Button.
'''
@app.route('/')
def index():
    # render login page
    return render_template("index.html", GOOGLE_CLIENT_ID=GOOGLE_CLIENT_ID)

'''
After user login set all values into session.
'''
@app.route('/login', methods=['POST', 'GET'])
def login():
    # Get google credential and decode using jose
    token = request.form.get("credential")

    try:
        # Specify the CLIENT_ID of the app that accesses the backend:
        user_info = id_token.verify_oauth2_token(token, requests.Request(), GOOGLE_CLIENT_ID)
        
        # ID token is valid. Get the user's Google Account ID from the decoded token.
        user_id = user_info["sub"]
        user_full_name = user_info["name"]
        user_given_name = user_info["given_name"]
        user_family_name = user_info["family_name"]
        user_picture = user_info["picture"]
        user_email = user_info["email"]

        return jsonify({"data":user_info})
    except ValueError:  
        # Invalid token
        pass

if __name__ == "__main__":
    app.run(port=8000, debug=True)