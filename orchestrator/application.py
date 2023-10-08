from src import create_app
from flask_restful import Api
from flask_jwt_extended import JWTManager
from src.views import VistaPong

application = create_app('default')
app_context = application.app_context()
app_context.push()

api = Api(application)
api.add_resource(VistaPong, '/')

jwt = JWTManager(application)

if __name__ == "__main__":
    application.run(host = "0.0.0.0", port = 3000, debug = True)