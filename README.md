# sign_in_with_google_for_web

As some of you may know ["Google Sign-in with web"](https://developers.google.com/identity/sign-in/web/sign-in)  will be deprecated on March 31, 2023. I have done a new ["Sign in with Google for web"](https://developers.google.com/identity/gsi/web/guides/overview) on my application. It works very smoothly and is easy to implement.

### Prerequisites:
1) Follow the steps described in [Setup](https://developers.google.com/identity/gsi/web/guides/get-google-api-clientid) to configure your OAuth Consent Screen and to obtain a Client ID.
2) [Load the client library](https://developers.google.com/identity/gsi/web/guides/client-library).
3) Set your Google client id as a environment variable GOOGLE_CLIENT_ID

## Getting Started

### Installing Dependencies

#### Python 3.9.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- To validate an ID token in Python, use the [verify_oauth2_token](https://google-auth.readthedocs.io/en/latest/reference/google.oauth2.id_token.html#google.oauth2.id_token.verify_oauth2_token)

## Running the server

From within the directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=app.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Endpoint:

Get Client Details

    GET '/login'
    - Fetches all informations about client: id, name, email, family_name.
    - Request Arguments: None
    - Returns: An object owners with all the cleint detail.
    - "localhost:8000/login"
    - {
        "data": {
            "aud": "CLIENT_ID",
            "azp": "CLIENT_ID",
            "email": "CLIENT_ EMAIL",
            "email_verified": true,
            "exp": 1678661244,
            "family_name": "....",
            "given_name": "....",
            "iat": , 
            "iss": "https://accounts.google.com",
            "jti": " ",
            "name": "Purvi Rawal",
            "nbf": , 
            "picture": " ",
            "sub": " "
        }
    }

### Author
Purvi Rawal

### Acknoledgemnts
[**Sign In with Google for Web**](https://developers.google.com/identity/gsi/web/guides/overview)
