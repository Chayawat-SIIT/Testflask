import os
from dotenv import load_dotenv

def load_env_variables():
    load_dotenv()  # Automatically loads from .env file
    os.environ.setdefault('DB_HOST', 'localhost')
    os.environ.setdefault('DB_PORT', '5432')
    os.environ.setdefault('DB_USER', 'user')
    os.environ.setdefault('DB_PASSWORD', 'password')
    os.environ.setdefault('DB_NAME', 'database')