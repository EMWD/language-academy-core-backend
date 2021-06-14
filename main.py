import sys
from flask import Flask
from flask_restful import Api, Resource, reqparse
from config import *
from src.controllers import *

app = Flask(__name__)
api = Api(app)

#base API endpoints
#
# versions
api.add_resource(ApiVersions, "/api/getversions", "/api/getversion/<string:id>")
# endpoints
api.add_resource(ApiEndpoints, "/api/getendpoints", "/api/getendpoint/<string:id>")
# users
api.add_resource(ApiUsers, "/api/users", "/api/user/<string:id>")
# groups
api.add_resource(ApiGroups, "/api/groups", "/api/group/<string:id>")
# hometasks
api.add_resource(ApiHometasks, "/api/hometasks")
# auth
api.add_resource(ApiAuth, "/api/auth")
