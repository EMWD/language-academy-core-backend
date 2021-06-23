from flask import jsonify
from flask_restful import Resource, reqparse
from libs.debugger.debugger import *
from src.models.auth import AuthModel
from src.models.users import UsersModel
from src.db.setup import Db


class ApiAuth(Resource):

    def get(self, id=''):
        pass

    def split_name(self, fullname):
            name_parts = fullname.split(' ')

            if len(name_parts) == 1:
                return [fullname, fullname]
            if len(name_parts) == 2:
                return [name_parts[0], name_parts[1]]

            return 0

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument("email")
        parser.add_argument("fullname")
        parser.add_argument("googleuid")
        params = parser.parse_args()
        
        email = params["email"]
        fullname = params["fullname"]
        googleuid = params["googleuid"]
        
        if email and fullname:
            error = ''
            auth_model = AuthModel(Db)
            user_model = UsersModel()

            attempt = auth_model.try_auth(email)
            if attempt:
                return jsonify('OK')

            if not attempt:
                name_parts = self.split_name(fullname)
                if name_parts:
                    name, last_name = name_parts
                    password = '1'
                    if not user_model.add_user(name, last_name, password, email, googleuid):
                        error = 'CANT ADD NEW USER'
                else:
                    error = "PROBLEM WITH NAME"

            exist_response = user_model.get_user_by_guid(googleuid)
            if exist_response:
                return exist_response

        if error:
            return jsonify("WE GOT PROBLEM")
        else:
            user_model = UsersModel()
            response = user_model.get_user_by_guid(googleuid)

            if response:
                return response
            else:
                return jsonify([])