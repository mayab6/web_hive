from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/signup')
def signup():
    return render_template('sign_up.html')


@app.route('/')
def index():
    name = request.args.get('name')
    return render_template('home.html', name=name, url=signup())


if __name__ == '__main__':
    app.run()
