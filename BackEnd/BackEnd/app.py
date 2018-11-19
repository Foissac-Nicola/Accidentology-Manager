from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)

POSTGRES = {
    'user': 'postgres',
    'pw': 'postgres',
    'db': 'my_database',
    'host': 'localhost',
    'port': '5432',
}

app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db.init_app(app)
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

