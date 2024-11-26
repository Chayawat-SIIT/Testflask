from flask import Blueprint, request, jsonify
from app.data.db import get_db_connection

concert_blueprint = Blueprint('concerts', __name__)

# Get Concerts (Fetch all concert details sorted by cdate_time)
@concert_blueprint.route('/concerts', methods=['GET'])
def get_concerts():
    connection = None
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT cid, cname, cdate_time FROM concert ORDER BY cdate_time")
        rows = cursor.fetchall()
        return jsonify(rows)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if connection:
            cursor.close()
            connection.close()


# Create Concert (Add a new concert)
@concert_blueprint.route('/concerts', methods=['POST'])
def create_concert():
    connection = None
    try:
        data = request.get_json()

        cname = data.get('cname')
        cdate_time = data.get('cdate_time')

        if not cname or not cdate_time:
            return jsonify({"error": "Concert name and date-time are required"}), 400

        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO concert (cname, cdate_time) VALUES (%s, %s) RETURNING cid",
            (cname, cdate_time)
        )
        concert_id = cursor.fetchone()[0]  # Get the generated concert ID
        connection.commit()

        return jsonify({"cid": concert_id, "cname": cname, "cdate_time": cdate_time}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if connection:
            cursor.close()
            connection.close()


# Update Concert (Modify existing concert details using the concert ID)
@concert_blueprint.route('/concerts/<int:cid>', methods=['PUT'])
def update_concert(cid):
    connection = None
    try:
        data = request.get_json()

        cname = data.get('cname')
        cdate_time = data.get('cdate_time')

        if not cname and not cdate_time:
            return jsonify({"error": "At least one field (name or date-time) must be provided"}), 400

        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM concert WHERE cid = %s", (cid,))
        concert = cursor.fetchone()
        if not concert:
            return jsonify({"error": "Concert table not found"}), 404

        # Update the concert
        if cname:
            cursor.execute("UPDATE concert SET cname = %s WHERE cid = %s", (cname, cid))
        if cdate_time:
            cursor.execute("UPDATE concert SET cdate_time = %s WHERE cid = %s", (cdate_time, cid))

        connection.commit()

        return jsonify({"cid": cid, "cname": cname if cname else concert[1], "cdate_time": cdate_time if cdate_time else concert[2]}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if connection:
            cursor.close()
            connection.close()


# Delete Concert (Remove a concert from the database by its ID)
@concert_blueprint.route('/concerts/<int:cid>', methods=['DELETE'])
def delete_concert(cid):
    connection = None
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM concert WHERE cid = %s", (cid,))
        concert = cursor.fetchone()
        if not concert:
            return jsonify({"error": "Concert not found"}), 404

        # Delete the concert
        cursor.execute("DELETE FROM concert WHERE cid = %s", (cid,))
        connection.commit()

        return jsonify({"message": f"Concert with ID {cid} deleted successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if connection:
            cursor.close()
            connection.close()
