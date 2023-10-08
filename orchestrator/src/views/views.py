from flask_restful import Resource


class VistaPong(Resource):

    def get(self):
        return 'pong orchetartor', 200
