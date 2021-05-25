import sys
from flask import Flask
from flask_restful import Api, Resource, reqparse
from config import *
from libs.debugger.debugger import de, d 
from src.controllers import *

app = Flask(__name__)

api = Api(app)

# versions
api.add_resource(ApiVersions, "/api/getversions", "/api/getversion/<string:id>")
# endpoints
api.add_resource(ApiEndpoints, "/api/getendpoints", "/api/getendpoint/<string:id>")
# users
api.add_resource(ApiUsers, "/api/users", "/api/user/<string:id>")
# groups
api.add_resource(ApiGroups, "/api/groups")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
