from flask import Blueprint
from flask_restx import Api

from .views import WalmartApi

dashboard_api_blueprint = Blueprint("dashboard_api", __name__, template_folder='templates', static_folder='static')

dashboard_api = Api(dashboard_api_blueprint)

# routes
dashboard_api.add_resource(WalmartApi, '/api/<string:keywords>')