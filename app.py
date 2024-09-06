from flask import Flask, jsonify
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for the app, allowing requests from the frontend URL
CORS(app, origins=["https://dashboardfrontend-4ak3.onrender.com"])

# Example route for testing the API
@app.route('/api/data', methods=['GET'])
def get_data():
    # Return sample data as JSON
    data = {
        'message': 'Hello from the backend!',
        'status': 'success',
        'data': [1, 2, 3, 4, 5]
    }
    return jsonify(data)

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
