from flask import Blueprint, request, jsonify
from app.data.db import get_db_connection

payment_blueprint = Blueprint('payment', __name__)

# 1. Add Payment
@payment_blueprint.route('/payment', methods=['POST'])
def add_payment():
    try:
        data = request.get_json()
        tid = data['tid']
        uid = data['uid']
        tdate_time = data['tdate_time']
        tstatus = data['tstatus']

        connection = get_db_connection()
        cursor = connection.cursor()

        # Insert payment details into the payments table
        cursor.execute(
            "INSERT INTO payments (tid, uid, tdate_time, tstatus) VALUES (%s, %s, %s, %s)", 
            (tid, uid, tdate_time, tstatus)
        )
        connection.commit()
        return jsonify({"message": "Payment processed successfully!"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if connection:
            cursor.close()
            connection.close()

# 2. Fetch Payments by User
@payment_blueprint.route('/payments/<int:uid>', methods=['GET'])
def fetch_payments(uid):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        # Fetch payments and concert details for a specific user
        cursor.execute("""
            SELECT payments.tid, payments.tdate_time, payments.tstatus, 
                   tickets.tktype, concert.concert_name
            FROM payments
            JOIN tickets ON payments.tid = tickets.tkid
            JOIN concert ON tickets.cid = concert.cid
            WHERE payments.uid = %s
        """, (uid,))
        payments = cursor.fetchall()

        if payments:
            return jsonify(payments), 200
        return jsonify({"message": "No payments found for this user."}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if connection:
            cursor.close()
            connection.close()

# 3. Update Payment Status
@payment_blueprint.route('/payment/<int:tid>', methods=['PUT'])
def update_payment_status(tid):
    try:
        data = request.get_json()
        new_status = data['tstatus']
        
        connection = get_db_connection()
        cursor = connection.cursor()

        # Update the payment status
        cursor.execute("UPDATE payments SET tstatus = %s WHERE tid = %s", (new_status, tid))
        connection.commit()

        return jsonify({"message": "Payment status updated successfully!"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if connection:
            cursor.close()
            connection.close()

# 4. Delete Payment
@payment_blueprint.route('/payment/<int:tid>', methods=['DELETE'])
def delete_payment(tid):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        # Delete the payment based on the provided payment ID
        cursor.execute("DELETE FROM payments WHERE tid = %s", (tid,))
        connection.commit()

        # Check if the payment was deleted
        if cursor.rowcount > 0:
            return jsonify({"message": "Payment deleted successfully!"}), 200
        else:
            return jsonify({"error": "Payment not found."}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if connection:
            cursor.close()
            connection.close()

