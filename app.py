from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is your Flask API!"

@app.route('/api/data')
def get_data():
    data = {"message": "This is data from the backend!"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
