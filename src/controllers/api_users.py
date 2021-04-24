from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from libs.debugger.debugger import *
from src.models.general import getSMTH


class ApiUsers(Resource):

    def get(self, id=''):

        if not id:
            raise AssertionError("ID PARAM REQUIRED")

        response = getSMTH(id)
        if not response:
            return jsonify("NO DATA OR WRONG REQUEST")

        return jsonify(response)

    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("author")
        parser.add_argument("arg2")
        params = parser.parse_args()

        d(params)
        # exir((params)
        exit(0)
        for quote in quotes:
            if(id == quote["id"]):
                return f"Quote with id {id} already exists", 400
        quote = {
            "id": int(id),
            "author": params["author"],
            "quote": params["quote"]
        }
        quotes.append(quote)
        return quote, 201

    # TODO
    # def return_json(self, obj):
    #     return jsonify(obj)
