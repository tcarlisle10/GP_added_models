import os

class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:{password}@localhost/trade_x_change' # needs to be changed to skill_x_change
    DEBUG = True


class TextingConfig:
    pass

class ProductionConfig:
    pass