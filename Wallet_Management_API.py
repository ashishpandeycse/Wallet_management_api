from flask import Flask, request, jsonify # type: ignore
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity # type: ignore

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this in production
jwt = JWTManager(app)

# Dummy data
users = []
expenses = []
categories = []

# User Authentication
@app.route('/hello')
def hello():
    # print("ok")
    return "ok"

@app.route('/api/auth/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    # Add user to the database (dummy implementation)
    users.append({'username': username, 'email': email, 'password': password})
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    # Dummy authentication, replace with proper authentication logic
    for user in users:
        if user['username'] == username and user['password'] == password:
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token), 200
    return jsonify({"message": "Invalid username or password"}), 401

# Expense Categories Management
@app.route('/api/categories', methods=['GET'])
@jwt_required()
def get_categories():
    # Fetch categories for the authenticated user (dummy implementation)
    return jsonify(categories), 200

@app.route('/api/categories', methods=['POST'])
@jwt_required()
def add_category():
    data = request.get_json()
    category_name = data.get('name')
    # Add category to the database (dummy implementation)
    categories.append({'name': category_name})
    return jsonify({'message': 'Category added successfully'}), 201

@app.route('/api/categories/<int:category_id>', methods=['DELETE'])
@jwt_required()
def delete_category(category_id):
    # Delete category from the database (dummy implementation)
    return jsonify({'message': 'Category deleted successfully'}), 200

# Expense Management
@app.route('/api/expenses', methods=['POST'])
@jwt_required()
def add_expense():
    data = request.get_json()
    # Add expense to the database (dummy implementation)
    expenses.append(data)
    return jsonify({'message': 'Expense added successfully'}), 201

@app.route('/api/expenses', methods=['GET'])
@jwt_required()
def get_expenses():
    # Fetch expenses for the authenticated user (dummy implementation)
    return jsonify(expenses), 200

# More routes for expense management can be added here...

if __name__ == '__main__':
    app.run(debug=False, port=8888)
