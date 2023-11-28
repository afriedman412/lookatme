# config.py
class Config:
    DEBUG = False
    YAML_FILES = ["tag_templates", "about", "entries"]


class DevelopmentConfig(Config):
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True


class TestingConfig(Config):
    TESTING = "true"
    FLASK_ENV = "test"
    CONFIGFILE = "pee"


class ProductionConfig(Config):
    pass
