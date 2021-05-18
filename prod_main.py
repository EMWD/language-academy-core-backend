import sys
from flask import Flask
from flask_restful import Api, Resource, reqparse
from config import *
from libs.debugger.debugger import de, d 
from src.controllers import *

app = Flask(__name__)

api = Api(app)

# get versions
api.add_resource(ApiVersions, "/api/getversions", "/api/getversion/<string:id>")
# get endpoints
api.add_resource(ApiEndpoints, "/api/getendpoints", "/api/getendpoint/<string:id>")
# get users
api.add_resource(ApiUsers, "/api/users", "/api/user/<string:id>")

# Made normal resolve about 2 diffrent start points
if __name__ == '__main__':
    app.run(host='194.67.110.179', port=5000)
