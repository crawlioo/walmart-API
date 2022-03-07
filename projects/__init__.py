from flask import Flask
from flask_sqlalchemy import SQLAlchemy


from projects.dashboard.views import dashboard_blueprint
from projects.dashboard.api.routes import dashboard_api_blueprint



# app initialization
db = SQLAlchemy()

def create_app():
    app = Flask(__name__, static_url_path="")
    
    apps_settings = "projects.config.DevelopmentConfig"
    app.config.from_object(apps_settings)

    # setup extension
    db.init_app(app)

    # register blueprint
    app.register_blueprint(dashboard_blueprint)

    # API blueprint
    app.register_blueprint(dashboard_api_blueprint)

    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app