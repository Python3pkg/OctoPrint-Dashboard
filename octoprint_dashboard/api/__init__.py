from octoprint_dashboard import app
from flask_restful import Api
from .printer import PrinterApi
from .group import GroupApi
from .file import FileApi

api = Api(app)

api.add_resource(PrinterApi, '/printer')
api.add_resource(GroupApi, '/group')
api.add_resource(FileApi, '/upload')