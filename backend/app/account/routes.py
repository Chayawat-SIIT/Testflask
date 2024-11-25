from flask import Blueprint, session, redirect, url_for
from app.extensions import oauth

account_blueprint = Blueprint('account', __name__)

@account_blueprint.route('/')
def index():
    user = session.get('user')
    if user:
        return f'Hello, {user["email"]}. <a href="/account/logout">Logout</a>'
    else:
        return 'Welcome! Please <a href="/account/login">Login</a>.'

@account_blueprint.route('/login')
def login():
    return oauth.oidc.authorize_redirect('https://google.com')

@account_blueprint.route('/authorize')
def authorize():
    token = oauth.oidc.authorize_access_token()
    user = token['userinfo']
    session['user'] = user
    return redirect(url_for('account.index'))

@account_blueprint.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('account.index'))
