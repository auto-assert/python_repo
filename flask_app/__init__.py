# flask_app/__init__.py
from flask import Flask, request, jsonify
import json

def create_app():
    app = Flask(__name__)

    # In-memory storage for simplicity; replace with a database for production
    users = []

    @app.route('/user', methods=['POST'])
    def create_user():
        user_data = request.get_json()
        username = user_data.get('username')
        password = user_data.get('password')
        profile = user_data.get('profile')
        
        if not username or not password or not profile:
            return jsonify({'error': 'Invalid data'}), 400

        user = {
            'username': username,
            'password': password,
            'profile': profile
        }
        users.append(user)

        # Append user data to a JSON file
        with open('users.json', 'w') as f:
            json.dump(users, f, indent=4)

        return jsonify(user), 201

    @app.route('/users', methods=['GET'])
    def get_users():
        return jsonify(users), 200

    return app
