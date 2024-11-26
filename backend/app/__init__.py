import os
from flask import Flask
from app.extensions import init_extensions
from app.account.routes import account_blueprint
from app.data.routes import data_blueprint
from app.concert.routes import concert_blueprint
from app.payment.routes import payment_blueprint
from app.ticket.routes import ticket_blueprint
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
    app.register_blueprint(concert_blueprint, url_prefix='/concerts')
    app.register_blueprint(payment_blueprint, url_prefix='/payment')
    app.register_blueprint(ticket_blueprint, url_prefix='/ticket')

    return app
