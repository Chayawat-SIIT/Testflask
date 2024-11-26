from flask import Blueprint, request, jsonify
from app.data.db import get_db_connection

user_blueprint = Blueprint('user', __name__)

# User Registration (Create a new user)
@user_blueprint.route('/register', methods=['POST'])
def register_user():
    connection = None
    try:
        # Get data from the incoming JSON request
        data = request.get_json()

        full_name = data.get('full_name')
        username = data.get('username')
        email = data.get('email')
        phone_num = data.get('phone_num')

        # Validate required fields
        if not full_name or not username or not email or not phone_num:
            return jsonify({"error": "All fields (full_name, username, email, phone_num) are required"}), 400

        connection = get_db_connection()
        cursor = connection.cursor()

        # Check if the username or email already exists
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        existing_user = cursor.fetchone()
        if existing_user:
            return jsonify({"error": "Username already exists"}), 400

        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        existing_email = cursor.fetchone()
        if existing_email:
            return jsonify({"error": "Email already exists"}), 400

        # Insert the new user into the database
        cursor.execute(
            "INSERT INTO users (full_name, username, email, phone_num) VALUES (%s, %s, %s, %s) RETURNING uid",
            (full_name, username, email, phone_num)
        )
        user_id = cursor.fetchone()[0]  # Get the newly generated user ID
        connection.commit()

        # Return success response
        return jsonify({"message": "User registered successfully", "uid": user_id}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if connection:
            cursor.close()
            connection.close()
