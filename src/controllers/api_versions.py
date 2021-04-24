from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from libs.debugger.debugger import *
from src.models.general import getSMTH
from config import *


class ApiVersions(Resource):

    config = Config()

    def get(self, id):
        
        #TODO
        # Make spec brackets snippet

        try:
            id = int(id)
        except ValueError:
            return jsonify("API VERSION ID MUST BE NUMBER")

        if id:
            api_versions = self.config.get_value(['API_ENDPOINTS'])

            if id > len(api_versions):
                return jsonify("THIS API VERSION IS DOESNT EXIST")

        all_api_versions = self.config.get_value(['API_ENDPOINTS', '1'])
        return jsonify(all_api_versions)
