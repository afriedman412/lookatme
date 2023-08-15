from flask import Flask

app = Flask(__name__)

from .routes import home, page, about

app.route("/")(home)
app.route('/about')(about)
app.route("/<tag>")(page)