from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from libs.debugger.debugger import *
# from src.models.users import get_users
from config import config


class ApiFakeUsers(Resource):

    def get(self, id=0):

        api_fake_users = config.get_value(['FAKE_USERS'])

        return jsonify(api_fake_users)
