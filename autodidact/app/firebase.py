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
        return user
    except Exception as e:
        return e


def log_in(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return user
    except Exception as e:
        return e


def refresh_token(user):
    user = auth.refresh(user['refreshToken'])
    return user


def send_verification_link(user):
    user = refresh_token(user)
    auth.send_email_verification(user['idToken'])


def reset_password(email):
    auth.send_password_reset_email(email)


def get_user_info(user):
    user = refresh_token(user)
    info = auth.get_account_info(user['idToken'])
    return info


def is_email_verified(user):
    info = get_user_info(user)
    return info['users'][0]['emailVerified']

