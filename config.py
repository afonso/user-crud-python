# config.py


class Config(object):
    """
    Common configurations
    """

    # Any configuration that is common across all environments


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG= True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False


class TestingConfig(Config):
    """
    Testing configurations
    """

    TESTING = True


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}