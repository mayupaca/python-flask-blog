from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return '<h1>Hello test page!</h1>'

@app.route('/user/<user_id>')
def userId(user_id):
    return '<h1>Your User ID: {0} {1} {2}</h1>'.format(user_id[0],user_id[1],user_id[2])  # .format(user_id): ()の中の値が{}の中に入る

if __name__ == '__main__':
    app.run(debug=True) # debug=Trueにするとデバッグモードになって、エラーを表示してくれる