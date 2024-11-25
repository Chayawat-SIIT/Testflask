import os
from flask import Flask
from app.extensions import init_extensions
from app.account.routes import account_blueprint
from app.data.routes import data_blueprint
from app.utils.config import load_env_variables

def create_app():
    # Load environment variables
    load_env_variables()

    # Create Flask app
    app = Flask(__name__)
    app.secret_key = os.environ.get('SECRET_KEY')

    # Initialize extensions
    init_extensions(app)

    # Register blueprints
    app.register_blueprint(account_blueprint, url_prefix='/account')
    app.register_blueprint(data_blueprint, url_prefix='/data')

    return app
