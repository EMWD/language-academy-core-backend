from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from libs.debugger.debugger import *
from src.models.hometasks import HometaskModel


class ApiHometasks(Resource):

    def get(self, id=''):
        hometask_model = HometaskModel()

        if not id:
            return jsonify(hometask_model.get_all_hometasks())

        response = hometask_model.get_user(id)

        if not response:
            return jsonify("NO DATA OR WRONG REQUEST")

        return jsonify(response)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("description")
        parser.add_argument("name")
        parser.add_argument("duedate")
        parser.add_argument("link")
        parser.add_argument("action")
        params = parser.parse_args()

        description = params["description"]
        name = params["name"]
        duedate = params["duedate"]
        link = params["link"]
        action = params["action"]

        if name:
            hometask_model = HometaskModel()
            res = hometask_model.add_hometask(
                description, name, duedate, link, action)

            if res:
                return jsonify("HOMETASK, SUCCESS")
            else:
                return jsonify("WE GOT PROBLEM")

        else:
            return jsonify("NOT ENOUGH PARAMS")
