from flask import Flask, render_template, url_for, redirect, session, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(message='Please enter email address.')])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message='This password is not matched.')])
    pass_confirm = PasswordField('Password(Confirm)',validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    # .validate_on_submit() - フォームの送信＆入力内容の確認
    if form.validate_on_submit():
        # 問題がなければsessionに情報を保持
        # session = ウェブサイトにアクセスしてsessionが始まる。最初のページから次のページへの通信が続く間一時的に情報を保持する領域
        session['email'] = form.email.data
        session['username'] = form.username.data
        session['password'] = form.password.data
        flash('Success registration!!')
        return redirect(url_for('user_maintenance'))
    return render_template('register.html', form=form)

@app.route('/user_maintenance')
def user_maintenance():
    return render_template('user_maintenance.html')

if __name__ == '__main__':
    app.run(debug=True)