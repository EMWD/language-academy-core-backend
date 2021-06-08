from flask import jsonify
from flask_restful import Resource, reqparse
from libs.debugger.debugger import *
from src.models.auth import AuthModel
from src.models.users import UsersModel
from src.db.setup import Db


class ApiAuth(Resource):

    def get(self, id=''):
        pass

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument("email")
        parser.add_argument("fullname")
        parser.add_argument("googleuid")
        params = parser.parse_args()
        
        email = params["email"]
        fullname = params["fullname"]
        # googleuid = params["googleuid"]
        
        if email:
            res = ''
            auth_model = AuthModel(Db)
            user_model = UsersModel()

            attempt = auth_model.try_auth(email)
            
            if attempt:
                return jsonify('OK')

            if not attempt:
                name, last_name = fullname, fullname
                password = '1'
                if user_model.add_user(name, last_name, password, email):
                    res = 'REG NEW USER'

        if res:
            return jsonify(res + ", SUCCESS")
        else:
            return jsonify("WE GOT PROBLEM")


        def split_name(self, name):
            return name.split(' ')
