import sys
from flask import Flask
from flask_restful import Api, Resource, reqparse
from config import *
from libs.debugger.debugger import *
from src.controllers import Quote

app = Flask(__name__)

api = Api(app)

api.add_resource(Quote, "/api", "/api/<int:id>")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
