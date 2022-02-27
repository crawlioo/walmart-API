from pathlib import Path
from dotenv import load_dotenv

load_dotenv(dotenv_path='./../.env')

class BaseConfig:
    BASE_DIR = Path(__file__).parent
    TESTING = False
    SECRET_KEY = '@Crawlio_SecretKey101'

class DevelopmentConfig(BaseConfig):
    DEBUG = True
