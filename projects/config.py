from pathlib import Path
from dotenv import load_dotenv


class BaseConfig:
    BASE_DIR = Path(__file__).parent
    TESTING = False
    SECRET_KEY = '@Crawlio_SecretKey101'

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite://db.sqlite3"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
