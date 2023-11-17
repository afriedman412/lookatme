from flask import Flask
from .routes import home, page

app = Flask(__name__)

app.route("/")(home)
app.route("/<tag>")(page)
