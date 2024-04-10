from flask import Flask, render_template

app = Flask(__name__)
# view関数
@app.route('/')
def index():
    user_name = "John"
    return render_template('index.html', user_name=user_name)

@app.route('/product')
def product():
    product_list = ["computer1", "computer2", "computer3"]
    product_dict = {"product_name":"computer1","product_price":"4300","product_maker":"maker1"}
    return render_template('product.html', products=product_list, product_dict=product_dict)

@app.route('/test')
def test():
    return '<h1>Hello test page!</h1>'

@app.route('/user/<user_id>')
def userId(user_id):
    return '<h1>Your User ID: {0} {1} {2}</h1>'.format(user_id[0],user_id[1],user_id[2])  # .format(user_id): ()の中の値が{}の中に入る


@app.route('/user')
def user():
    user_list = [
        ["1","John Lennon","john@test.com","1"],
        ["2","Paul McCartney","paul@test.com","0"],
        ["3","Ringo Starr","ringo@test.com","0"]
    ]

    return render_template('user.html', users=user_list)

@app.errorhandler(404)
def error_404(error):
    return render_template('error_pages/404.html'), 404

if __name__ == '__main__':
    app.run(debug=True) # debug=Trueにするとデバッグモードになって、エラーを表示してくれる