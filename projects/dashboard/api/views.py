from flask import jsonify
from flask_restx import Resource

from projects.scraper.walmart import process_scraper


class WalmartApi(Resource):

    def get(self, keywords: str):
        results = process_scraper(keywords)
        return jsonify(
            {'message': results}
        )
