from flask import Flask
from app.account.routes import account_blueprint
from app.data.routes import data_blueprint
from app.extensions import cors
from app.utils.config import load_env_variables

def create_app():
    # Load environment variables
    load_env_variables()

    # Create Flask app
    app = Flask(__name__)
    app.secret_key = 'your-secure-key'  # Replace with a secure value or use .env

    # Initialize extensions
    cors.init_app(app)

    # Register blueprints
    app.register_blueprint(account_blueprint, url_prefix='/account')
    app.register_blueprint(data_blueprint, url_prefix='/data')

    return app
