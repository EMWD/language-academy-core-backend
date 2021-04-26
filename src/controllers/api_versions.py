from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from libs.debugger.debugger import *
# from src.models.users import get_users
from config import config


class ApiVersions(Resource):

    def get(self, id=0):

        try:
            id = int(id)
        except ValueError:
            return jsonify("API VERSION ID MUST BE NUMBER")

        all_api_versions = config.get_value(['API_VERSIONS'])

        if id > len(all_api_versions):
            return jsonify("THIS API VERSION IS DOESNT EXIST")

        return jsonify(all_api_versions)
