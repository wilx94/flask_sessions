from flask import Flask, session, render_template, request, redirect, g
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session.pop('user', None)
        if request.form['password'] == 'password':
            session['user'] = request.form['user_name']
            return redirect(url_for('protected'))

    return render_template('index.html')


@app.route('/protected')
def protected():
    return render_template('protected.html')


@app.before_request
def before_request():
    g.


@app.route('/get_session')
def get_session():
    if 'user' in session:
        return session['user']

    return 'Not logged in!'


@app.route('/drop_session')
def drop_session():
    session.pop('user', None)
    return 'Dropped!'


if __name__ == '__main__':
    app.run(debug=True, port=9000)
