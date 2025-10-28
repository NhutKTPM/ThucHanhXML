from flask import Flask, jsonify, request
import json

app = Flask(__name__)
    

# Load data from JSON files
# Load bai_9_1.json for books data
with open('Buoi_9/bai_9_1.json', 'r', encoding='utf-8') as f:
    books_data = json.load(f)

with open('Buoi_9/bai_9_2.json', 'r', encoding='utf-8') as f:
    users_data = json.load(f)

@app.route('/')
def home():
    return "Welcome to the Flask JSON Validator API!"

@app.route('/api/book', methods=['GET'])
def get_books():
    return jsonify(books_data)

@app.route('/api/user/<username>', methods=['GET'])
def get_user(username):
    user = next((user for user in users_data['users'] if user['username'] == username), None)
    if user:
        return jsonify(user)
    return jsonify({'error': 'User not found'}), 404

@app.route('/api/subtract', methods=['POST'])
def subtract_numbers():
    data = request.get_json()
    if 'num1' in data and 'num2' in data:
        result = data['num1'] - data['num2']
        return jsonify({'result': result})
    return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(debug=True)