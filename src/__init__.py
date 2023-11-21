import os

import yaml
from flask import Flask, g

from .config import Config
from .routes import home, page

app = Flask(__name__)
app.config.from_object(Config)


def load_data() -> None:
    file_names = app.config.get("YAML_FILES", [])
    for file in file_names:
        # 'str' because there is a typing issue
        yaml_path = os.path.join(str(app.static_folder), f"{file}.yml")
        try:
            with open(yaml_path, "r") as yaml_file:
                setattr(g, file, yaml.safe_load(yaml_file))
        except FileNotFoundError:
            app.logger.warning(f"YAML file not found: {yaml_path}")
        except yaml.YAMLError as e:
            app.logger.error(f"Error loading YAML file {yaml_path}: {e}")


app.before_request(load_data)
app.route("/")(home)
app.route("/<tag>")(page)
