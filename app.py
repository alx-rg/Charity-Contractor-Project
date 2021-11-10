
# env/bin/activate
# If you ever want to deactivate your virtual environment, just type deactivate in your terminal window.#
# export FLASK_ENV=development; flask run
# http://127.0.0.1:5000/

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    # change the original return statement you wrote to the one below
    return render_template('home.html', msg='Flask is Cool!!')
