from flask import Blueprint, jsonify
from app.data.db import get_db_connection

data_blueprint = Blueprint('data', __name__)

@data_blueprint.route('/', methods=['GET'])
def get_data():
    connection = None
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM concert")  # Replace with your table
        rows = cursor.fetchall()
        return jsonify(rows)

    except Exception as e:
        return jsonify({"error": str(e)})

    finally:
        if connection:
            cursor.close()
            connection.close()
