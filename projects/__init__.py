import os
from flask import Flask



def create_app():
    app = Flask(__name__, static_url_path="")
    
    apps_settings = "projects.config.DevelopmentConfig"
    app.config.from_object(apps_settings)


    return app