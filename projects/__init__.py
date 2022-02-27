from flask import Flask


from projects.dashboard.views import dashboard_blueprint
from projects.dashboard.api.routes import dashboard_api_blueprint



def create_app():
    app = Flask(__name__, static_url_path="")
    
    apps_settings = "projects.config.DevelopmentConfig"
    app.config.from_object(apps_settings)

    # register blueprint
    app.register_blueprint(dashboard_blueprint)

    # API blueprint
    app.register_blueprint(dashboard_api_blueprint)

    return app