from flask import Flask, jsonify
import requests

app = Flask(__name__)

users_data = [
    {"id": 1, "name": "Asti", "role": "admin"},
    {"id": 2, "name": "Abi", "role": "customer"},
    {"id": 3, "name": "Nayla", "role": "customer"}
]

@app.route('/users')
def get_users():
    return jsonify({
        "service": "user-service",
        "data": users_data
    })

@app.route('/users-with-products')
def users_with_products():
    response = requests.get('http://product-service:5000/products')
    products = response.json()

    return jsonify({
        "service": "user-service",
        "users": users_data,
        "products": products["data"]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
