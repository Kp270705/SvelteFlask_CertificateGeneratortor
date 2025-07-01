from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # enable CORS for all routes

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello from Flask backend!"})

@app.route('/api/testApi', methods=['GET'])
def test():
    return jsonify({"test_message": "This is a test endpoint!"})

@app.route('/api/testApi2', methods=['GET'])
def test2():
    return jsonify({"test_message2": "This is a test2 endpoint!"})

@app.route('/api/send', methods=['POST'])
def receive_data():
    data = request.json
    print("Received from frontend:", data)
    return jsonify({"status": "received", "data": data})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
