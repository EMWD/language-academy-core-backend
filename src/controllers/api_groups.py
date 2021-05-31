from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from libs.debugger.debugger import *
from src.models.groups import GroupModel 


class ApiGroups(Resource):

    def get(self, id=''):
        group_model = GroupModel()
        response = []

        # id is group_name
        if id:
            response = group_model.get_group_by_name(id)
        else:
            response = group_model.get_all_groups()

        if response:
            return response
        
        return jsonify("NO DATA")

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("lang")
        parser.add_argument("level")
        parser.add_argument("numbers")
        parser.add_argument("action")
        params = parser.parse_args()

        print(params)

        name = params["name"]
        lang = params["lang"]
        level = params["level"]
        numbers = params["numbers"]
        action = params["action"]

        if name:

            group_model = GroupModel()
            res = group_model.add_group(name, lang, level, numbers, action)

            if res:
                return jsonify("GROUPS, SUCCESS")
            else:
                return jsonify("WE GOT PROBLEM")
        
        else:
            return jsonify("NOT ENOUGH PARAMS")