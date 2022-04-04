from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Hello, World')


@app.route('/ouser/<username>') #страница вне шаблона
def oprofile(username):
    return f'<h1>User: {username}</h1>'


@app.route('/user/<username>') #страница внутри шаблона
def profile(username):
    return render_template('user.html', title='Profile', username=username)


if __name__ == "__main__":
    app.run(debug=True)
