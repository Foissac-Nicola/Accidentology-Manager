from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class ServiceIndicator(Resource):

    def get(self):
        return {"get": "example"}

    def post(self):
        return {"post": "example"}

    def delete(self):
        return {"delete": "example"}

    def put(self):
        return {"put": "example"}

api.add_resource(ServiceIndicator,'/Indicator')
if __name__ == '__main__':
    app.run()
