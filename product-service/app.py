from flask import Flask, jsonify

app = Flask(__name__)

products_data = [
    {"id": 101, "name": "Laptop gaming", "price": 12000000},
    {"id": 102, "name": "Keyboard", "price": 350000},
    {"id": 103, "name": "Mouse", "price": 150000}
]

@app.route('/products')
def get_products():
    return jsonify({
        "service": "product-service",
        "data": products_data
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
