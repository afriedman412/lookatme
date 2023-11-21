# config.py


class Config:
    DEBUG = False
    YAML_FILES = ["tag_templates", "about", "entries"]


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass
