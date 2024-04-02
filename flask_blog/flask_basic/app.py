from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/test')
def test():
    return '<h1>Hello test page!</h1>'

@app.route('/user/<user_id>')
def userId(user_id):
    return '<h1>Your User ID: {0}</h1>'.format(user_id)  # .format(user_id): ()の中の値が{}の中に入る

if __name__ == '__main__':
    app.run()