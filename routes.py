from flask import Blueprint, jsonify, request
from database import check_user

api_blueprint = Blueprint('api', __name__)

# Inloggen van een gebruiker
@api_blueprint.route('/api/login', methods=['POST'])
def login():
    try:
        username = request.json.get('username')
        password = request.json.get('password')
        
        # Controleer of de gebruiker bestaat en het wachtwoord klopt
        if check_user(username, password):
            return jsonify({'message': 'Inloggen succesvol'}), 200
        else:
            return jsonify({'error': 'Ongeldige inloggegevens'}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 500
