from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from libs.debugger.debugger import *
from src.models.general import getSMTH
from config import config


class ApiEndpoints(Resource):

    def get(self, id=0):

        all_api_versions = config.get_value(['API_ENDPOINTS'])

        return jsonify(all_api_versions)
