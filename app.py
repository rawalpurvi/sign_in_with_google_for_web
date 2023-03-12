# Google library for verify the token
from google.oauth2 import id_token
from google.auth.transport import requests

import os

# Third-party libraries
from flask import (
    Flask,
    render_template,
    request,
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
After user login set all values to display.
'''
@app.route('/login', methods=['POST', 'GET'])
def login():
    # Get google credential
    token = request.form.get("credential")

    # Verify Google Response Token
    try:
        # Specify the CLIENT_ID of the app that accesses the backend:
        user_info = id_token.verify_oauth2_token(token, requests.Request(), GOOGLE_CLIENT_ID)
        return jsonify({"data":user_info})
    except ValueError:  
        # Invalid token
        pass

if __name__ == "__main__":
    app.run(port=8000, debug=True)