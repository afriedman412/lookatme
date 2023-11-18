from flask import Flask, g
from .routes import home, page
import yaml
import os

app = Flask(__name__)


@app.before_request
def load_data():
    for file in ['tag_templates', 'settings', 'entries', 'content']:
        with open(
            os.path.join(
                app.static_folder, f'{file}.yml'), 'r'
                ) as yaml_file:
            setattr(g, file, yaml.safe_load(yaml_file))


app.route("/")(home)
app.route("/<tag>")(page)
