from flask_cors import CORS
from authlib.integrations.flask_client import OAuth
import os

cors = CORS()
oauth = OAuth()

oauth.register(
    name='oidc',
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    server_metadata_url='https://cognito-idp.us-east-1.amazonaws.com/us-east-1_LfeJWW1e9/.well-known/openid-configuration',
    client_kwargs={'scope': 'email openid phone'}
)
