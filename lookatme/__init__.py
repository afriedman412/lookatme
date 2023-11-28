import logging
import os

import yaml
from flask import Flask, g, request

from .config import Config, TestingConfig
from .helpers import add_log
from .routes import home, page

app = Flask(__name__)


def log_request_info() -> None:
    app.logger.debug("Request: %s %s", request.method, request.path)


if os.environ.get("FLASK_ENV") == "test":
    app.logger.setLevel(logging.DEBUG)
    app.logger.addHandler(add_log())
    app.logger.debug("loading TEST env in init!!")
    app.config.from_object(TestingConfig)
    app.static_folder = "../tests/static"
    app.template_folder = "./templates"
    app.before_request(log_request_info)
else:
    app.logger.debug("loading NORMAL env in init!!")
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
