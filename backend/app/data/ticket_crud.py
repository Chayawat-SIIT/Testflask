from flask import Blueprint, request, jsonify
from app.data.db import get_db_connection
from datetime import datetime


ticket_blueprint = Blueprint('ticket', __name__)

# Add Ticket
@ticket_blueprint.route('/ticket', methods=['POST'])
def add_ticket():
    try:
        data = request.get_json()  # Expecting JSON data
        tkzone = data['tkzone']
        tktype = data['tktype']
        cid = data['cid']
        uid = data['uid']

        connection = get_db_connection()
        cursor = connection.cursor()
        
        # Validate if user already purchased the same ticket for the concert
        cursor.execute("SELECT COUNT(*) FROM tickets WHERE uid = %s AND cid = %s AND tktype = %s", (uid, cid, tktype))
        if cursor.fetchone()[0] > 0:
            return jsonify({"error": "User already purchased this ticket type for the concert."}), 400
        
        # Insert new ticket
        cursor.execute(
            "INSERT INTO tickets (tkzone, tktype, cid, uid) VALUES (%s, %s, %s, %s)", 
            (tkzone, tktype, cid, uid)
        )
        connection.commit()
        return jsonify({"message": "Ticket purchased successfully!"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if connection:
            cursor.close()
            connection.close()

# Fetch Tickets by User
@ticket_blueprint.route('/tickets/<int:uid>', methods=['GET'])
def fetch_tickets(uid):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        # Retrieve tickets for the user along with concert details
        cursor.execute("""
            SELECT tickets.tkid, tickets.tkzone, tickets.tktype, tickets.tkstatus, concert.concert_name, concert.date
            FROM tickets
            JOIN concert ON tickets.cid = concert.cid
            WHERE tickets.uid = %s
        """, (uid,))
        tickets = cursor.fetchall()

        if tickets:
            return jsonify(tickets), 200
        return jsonify({"message": "No tickets found for this user."}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if connection:
            cursor.close()
            connection.close()

# Update Ticket Status
@ticket_blueprint.route('/ticket/<int:tkid>', methods=['PUT'])
def update_ticket_status(tkid):
    try:
        data = request.get_json()
        new_status = data['tkstatus']
        
        connection = get_db_connection()
        cursor = connection.cursor()

        # Update the ticket status
        cursor.execute("UPDATE tickets SET tkstatus = %s WHERE tkid = %s", (new_status, tkid))
        connection.commit()

        return jsonify({"message": "Ticket status updated successfully!"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if connection:
            cursor.close()
            connection.close()

# Delete Ticket
@ticket_blueprint.route('/ticket/<int:tkid>', methods=['DELETE'])
def delete_ticket(tkid):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        # Delete the ticket based on the provided ticket ID
        cursor.execute("DELETE FROM tickets WHERE tkid = %s", (tkid,))
        connection.commit()

        # Check if the ticket was deleted
        if cursor.rowcount > 0:
            return jsonify({"message": "Ticket deleted successfully!"}), 200
        else:
            return jsonify({"error": "Ticket not found."}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if connection:
            cursor.close()
            connection.close()

