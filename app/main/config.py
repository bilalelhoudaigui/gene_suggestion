class Config:
    DB_TYPE = "mysql+pymysql"
    DB_USER = "anonymous"
    DB_PASS = ""
    DB_NAME = "ensembl_website_97"
    HOST = "ensembldb.ensembl.org"
    PORT = 3306


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = Config.DB_TYPE + "://" + Config.DB_USER + ":" + Config.DB_PASS + "@" \
                              + Config.HOST + ":" + str(Config.PORT) + "/" + Config.DB_NAME
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    # A different test database can be defined here
    SQLALCHEMY_DATABASE_URI = Config.DB_TYPE + "://" + Config.DB_USER + ":" + Config.DB_PASS + "@" \
                              + Config.HOST + ":" + str(Config.PORT) + "/" + Config.DB_NAME
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # A different test database can be defined here
    SQLALCHEMY_DATABASE_URI = Config.DB_TYPE + "://" + Config.DB_USER + ":" + Config.DB_PASS + "@" \
                              + Config.HOST + ":" + str(Config.PORT) + "/" + Config.DB_NAME

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
