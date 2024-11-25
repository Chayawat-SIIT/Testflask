import os
from flask_cors import CORS
from authlib.integrations.flask_client import OAuth

cors = CORS()
oauth = OAuth()

def init_extensions(app):
    """
    Initialize Flask extensions with the app instance.
    """
    cors.init_app(app)  # Initialize CORS with app
    oauth.init_app(app)  # Initialize OAuth with app

    # Register the OAuth provider (Cognito)
    oauth.register(
        name='oidc',
        client_id=os.environ.get('CLIENT_ID'),
        client_secret=os.environ.get('CLIENT_SECRET'),
        api_base_url='https://us-east-1lfejww1e9.auth.us-east-1.amazoncognito.com',
        authorize_url='https://us-east-1lfejww1e9.auth.us-east-1.amazoncognito.com/login',
        access_token_url='https://us-east-1lfejww1e9.auth.us-east-1.amazoncognito.com/oauth2/token',
        client_kwargs={
            'scope': 'email openid profile',
            'response_type': 'code',
        },
    )