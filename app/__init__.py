from flask import Flask, g
from .routes import home, page
import yaml
import os

app = Flask(__name__)

@app.before_request
def load_data():
    data_path = os.path.join(app.static_folder, 'tag_templates.yml')
    with open(data_path, 'r') as yaml_file:
        g.tag_templates = yaml.safe_load(yaml_file)

app.route("/")(home)
app.route("/<tag>")(page)
