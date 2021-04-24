import sys
from flask import Flask
from flask_restful import Api, Resource, reqparse
from config import *
from libs.debugger.debugger import de, d 
from src.controllers import *

app = Flask(__name__)

api = Api(app)

# api.add_resource(ApiUsers, "/api", "/api/<string:id>")

api.add_resource(ApiVersions, "/api/getall", "/api/getall/<string:id>")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
