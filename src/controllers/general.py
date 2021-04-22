import random
from flask import Flask
from flask_restful import Api, Resource, reqparse
from data.quotes import quotes
# from libs.debugger.debugger import *
from src.models.general import *

class Quote(Resource):

    def get(self, id=''):
            
        # if not id:
        #     return random.choice(quotes), 200
        # for quote in quotes:
        #     if(quote["id"] == id):
        #         return quote, 200
        # return "Quote not found", 404

        return getSMTH(id)

    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("author")
        parser.add_argument("quote")
        params = parser.parse_args()
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
