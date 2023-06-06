from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    name = request.args.get('name')
    return render_template('hello_name.html', name=name)


if __name__ == '__main__':
    app.run()
