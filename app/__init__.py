from flask import Flask

app = Flask(__name__)

from .routes import home, page

app.route("/")(home)
app.route("/<tag>")(page)