from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from libs.debugger.debugger import *
from src.models.links import LinksModel
from src.helpers.json_formatter import jf


class ApiLinks(Resource):

    def get(self, id=''):
        links_model = LinksModel()

        response = links_model.get_all_links()
        if response:
            return response

        return jsonify("NO DATA")

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("link", action='append')
        parsed_args = parser.parse_args()
        links = parsed_args["link"]

        if links:
            links_model = LinksModel()
            res = links_model.add_links(links)

            if res:
                return jsonify("LINKS, SUCCESS")
            else:
                return jsonify("WE GOT PROBLEM")

        else:
            return jsonify("NOT ENOUGH PARAMS")
