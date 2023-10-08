import os
import requests
from flask_restful import Resource

PATH_USER = os.getenv('USERS_PATH', 'localhost:3001') if os.environ.get(
    'USERS_PATH') != 'default' else 'localhost:3001'


class VistaPong(Resource):

    def get(self):
        return 'pong orchetartor', 200


class VistaPongUser(Resource):

    def get(self):

        user = requests.get('http://{0}/users/pong'.format(PATH_USER))

        if user.status_code == 200:
            return user.json(), 200
        else:
            return user.json(), 400
