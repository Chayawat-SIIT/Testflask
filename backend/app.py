from flask import Flask, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
from flask_cors import CORS

app = Flask(__name__)
CORS = CORS(app)

# Database connection details
DB_HOST = 'database-1.cp25uacsjlql.us-east-1.rds.amazonaws.com'  # Replace with your RDS endpoint
DB_PORT = '5432'              # PostgreSQL default port
DB_USER = 'postgres'     # Replace with your username
DB_PASSWORD = 'g10-database' # Replace with your password
DB_NAME = 'postgres'     # Replace with your database name

@app.route('/data', methods=['GET'])
def get_data():
    connection = None
    try:
        # Establish connection to PostgreSQL
        connection = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            dbname=DB_NAME
        )
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        
        # Execute query
        cursor.execute("select * from concert")  # Replace `your_table` with your table name
        rows = cursor.fetchall()

        # Return data as JSON
        return jsonify(rows)

    except Exception as e:
        return jsonify({"error": str(e)})

    finally:
        if connection:
            cursor.close()
            connection.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
