from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")
@app.route('/PC')
def PC():
    return render_template("PC.html")
@app.route('/phone')
def phone():
    return render_template("phone.html")

if __name__ == '__main__':
    app.run()
