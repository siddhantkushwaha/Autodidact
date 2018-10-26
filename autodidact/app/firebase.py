import json
import requests
import pyrebase

config = {
    "apiKey": "AIzaSyC6ncYDClT8Pb9n9At03KZh7XOUeRKZA3A",
    "authDomain": "autodidact-forum.firebaseapp.com",
    "databaseURL": "https://autodidact-forum.firebaseio.com",
    "projectId": "autodidact-forum",
    "storageBucket": "autodidact-forum.appspot.com",
    "messagingSenderId": "235896897611"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


def sign_up(email, password):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        send_verification_link(user)
        return user
    except requests.exceptions.HTTPError as err:
        return json.loads(err.strerror)['error']['message']
    except requests.exceptions.ConnectionError as err:
        return err
    except requests.exceptions.RequestException as err:
        return err


def log_in(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return user
    except requests.exceptions.HTTPError as err:
        return json.loads(err.strerror)['error']['message']
    except requests.exceptions.ConnectionError as err:
        return err
    except requests.exceptions.RequestException as err:
        return err


def refresh_token(user):
    try:
        user = auth.refresh(user['refreshToken'])
        return user
    except requests.exceptions.HTTPError as err:
        return json.loads(err.strerror)['error']['message']
    except requests.exceptions.ConnectionError as err:
        return err
    except requests.exceptions.RequestException as err:
        return err


def send_verification_link(user):
    try:
        user = refresh_token(user)
        auth.send_email_verification(user['idToken'])
    except requests.exceptions.HTTPError as err:
        return json.loads(err.strerror)['error']['message']
    except requests.exceptions.ConnectionError as err:
        return err
    except requests.exceptions.RequestException as err:
        return err


def reset_password(email):
    try:
        auth.send_password_reset_email(email)
    except requests.exceptions.HTTPError as err:
        return json.loads(err.strerror)['error']['message']
    except requests.exceptions.ConnectionError as err:
        return err
    except requests.exceptions.RequestException as err:
        return err


def get_user_info(user):
    try:
        user = refresh_token(user)
        info = auth.get_account_info(user['idToken'])
        return info
    except requests.exceptions.HTTPError as err:
        return json.loads(err.strerror)['error']['message']
    except requests.exceptions.ConnectionError as err:
        return err
    except requests.exceptions.RequestException as err:
        return err


def is_email_verified(user):
    try:
        info = get_user_info(user)
        return info['users'][0]['emailVerified']
    except requests.exceptions.HTTPError as err:
        return json.loads(err.strerror)['error']['message']
    except requests.exceptions.ConnectionError as err:
        return err
    except requests.exceptions.RequestException as err:
        return err