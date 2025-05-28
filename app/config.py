class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"
    SQLACHEMY_TRACK_MODIFICATIONS = False
    
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    