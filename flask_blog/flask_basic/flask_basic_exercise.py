from flask import Flask

app = Flask(__name__)

@app.route('/')
def index(): # view関数
    return '<h1>Product Page</h1>'

@app.route('/product/<product_id>')
def productId(product_id):
    product_list = [
        ["1", "Laptop A", "Core i5", "￥68,500"],
        ["2", "Laptop B", "AMD Ryzen 5", "￥81,300"],
        ["3", "Laptop C", "CeleronN4020", "￥64,300"]
    ]
    for product in product_list:
        if product_id in product:
            break
    product_name = product[1]
    product_cpu = product[2]
    product_price = product[3]

    return '<p>Product Name: {0} </br> CPU: {1} </br> Price: {2}</p>'.format(product_name, product_cpu, product_price)

if __name__ == '__main__':
    app.run(debug=True)
