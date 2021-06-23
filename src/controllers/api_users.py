from flask import jsonify
from flask_restful import Resource, reqparse
from src.db.setup import Db
from libs.debugger.debugger import *
from src.models.users import UsersModel


class ApiUsers(Resource):

    def get(self, id=''):
        users_model = UsersModel()
        response = []

        if id:
            response = users_model.get_user(id)
        else:
            response = users_model.get_all_users()

        if response:
            return response
        
        return jsonify([])

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("lastname")
        parser.add_argument("password")
        parser.add_argument("email")
        params = parser.parse_args()

        name = params["name"]
        last_name = params["lastname"]
        password = params["password"]
        email = params["email"]

        if name and last_name and password:

            users_model = UsersModel()
            res = users_model.add_user(name, last_name, password, email)

            if res:
                return jsonify("SUCCESS")
            else:
                return jsonify("WE GOT PROBLEM")

        else:
            return jsonify("NOT ENOUGH PARAMS")
